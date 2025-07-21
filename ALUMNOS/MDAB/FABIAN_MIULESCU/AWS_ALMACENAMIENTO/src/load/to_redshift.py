import boto3
import polars as pl
import psycopg2
from io import BytesIO

from src.config.settings import settings
from src.extract.from_postgres import extract_from_postgres


def get_redshift_connection():
    conn = psycopg2.connect(
        dbname=settings.redshift_db,
        user=settings.redshift_user,
        password=settings.redshift_password,
        host=settings.redshift_host,
        port=settings.redshift_port
    )
    return conn

def upload_df_to_s3_as_parquet(df: pl.DataFrame, bucket: str, key: str):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.aws_access_key_id,
        aws_secret_access_key=settings.aws_secret_access_key,
        region_name=settings.aws_region
    )
    buffer = BytesIO()
    df.write_parquet(buffer)
    buffer.seek(0)
    s3_client.upload_fileobj(buffer, bucket, key)
    print(f"Archivo Parquet cargado en s3://{bucket}/{key}")

def type_mapper(polars_type):
    mapping = {
        pl.Int64: "BIGINT",
        pl.Int32: "INTEGER",
        pl.Float64: "FLOAT8",
        pl.Float32: "FLOAT4",
        pl.String: "VARCHAR(256)",
        pl.Date: "DATE",
        pl.Datetime: "TIMESTAMP",
        pl.Boolean: "BOOLEAN"
    }
    return mapping.get(polars_type, "VARCHAR(256)")

def generate_redshift_create_table_ddl(df: pl.DataFrame, table_name: str) -> str:
    columns = [f'"{col}" {type_mapper(dtype)}' for col, dtype in df.schema.items()]
    return f"CREATE TABLE IF NOT EXISTS {table_name} (\n    " + ",\n    ".join(columns) + "\n);"

def run_redshift_etl_for_table(table_name: str, conn):
    print(f"--- Iniciando ETL para la tabla: {table_name} ---")
    df = extract_from_postgres(table_name)
    if df.is_empty():
        print(f"La tabla {table_name} está vacía. Saltando ETL.")
        return

    ddl = generate_redshift_create_table_ddl(df, table_name)
    cursor = conn.cursor()
    print("Ejecutando DDL en Redshift:")
    print(ddl)
    cursor.execute(ddl)
    conn.commit()

    s3_key = f"parquet/{table_name}/{table_name}.parquet"
    upload_df_to_s3_as_parquet(df, settings.s3_bucket_name, s3_key)

    copy_command = f"""
        COPY {table_name}
        FROM 's3://{settings.s3_bucket_name}/{s3_key}'
        FORMAT AS PARQUET;
    """
    print("Ejecutando comando COPY en Redshift...")
    cursor.execute(f"TRUNCATE TABLE {table_name};") 
    cursor.execute(copy_command)
    conn.commit()
    cursor.close()
    print(f"ETL para la tabla {table_name} completado exitosamente.")

def main():
    conn = get_redshift_connection()
    tables = ['airplanes', 'passengers', 'flights', 'flight_passengers']
    for table in tables:
        try:
            run_redshift_etl_for_table(table, conn)
        except Exception as e:
            print(f"Error en el ETL para la tabla {table}: {e}")
            conn.rollback()
    conn.close()

if __name__ == "__main__":
    main()
