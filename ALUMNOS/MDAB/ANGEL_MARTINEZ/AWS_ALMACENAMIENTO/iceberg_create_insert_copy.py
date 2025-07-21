import logging
import os
from dotenv import load_dotenv

import numpy as np
import pandas as pd
from pyarrow import Table
from pyiceberg.catalog import Catalog, load_catalog
from pyiceberg.partitioning import PartitionSpec
from pyiceberg.schema import Schema
from pyiceberg.types import (
    IntegerType,
    NestedField,
    StringType,
    ListType,
    StructType
)
field_type = ListType(element_type=StringType(), element_id=1)

import psycopg2
load_dotenv()

bucket = "s3://athena-edem-angel/"

RDS_HOST = os.environ['RDS_HOST']
RDS_PORT = os.environ['RDS_PORT']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']

def connect_to_postgres_rds() -> psycopg2.connect:
    conn = psycopg2.connect(
        host=RDS_HOST,
        port=RDS_PORT,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB
    )
    return conn

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

aviones_iceberg = Schema(
    NestedField(field_id=1, name="plateNumber", field_type=StringType(), required=False),
    NestedField(field_id=2, name="type", field_type=StringType(), required=False),
    NestedField(field_id=3, name="lastMaintenanceDate", field_type=StringType(), required=False),
    NestedField(field_id=4, name="nextMaintenanceDate", field_type=StringType(), required=False),
    NestedField(field_id=5, name="capacity", field_type=IntegerType(), required=False),
    NestedField(field_id=6, name="ownerId", field_type=StringType(), required=False),
    NestedField(field_id=7, name="ownerName", field_type=StringType(), required=False),
    NestedField(field_id=8, name="hangarId", field_type=StringType(), required=False),
    NestedField(field_id=9, name="fuel_capacity", field_type=IntegerType(), required=False),
)

vuelos_iceberg = Schema(
    NestedField(field_id=1, name="flightId", field_type=StringType(), required=False),
    NestedField(field_id=2, name="plateNumber", field_type=StringType(), required=False),
    NestedField(field_id=3, name="arrivalTime", field_type=StringType(), required=False),
    NestedField(field_id=4, name="departureTime", field_type=StringType(), required=False),
    NestedField(field_id=5, name="fuelConsumption", field_type=IntegerType(), required=False),
    NestedField(field_id=6, name="occupiedSeats", field_type=IntegerType(), required=False),
    NestedField(field_id=7, name="origin", field_type=StringType(), required=False),
    NestedField(field_id=8, name="destination", field_type=StringType(), required=False),
)


pasajeros_iceberg = Schema(
    NestedField(field_id=1, name="passengerId", field_type=StringType(), required=False),
    NestedField(field_id=2, name="name", field_type=StringType(), required=False),
    NestedField(field_id=3, name="nationalId", field_type=StringType(), required=False),
    NestedField(field_id=4, name="dateOfBirth", field_type=(), required=False),
)

def load_catalog_iceberg(provider: str, warehouse_bucket: str, region: str) -> Catalog:
    return load_catalog(
        provider,
        **{
            "type": provider,
            "warehouse": warehouse_bucket,
            "region": region,
        }
    )

def create_table_iceberg(catalog: Catalog, schema: dict, table_name: str,
                         table_location: str, partition_spec: str) -> None:
    if catalog.table_exists(table_name):
        logging.info(f"Table '{table_name}' already exists!")
        return None
    catalog.create_table(
        identifier=table_name,
        location=table_location,
        schema=schema,
        partition_spec=partition_spec,
    )

def read_data_iceberg(table: Table) -> pd.DataFrame:
    rows = table.scan().to_arrow().to_pandas()
    return rows

def extract_data_from_postgres(conn: psycopg2.connect, table_name: str) -> None:
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name};")
    data = cur.fetchall()
    return data

def map_postgres_to_aviones(data_rows):
    data = {
        "plateNumber": pd.Series(dtype="string"),
        "type": pd.Series(dtype="string"),
        "lastMaintenanceDate": pd.Series(dtype="datetime64[us]"),
        "nextMaintenanceDate": pd.Series(dtype="datetime64[us]"),
        "capacity": pd.Series(dtype="Int32"),
        "ownerId": pd.Series(dtype="string"),
        "ownerName": pd.Series(dtype="string"),
        "hangarId": pd.Series(dtype="string"),
        "fuel_capacity": pd.Series(dtype="Int32"),
    }
    for row in data_rows:
        data["plateNumber"] = pd.concat([data["plateNumber"], pd.Series([row[0]], dtype="string")], ignore_index=True)
        data["type"] = pd.concat([data["type"], pd.Series([row[1]], dtype="string")], ignore_index=True)
        data["lastMaintenanceDate"] = pd.concat([data["lastMaintenanceDate"], pd.Series([row[2]], dtype="string") if row[2] else pd.Series([pd.NaT], dtype="string")], ignore_index=True)
        data["nextMaintenanceDate"] = pd.concat([data["nextMaintenanceDate"], pd.Series([row[3]], dtype="string") if row[3] else pd.Series([pd.NaT], dtype="string")], ignore_index=True)
        data["capacity"] = pd.concat([data["capacity"], pd.Series([row[4]], dtype="Int32")], ignore_index=True)
        data["ownerId"] = pd.concat([data["ownerId"], pd.Series([row[5]], dtype="string")], ignore_index=True)
        data["ownerName"] = pd.concat([data["ownerName"], pd.Series([row[6]], dtype="string")], ignore_index=True)
        data["hangarId"] = pd.concat([data["hangarId"], pd.Series([row[7]], dtype="string")], ignore_index=True)
        data["fuel_capacity"] = pd.concat([data["fuel_capacity"], pd.Series([row[8]], dtype="Int32")], ignore_index=True)
    return data

def map_postgres_to_pasajeros(data_rows):
    data = {
        "passengerId": pd.Series(dtype="string"),
        "name": pd.Series(dtype="string"),
        "nationalId": pd.Series(dtype="string"),
        "dateOfBirth": pd.Series(dtype="datetime64[us]"),
    }
    for row in data_rows:
        data["passengerId"] = pd.concat([data["passengerId"], pd.Series([row[0]], dtype="string")], ignore_index=True)
        data["name"] = pd.concat([data["name"], pd.Series([row[1]], dtype="string")], ignore_index=True)
        data["nationalId"] = pd.concat([data["nationalId"], pd.Series([row[2]], dtype="string")], ignore_index=True)
        data["dateOfBirth"] = pd.concat([data["dateOfBirth"], pd.Series([row[3]], dtype="datetime64[us]") if row[3] else pd.Series([pd.NaT], dtype="datetime64[us]")], ignore_index=True)
    return data

def map_postgres_to_vuelos(data_rows):
    data = {
        "flightId": pd.Series(dtype="string"),
        "plateNumber": pd.Series(dtype="string"),
        "arrivalTime": pd.Series(dtype="string"),
        "departureTime": pd.Series(dtype="string"),
        "fuelConsumption": pd.Series(dtype="Int32"),
        "occupiedSeats": pd.Series(dtype="Int32"),
        "origin": pd.Series(dtype="string"),
        "destination": pd.Series(dtype="string"),  
    }
    for row in data_rows:
        data["flightId"] = pd.concat([data["flightId"], pd.Series([row[0]], dtype="string")], ignore_index=True)
        data["plateNumber"] = pd.concat([data["plateNumber"], pd.Series([row[1]], dtype="string")], ignore_index=True)
        data["arrivalTime"] = pd.concat([data["arrivalTime"], pd.Series([row[2]], dtype="string") if row[2] else pd.Series([pd.NaT], dtype="string")], ignore_index=True)
        data["departureTime"] = pd.concat([data["departureTime"], pd.Series([row[3]], dtype="string") if row[3] else pd.Series([pd.NaT], dtype="string")], ignore_index=True)
        data["fuelConsumption"] = pd.concat([data["fuelConsumption"], pd.Series([row[4]], dtype="Int32")], ignore_index=True)
        data["occupiedSeats"] = pd.concat([data["occupiedSeats"], pd.Series([row[5]], dtype="Int32")], ignore_index=True)
        data["origin"] = pd.concat([data["origin"], pd.Series([row[6]], dtype="string")], ignore_index=True)
        data["destination"] = pd.concat([data["destination"], pd.Series([row[7]], dtype="string")], ignore_index=True)
    return data

def insert_data_iceberg(data: dict,
                        iceberg_table: Table) -> None:
    df = pd.DataFrame(data)
    arrow_table = Table.from_pandas(df, preserve_index=False)
    with iceberg_table.transaction() as txn:
        txn.append(arrow_table)


if __name__ == "__main__":
    conn_postgres = connect_to_postgres_rds()
    logging.info("Connected to RDS")
    postgres_tables = ['aviones', 'pasajeros', 'vuelos']
    logging.info("Connected to RDS")
    logging.info(f"Extracting data from postgres table {postgres_tables}")
    for postgres_table in postgres_tables:
        logging.info(f"Extracting data from postgres table {postgres_table}")
        data_rows = extract_data_from_postgres(conn_postgres, postgres_table)
        print(data_rows)
        logging.info("Data extracted")
    provider = "glue"
    warehouse_bucket = bucket
    region = "eu-north-1"
    catalog = load_catalog_iceberg(provider, warehouse_bucket, region)
    logging.info("Catalog loaded")
    database_name = "db1"
    tables_info = [
        {
            "postgres_table": "aviones",
            "iceberg_schema": aviones_iceberg,
            "iceberg_table_name": "aviones",
            "map_function": map_postgres_to_aviones
        },
        {
            "postgres_table": "vuelos",
            "iceberg_schema": vuelos_iceberg,
            "iceberg_table_name": "vuelos",
            "map_function": map_postgres_to_vuelos
        },
        {
            "postgres_table": "pasajeros",
            "iceberg_schema": pasajeros_iceberg,
            "iceberg_table_name": "pasajeros",
            "map_function": map_postgres_to_pasajeros  
        }
    ]
    for table_info in tables_info:
        postgres_table = table_info["postgres_table"]
        iceberg_schema = table_info["iceberg_schema"]
        iceberg_table_name = table_info["iceberg_table_name"]
        map_function = table_info["map_function"]
        
        logging.info(f"Extracting data from postgres table {postgres_table}")
        data_rows = extract_data_from_postgres(conn_postgres, postgres_table)
        mapped_data = map_function(data_rows)
        
        iceberg_table_identifier = f"{database_name}.{iceberg_table_name}"
        partition_spec = PartitionSpec(spec_id=0)
        iceberg_table_location = f"{warehouse_bucket}{database_name}/{iceberg_table_name}"
        
        create_table_iceberg(catalog, iceberg_schema, iceberg_table_identifier, iceberg_table_location, partition_spec)
        logging.info(f"Table '{iceberg_table_name}' created")
        
        iceberg_table = catalog.load_table(iceberg_table_identifier)
        insert_data_iceberg(mapped_data, iceberg_table)
        logging.info(f"Data inserted into Iceberg table '{iceberg_table_name}'")
