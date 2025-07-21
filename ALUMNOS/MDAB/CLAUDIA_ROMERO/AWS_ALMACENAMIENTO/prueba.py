import logging
import os

import psycopg2
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv()

# Datos RDS PostgreSQL
RDS_HOST = os.environ['RDS_HOST']
RDS_PORT = os.environ['RDS_PORT']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']

# Datos Redshift
REDSHIFT_HOST = os.environ['REDSHIFT_HOST']
REDSHIFT_PORT = os.environ['REDSHIFT_PORT']
REDSHIFT_USER = os.environ['REDSHIFT_USER']
REDSHIFT_PASSWORD = os.environ['REDSHIFT_PASSWORD']
REDSHIFT_DB = os.environ['REDSHIFT_DB']

def connect_to_postgres_rds():
    return psycopg2.connect(
        host=RDS_HOST,
        port=RDS_PORT,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB
    )

def connect_to_redshift():
    return psycopg2.connect(
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT,
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD,
        database=REDSHIFT_DB
    )

def extract_schema_and_type_from_postgres(conn, table_name):
    cur = conn.cursor()
    cur.execute(f"""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = '{table_name}'
        ORDER BY ordinal_position;
    """)
    return cur.fetchall()

def extract_data_from_postgres(conn, table_name):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name};")
    return cur.fetchall()

def create_table_from_schema_in_redshift(conn, table_name, schema):
    cur = conn.cursor()
    ddl = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(f'{col} {dtype}' for col, dtype in schema)});"
    cur.execute(ddl)
    conn.commit()

def insert_data_redshift(conn, table_name, schema, data):
    cur = conn.cursor()
    columns = ', '.join([col for col, _ in schema])
    placeholders = ', '.join(['%s'] * len(schema))
    insert = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"
    for row in data:
        cur.execute(insert, row)
    conn.commit()

if __name__ == "__main__":
    tables = ["airplanes", "flights", "passengers", "flight_passengers"]

    logging.info("🔌 Conectando a RDS PostgreSQL...")
    rds_conn = connect_to_postgres_rds()

    logging.info("🔌 Conectando a Redshift...")
    redshift_conn = connect_to_redshift()

    for table in tables:
        logging.info(f"📋 Procesando tabla: {table}")
        schema = extract_schema_and_type_from_postgres(rds_conn, table)
        data = extract_data_from_postgres(rds_conn, table)

        logging.info("🧱 Creando tabla en Redshift...")
        create_table_from_schema_in_redshift(redshift_conn, table, schema)

        if data:
            logging.info(f"📥 Insertando {len(data)} filas...")
            insert_data_redshift(redshift_conn, table, schema, data)
        else:
            logging.info("⚠️ No hay datos para insertar.")

    rds_conn.close()
    redshift_conn.close()
    logging.info("✅ ¡Carga completada!")
