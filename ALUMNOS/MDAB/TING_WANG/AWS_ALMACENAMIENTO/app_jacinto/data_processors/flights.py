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

from data.initial_info import flights
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


def main_flights():
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
        query_postgres_create_flights = """CREATE TABLE IF NOT EXISTS flights (
                id serial PRIMARY KEY,
                flightId VARCHAR(50),
                plateNumber VARCHAR(50),
                arrivalTime VARCHAR(50),
                departureTime VARCHAR(50),
                fuelConsumption INT,
                occupiedSeats INT,
                origin VARCHAR(50),
                destination VARCHAR(50),
                created_at TIMESTAMP);"""
        query_postgres_create_passengers = """CREATE TABLE IF NOT EXISTS flights_passengers (
                id serial PRIMARY KEY,
                flightId VARCHAR(50),
                passengerId VARCHAR(100),
                passengerStatus VARCHAR(100));"""
        create_table(conn_postgres, query_postgres_create_flights)
        logging.info("Table flights created in postgres")
        create_table(conn_postgres, query_postgres_create_passengers)
        logging.info("Table flights_passengers created in postgres")

        logging.info("Inserting data to postgres table")
        for flight in flights:
            data_flights = (
                flight["flightId"],
                flight["plateNumber"],
                flight["arrivalTime"],
                flight["departureTime"],
                flight["fuelConsumption"],
                flight["occupiedSeats"],
                flight["origin"],
                flight["destination"]
            )
            query_postgres_insert_flights = """INSERT INTO flights 
                (flightId, plateNumber, arrivalTime, departureTime, fuelConsumption, occupiedSeats, origin, destination, created_at) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s, NOW());"""
            insert_data(conn_postgres, data_flights, query_postgres_insert_flights)
            logging.info("Flights data inserted to postgres")

            for passenger in flight["passengerIds"]:
                passenger_values = (
                    flight["flightId"],
                    passenger[0],
                    passenger[1]
                )
            query_postgres_insert_passengers = """INSERT INTO flights_passengers
                                (flightId, passengerId, passengerStatus)
                                VALUES (%s, %s, %s);"""
            insert_data(conn_postgres, passenger_values, query_postgres_insert_passengers)
            logging.info("Passengers data inserted to postgres")
        logging.info("RDS completed")

        input("Please, press Enter to start Redshift process...")

        logging.info("Starting Redshift process")
        logging.info("Extracting data from postgres")
        postgres_table_flights = 'flights'
        postgres_table_passengers = "flights_passengers"
        data_flights = extract_data_from_postgres(conn_postgres, postgres_table_flights)
        logging.info("Flight data extracted")
        data_flights_passengers = extract_data_from_postgres(conn_postgres, postgres_table_passengers)
        logging.info("Passengers data extracted")

        logging.info("Extracting schema and type from postgres")
        schema_flights = extract_schema_and_type_from_postgres(conn_postgres, postgres_table_flights)
        logging.info("Schema flights extracted")
        schema_passengers = extract_schema_and_type_from_postgres(conn_postgres, postgres_table_passengers)
        logging.info("Schema passengers extracted")

        logging.info("Creating table in redshift")
        create_table_from_schema_in_aws_redshift(conn_redshift, postgres_table_flights, schema_flights)
        logging.info("Table flights created in redshift")
        create_table_from_schema_in_aws_redshift(conn_redshift, postgres_table_passengers, schema_passengers)
        logging.info("Table passengers created in redshift")

        logging.info("Inserting data in redshift")
        for row in data_flights:
            insert_data_redshift(conn_redshift, postgres_table_flights, schema_flights, row)
        logging.info("Data flights inserted")
        for passenger in data_flights_passengers:
            insert_data_redshift(conn_redshift, postgres_table_passengers, schema_passengers, passenger)
        logging.info("Data passengers inserted")
        logging.info("Redshift completed")

        input("Please, press Enter to start Iceberg process...")

        logging.info("Starting Iceberg process")
        provider = "glue"
        warehouse_bucket = BUCKET
        region = REGION
        catalog = load_catalog_iceberg(provider, warehouse_bucket, region)
        logging.info("Catalog loaded")

        database_name = "db1"
        table_name_flights = "table_flights"
        table_name_passengers = "table_flights_passengers"
        iceberg_table_identifier_flights = f"{database_name}.{table_name_flights}"
        iceberg_table_identifier_passengers = f"{database_name}.{table_name_passengers}"
        schema_flights = Schema(
            NestedField(field_id=1, name="id", field_type=IntegerType(), required=False),
            NestedField(field_id=2, name="flightid", field_type=StringType(), required=False),
            NestedField(field_id=3, name="platenumber", field_type=StringType(), required=False),
            NestedField(field_id=4, name="arrivaltime", field_type=StringType(), required=False),
            NestedField(field_id=5, name="departuretime", field_type=StringType(), required=False),
            NestedField(field_id=6, name="fuelconsumption", field_type=IntegerType(), required=False),
            NestedField(field_id=7, name="occupiedseats", field_type=IntegerType(), required=False),
            NestedField(field_id=8, name="origin", field_type=StringType(), required=False),
            NestedField(field_id=9, name="destination", field_type=StringType(), required=False),
            NestedField(field_id=10, name="created_at", field_type=TimestampType(), required=False)
        )
        schema_passengers= Schema(
            NestedField(field_id=1, name="id", field_type=IntegerType(), required=False),
            NestedField(field_id=2, name="flightid", field_type=StringType(), required=False),
            NestedField(field_id=3, name="passengerid", field_type=StringType(), required=False),
            NestedField(field_id=4, name="passengerstatus", field_type=StringType(), required=False)
        )
        iceberg_table_location_flights = f"{warehouse_bucket}{database_name}/{table_name_flights}"
        iceberg_table_location_passengers = f"{warehouse_bucket}{database_name}/{table_name_passengers}"
        partition_spec = PartitionSpec(spec_id=0)
        create_table_iceberg(catalog, schema_flights, iceberg_table_identifier_flights,
                                            iceberg_table_location_flights, partition_spec)
        logging.info("Table flights created")    
        create_table_iceberg(catalog, schema_passengers, iceberg_table_identifier_passengers,
                                            iceberg_table_location_passengers, partition_spec)
        logging.info("Table passengers created")

        iceberg_table_flights = catalog.load_table(iceberg_table_identifier_flights)
        iceberg_table_passengers = catalog.load_table(iceberg_table_identifier_passengers)
        insert_data_iceberg(conn_postgres, data_flights, iceberg_table_flights, postgres_table_flights)
        logging.info("Data flights inserted")
        insert_data_iceberg(conn_postgres, data_flights_passengers, iceberg_table_passengers, postgres_table_passengers)
        logging.info("Data passengers inserted")

        rows_flights = read_data_iceberg(iceberg_table_flights)
        logging.info(rows_flights)
        rows_passengers = read_data_iceberg(iceberg_table_passengers)
        logging.info(rows_passengers)
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
    main_flights()
