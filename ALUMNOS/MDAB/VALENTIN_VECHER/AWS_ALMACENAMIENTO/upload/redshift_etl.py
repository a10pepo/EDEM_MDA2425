import logging
import os

import psycopg2
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv()

# Parámetros de conexión RDS PostgreSQL
RDS_HOST = os.environ['RDS_HOST']
RDS_PORT = os.environ['RDS_PORT']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']

# Parámetros de conexión Redshift
REDSHIFT_HOST = os.environ['REDSHIFT_HOST']
REDSHIFT_PORT = os.environ['REDSHIFT_PORT']
REDSHIFT_USER = os.environ['REDSHIFT_USER']
REDSHIFT_PASSWORD = os.environ['REDSHIFT_PASSWORD']
REDSHIFT_DB = os.environ['REDSHIFT_DB']


def connect_to_postgres_rds() -> psycopg2.connect:
    return psycopg2.connect(
        host=RDS_HOST,
        port=RDS_PORT,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB
    )


def connect_to_redshift() -> psycopg2.connect:
    return psycopg2.connect(
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT,
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD,
        database=REDSHIFT_DB
    )


def extract_schema_from_postgres(conn: psycopg2.connect, table_name: str) -> list:
    cur = conn.cursor()
    cur.execute(f"""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = %s
        ORDER BY ordinal_position;
    """, (table_name,))
    schema = cur.fetchall()
    cur.close()
    return schema


def extract_data_from_postgres(conn: psycopg2.connect, table_name: str) -> list:
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name};")
    rows = cur.fetchall()
    cur.close()
    return rows


def create_table_in_redshift(conn: psycopg2.connect, table_name: str, schema: list) -> None:
    cols_ddl = ", ".join(f"{col} {dtype}" for col, dtype in schema)
    ddl = f"CREATE TABLE IF NOT EXISTS {table_name} ({cols_ddl});"
    cur = conn.cursor()
    cur.execute(ddl)
    conn.commit()
    cur.close()


def insert_rows_redshift(conn: psycopg2.connect, table_name: str, schema: list, rows: list) -> None:
    columns = [col for col, _ in schema]
    cols_sql = ", ".join(columns)
    placeholders = ", ".join(["%s"] * len(columns))
    insert_sql = f"INSERT INTO {table_name} ({cols_sql}) VALUES ({placeholders});"

    cur = conn.cursor()
    for row in rows:
        cur.execute(insert_sql, row)
    conn.commit()
    cur.close()


if __name__ == "__main__":
    tables_to_copy = [
        "airplanes",
        "passengers",
        "flights",
        "flight_passengers"
    ]

    logging.info("Conectando a RDS PostgreSQL…")
    pg_conn = connect_to_postgres_rds()
    logging.info("Conectando a Redshift…")
    rs_conn = connect_to_redshift()

    for tbl in tables_to_copy:
        logging.info(f"Procesando tabla {tbl}…")

        logging.info("  Extrayendo esquema desde PostgreSQL")
        schema = extract_schema_from_postgres(pg_conn, tbl)

        logging.info("  Creando tabla en Redshift")
        create_table_in_redshift(rs_conn, tbl, schema)

        logging.info("  Extrayendo datos desde PostgreSQL")
        data_rows = extract_data_from_postgres(pg_conn, tbl)

        if data_rows:
            logging.info(f"  Insertando {len(data_rows)} filas en Redshift")
            insert_rows_redshift(rs_conn, tbl, schema, data_rows)
        else:
            logging.info("  No hay datos para insertar")

    pg_conn.close()
    rs_conn.close()
    logging.info("¡Copiado completado!") 
