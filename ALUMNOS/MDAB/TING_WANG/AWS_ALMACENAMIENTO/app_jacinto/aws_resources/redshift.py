import logging
import os

import psycopg2
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

REDSHIFT_HOST = os.environ['REDSHIFT_HOST']
REDSHIFT_PORT = os.environ['REDSHIFT_PORT']
REDSHIFT_USER = os.environ['REDSHIFT_USER']
REDSHIFT_PASSWORD = os.environ['REDSHIFT_PASSWORD']
REDSHIFT_DB = os.environ['REDSHIFT_DB']


def connect_to_redshift(conn: psycopg2.connect) -> None:
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