import logging
import os
import json
import psycopg2
from dotenv import load_dotenv
from pyiceberg.partitioning import PartitionSpec
from pyiceberg.schema import Schema
from pyiceberg.types import (
    IntegerType,
    NestedField,
    StringType,
    TimestampType,
)

from data.initial_info import passengers
from aws_resources.rds import *
from aws_resources.redshift import *
from aws_resources.iceberg import *


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

BUCKET = os.environ['WAREHOUSE_BUCKET']
REGION = os.environ['AWS_REGION']


def main_passengers():
    try:
        conn_postgres = psycopg2.connect(
            host=RDS_HOST,
            port=RDS_PORT,
            user=RDS_USER,
            password=RDS_PASSWORD,
            database=RDS_DB
        )
        connect_to_postgres_rds(conn_postgres)
        logging.info("Connected to RDS")
        conn_redshift = psycopg2.connect(
            host=REDSHIFT_HOST,
            port=REDSHIFT_PORT,
            user=REDSHIFT_USER,
            password=REDSHIFT_PASSWORD,
            database=REDSHIFT_DB
        )
        connect_to_redshift(conn_redshift)
        logging.info("Connected to Redshift")

        input("Please, press Enter to start RDS process...")

        logging.info("Starting RDS process")
        logging.info("Creating table in postgres")
        query_postgres_create = """CREATE TABLE IF NOT EXISTS passengers_info (
                id serial PRIMARY KEY,
                passengerId VARCHAR(50),
                name VARCHAR(50),
                nationalId VARCHAR(50),
                dateOfBirth DATE,
                created_at TIMESTAMP);"""
        create_table(conn_postgres, query_postgres_create)
        postgres_table = "passengers_info"
        logging.info(f"Table {postgres_table} created in postgres")

        logging.info("Inserting data to postgres table")
        for passenger in passengers:
            data_passengers_info = (
                passenger["passengerId"],
                passenger["name"],
                passenger["nationalId"],
                passenger["dateOfBirth"]
            )
            query_postgres_insert = """INSERT INTO passengers_info 
                (passengerId, name, nationalId, dateOfBirth, created_at) 
                VALUES 
                (%s,%s,%s,TO_DATE(%s, 'YYYY-MM-DD'),NOW());"""
            insert_data(conn_postgres, data_passengers_info, query_postgres_insert)
        logging.info(f"Data inserted to table {postgres_table} in postgres")
        logging.info("RDS completed")

        input("Please, press Enter to start Redshift process...")

        logging.info("Starting Redshift process")
        logging.info("Extracting data from postgres")
        data_rows = extract_data_from_postgres(conn_postgres, postgres_table)
        logging.info("Data extracted from postgres")
        logging.info("Extracting schema and type from postgres")
        postgres_schema = extract_schema_and_type_from_postgres(conn_postgres, postgres_table)
        logging.info("Schema extracted")
        logging.info("Creating table in redshift")
        create_table_from_schema_in_aws_redshift(conn_redshift, postgres_table, postgres_schema)
        logging.info("Table created in redshift")
        logging.info("Inserting data in redshift")
        for row in data_rows:
            insert_data_redshift(conn_redshift, postgres_table, postgres_schema, row)
        logging.info("Data inserted to redshift")
        logging.info("Redshift completed")

        input("Please, press Enter to start Iceberg process...")

        logging.info("Starting Iceberg process")
        provider = "glue"
        warehouse_bucket = BUCKET
        region = REGION
        catalog = load_catalog_iceberg(provider, warehouse_bucket, region)
        logging.info("Catalog loaded")

        database_name = "db1"
        table_name = "table_passengers_info"
        iceberg_table_identifier = f"{database_name}.{table_name}"
        iceberg_schema = Schema(
        NestedField(field_id=1, name="id", field_type=IntegerType(), required=False),
        NestedField(field_id=2, name="passengerid", field_type=StringType(), required=False),
        NestedField(field_id=3, name="name", field_type=StringType(), required=False),
        NestedField(field_id=4, name="nationalid", field_type=StringType(), required=False),
        NestedField(field_id=5, name="dateofbirth", field_type=DateType(), required=False), ####
        NestedField(field_id=6, name="created_at", field_type=TimestampType(), required=False)
        )
        partition_spec = PartitionSpec(spec_id=0)
        iceberg_table_location = f"{warehouse_bucket}{database_name}/{table_name}"
        create_table_iceberg(catalog, iceberg_schema, iceberg_table_identifier,
                                            iceberg_table_location, partition_spec)
        logging.info(f"{table_name} created in Iceberg")

        iceberg_table = catalog.load_table(iceberg_table_identifier)
        insert_data_iceberg(conn_postgres, data_rows, iceberg_table, postgres_table)
        logging.info(f"Data inserted in {table_name} in Iceberg")

        rows = read_data_iceberg(iceberg_table)
        logging.info(rows)
        logging.info("Iceberg completed")

    except Exception as e:
        logging.error(e)
    
    finally:
        if conn_postgres:
            conn_postgres.close()
        if conn_redshift:
            conn_redshift.close()
        logging.info("Connections closed")


if __name__ == "__main__":
    main_passengers()
