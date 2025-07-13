import psycopg2
import pandas as pd
import boto3
from pyiceberg.catalog import load_catalog

# Configuración PostgreSQL (origen)
POSTGRES_CONFIG = {
    'host': 'tu-rds-endpoint.amazonaws.com',
    'database': 'aviation_db',
    'user': 'postgres',
    'password': 'tu_password',
    'port': 5432
}

# Configuración AWS
AWS_CONFIG = {
    'bucket': 'tu-bucket-s3',
    'region': 'us-east-1'
}

def extract_from_postgres():
    """Extraer datos de PostgreSQL"""
    conn = psycopg2.connect(**POSTGRES_CONFIG)
    
    airplanes_df = pd.read_sql("SELECT * FROM airplanes", conn)
    passengers_df = pd.read_sql("SELECT * FROM passengers", conn)
    flights_df = pd.read_sql("SELECT * FROM flights", conn)
    
    conn.close()
    return airplanes_df, passengers_df, flights_df

def load_to_s3_parquet(df, table_name):
    """Cargar DataFrame como Parquet en S3"""
    s3 = boto3.client('s3')
    
    # Convertir a Parquet
    parquet_file = f"{table_name}.parquet"
    df.to_parquet(parquet_file, index=False)
    
    # Subir a S3
    s3_key = f"aviation_data/{table_name}/{table_name}.parquet"
    s3.upload_file(parquet_file, AWS_CONFIG['bucket'], s3_key)
    
    print(f"Subido {table_name} a S3: s3://{AWS_CONFIG['bucket']}/{s3_key}")

def create_glue_table(table_name, columns):
    """Crear tabla en AWS Glue Catalog"""
    glue = boto3.client('glue')
    
    # Definir columnas para Glue
    glue_columns = []
    for col, dtype in columns.items():
        if 'int' in str(dtype):
            glue_type = 'bigint'
        else:
            glue_type = 'string'
        glue_columns.append({'Name': col, 'Type': glue_type})
    
    # Crear tabla
    try:
        glue.create_table(
            DatabaseName='aviation_db',
            TableInput={
                'Name': table_name,
                'StorageDescriptor': {
                    'Columns': glue_columns,
                    'Location': f"s3://{AWS_CONFIG['bucket']}/aviation_data/{table_name}/",
                    'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
                    'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
                    'SerdeInfo': {
                        'SerializationLibrary': 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
                    }
                },
                'TableType': 'EXTERNAL_TABLE'
            }
        )
        print(f"Tabla {table_name} creada en Glue Catalog")
    except Exception as e:
        print(f"Error creando tabla {table_name}: {e}")

def main():
    try:
        print("Extrayendo datos de PostgreSQL...")
        airplanes_df, passengers_df, flights_df = extract_from_postgres()
        
        print("Cargando datos en S3...")
        load_to_s3_parquet(airplanes_df, 'airplanes')
        load_to_s3_parquet(passengers_df, 'passengers')
        load_to_s3_parquet(flights_df, 'flights')
        
        print("Creando tablas en Glue Catalog...")
        create_glue_table('airplanes', airplanes_df.dtypes)
        create_glue_table('passengers', passengers_df.dtypes)
        create_glue_table('flights', flights_df.dtypes)
        
        print("¡EL a Data Lakehouse completado!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()