import os
import logging
import psycopg2
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv()

# Variables de entorno
RDS_HOST = os.environ['RDS_HOST']
RDS_PORT = os.environ['RDS_PORT']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']

REDSHIFT_HOST = os.environ['REDSHIFT_HOST']
REDSHIFT_PORT = os.environ['REDSHIFT_PORT']
REDSHIFT_USER = os.environ['REDSHIFT_USER']
REDSHIFT_PASSWORD = os.environ['REDSHIFT_PASSWORD']
REDSHIFT_DB = os.environ['REDSHIFT_DB']

def connect_to_postgres_rds() -> psycopg2.connect:
    conn = psycopg2.connect(
        host=RDS_HOST,
        port=RDS_PORT,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB
    )
    return conn

def connect_to_redshift() -> psycopg2.connect:
    conn = psycopg2.connect(
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT,
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD,
        database=REDSHIFT_DB
    )
    return conn

# Función pedida: crear BBDD si no existe
def create_database(conn: psycopg2.connect) -> None:
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname='testdb';")
    exists = cur.fetchone()
    if not exists:
        cur.execute("CREATE DATABASE testdb;")

def get_table_schema(conn, table_name):
    with conn.cursor() as cur:
        cur.execute(f"""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_name = '{table_name}'
            ORDER BY ordinal_position
        """)
        return cur.fetchall()

def extract_data(conn, table_name):
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM {table_name}")
        return cur.fetchall()

def create_table_if_not_exists(conn, table_name, schema):
    columns = ', '.join([f"{col} {dtype}" for col, dtype in schema])
    with conn.cursor() as cur:
        cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
    conn.commit()

def insert_data(conn, table_name, schema, data):
    columns = ', '.join([col for col, _ in schema])
    placeholders = ', '.join(['%s'] * len(schema))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    with conn.cursor() as cur:
        for row in data:
            cur.execute(query, row)
    conn.commit()

def run_etl(table_name):
    try:
        logging.info("Conectando a RDS...")
        rds_conn = connect_to_postgres_rds()
        logging.info("Conectando a Redshift...")
        redshift_conn = connect_to_redshift()

        # create_database(rds_conn)  # Solo descomenta si quieres usarla

        logging.info("Extrayendo esquema de tabla...")
        schema = get_table_schema(rds_conn, table_name)

        logging.info("Extrayendo datos de RDS...")
        data = extract_data(rds_conn, table_name)

        logging.info("Creando tabla en Redshift si no existe...")
        create_table_if_not_exists(redshift_conn, table_name, schema)

        logging.info("Insertando datos en Redshift...")
        insert_data(redshift_conn, table_name, schema, data)

        logging.info("Proceso ETL completado.")

    except Exception as e:
        logging.error(f"Error durante el proceso ETL: {e}")

    finally:
        rds_conn.close()
        redshift_conn.close()
        logging.info("Conexiones cerradas.")

if __name__ == "__main__":
    run_etl("test_table_name")
