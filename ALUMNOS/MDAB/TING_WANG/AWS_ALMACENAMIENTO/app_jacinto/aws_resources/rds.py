import logging
import os
import json

import psycopg2
from dotenv import load_dotenv

load_dotenv()

RDS_HOST = os.environ['RDS_HOST']
RDS_PORT = os.environ['RDS_PORT']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']


def connect_to_postgres_rds(conn: psycopg2.connect) -> None:
    return conn

def create_table(conn: psycopg2.connect, query: str) -> None:
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(query)


def insert_data(conn: psycopg2.connect, data: list, query: str) -> None:
        cur = conn.cursor()
        cur.execute(query, data)
        conn.commit()
