import logging
import os
from typing import List, Dict, Any, Tuple
import psycopg2
from dotenv import load_dotenv
import time

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


def extract_data_from_postgres(conn: psycopg2.connect, table_names: List[str]) -> Dict[str, List[Any]]:
    cur = conn.cursor()
    results = {}
    for table_name in table_names:
        cur.execute(f"SELECT * FROM {table_name};")
        results[table_name] = cur.fetchall()
    return results


def extract_schema_and_type_from_postgres(conn: psycopg2.connect, table_names: List[str]) -> Dict[str, List[Tuple[str, str]]]:
    cur = conn.cursor()
    results = {}
    for table_name in table_names:
        cur.execute(f"""
            SELECT column_name, data_type
            FROM information_schema.columns 
            WHERE table_name = %s
            ORDER BY ordinal_position;
        """, (table_name,))
        results[table_name] = cur.fetchall()
    return results


def create_tables_from_schemas_in_redshift(conn: psycopg2.connect, table_names: List[str], schemas: Dict[str, List[Tuple[str, str]]]) -> None:
    cur = conn.cursor()
    for table_name in table_names:
        schema = schemas[table_name]
        query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                    {', '.join([f'{column[0]} {column[1]}' for column in schema])}
                    );"""
        cur.execute(query)
    conn.commit()


def insert_data_redshift(conn: psycopg2.connect, table_name: str, schema: List[Tuple[str, str]], data: List[Tuple]) -> None:
    cur = conn.cursor()
    columns = ', '.join([column[0] for column in schema])
    placeholders = ', '.join(['%s'] * len(schema))
    query = f"""INSERT INTO {table_name} ({columns})
                VALUES ({placeholders});"""
    cur.executemany(query, data)
    conn.commit()


if __name__ == "__main__":
    postgres_tables = ["flights", "passengers", "flight_passengers"]

    while True:
        logging.info("Connecting to RDS")
        conn_postgres = connect_to_postgres_rds()
        conn_redshift = connect_to_redshift()
        logging.info("Connected to RDS")

        logging.info("Extracting data from postgres")
        data_rows = extract_data_from_postgres(conn_postgres, postgres_tables)
        logging.info("Data extracted")

        logging.info("Extracting schema and type from postgres")
        schema = extract_schema_and_type_from_postgres(conn_postgres, postgres_tables)
        logging.info("Schema extracted")

        logging.info("Creating tables in redshift")
        create_tables_from_schemas_in_redshift(conn_redshift, postgres_tables, schema)
        logging.info("Tables created")

        logging.info("Inserting data in redshift")
        for table_name in postgres_tables:
            insert_data_redshift(conn_redshift, table_name, schema[table_name], data_rows[table_name])
            logging.info(f"Data inserted into {table_name}")

        conn_postgres.close()
        conn_redshift.close()

        time.sleep(10)