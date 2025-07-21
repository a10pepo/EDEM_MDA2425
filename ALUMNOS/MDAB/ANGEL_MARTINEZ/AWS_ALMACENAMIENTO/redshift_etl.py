import logging
import os

import psycopg2
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

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


def create_database(conn: psycopg2.connect) -> None:
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname='testdb';")
    exists = cur.fetchone()
    if not exists:
        cur.execute("CREATE DATABASE testdb;")


def extract_data_from_postgres(conn: psycopg2.connect, table_name: str) -> None:
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name};")
    data = cur.fetchall()
    return data


def extract_schema_and_type_from_postgres(conn: psycopg2.connect, table_name: str) -> list:
    cur = conn.cursor()
    cur.execute(f"""SELECT column_name, data_type
                    FROM information_schema.columns 
                    WHERE table_name = '{table_name}'
                    ORDER BY ordinal_position;""")  # Ensure correct column order
    data = cur.fetchall()
    return data


def create_table_from_schema_in_aws_redshift(conn: psycopg2.connect, table_name: str, schema: list) -> None:
    cur = conn.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                {', '.join([f'{column[0]} {column[1]}' for column in schema])}
                );"""
    cur.execute(query)
    conn.commit()


def insert_data_redshift(conn: psycopg2.connect, table_name: str, schema: list, data: tuple) -> None:
    cur = conn.cursor()
    columns = ', '.join([column[0] for column in schema])
    placeholders = ', '.join(['%s'] * len(data))
    query = f"""INSERT INTO {table_name} ({columns})
                VALUES ({placeholders});
            """
    cur.execute(query, data)
    conn.commit()


if __name__ == "__main__":
    postgres_table = 'test_table_name'
    logging.info("Connecting to RDS")
    conn_postgres = connect_to_postgres_rds()
    conn_redshift = connect_to_redshift()
    logging.info("Connected to RDS")
    logging.info("Extracting data from postgres")
    data_rows = extract_data_from_postgres(conn_postgres, postgres_table)
    print(data_rows)
    logging.info("Data extracted")
    logging.info("Extracting schema and type from postgres")
    schema = extract_schema_and_type_from_postgres(conn_postgres, postgres_table)
    print(schema)
    logging.info("Schema extracted")
    logging.info("Creating table in redshift")
    create_table_from_schema_in_aws_redshift(conn_redshift, postgres_table, schema)
    logging.info("Table created")
    logging.info("Inserting data in redshift")
    for row in data_rows:
        insert_data_redshift(conn_redshift, postgres_table, schema, row)
        logging.info("Data inserted")
    conn_postgres.close()
    conn_redshift.close()
