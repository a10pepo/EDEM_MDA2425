import logging

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
    TimestampType,
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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


def insert_data_iceberg(data: dict,
                        iceberg_table: Table) -> None:
    df = pd.DataFrame(data)
    arrow_table = Table.from_pandas(df)
    with iceberg_table.transaction() as txn:
        txn.append(arrow_table)


def process_table(catalog, db_name, table_name, schema, data):
    identifier = f"{db_name}.{table_name}"
    location = f"{warehouse_bucket.rstrip('/')}/{db_name}/{table_name}"
    create_table_iceberg(catalog, schema, identifier, location, PartitionSpec(spec_id=0))
    logging.info(f"Table '{table_name}' created")
    iceberg_table = catalog.load_table(identifier)
    insert_data_iceberg(data, iceberg_table)
    logging.info(f"Data inserted into '{table_name}'")


provider = "glue"
warehouse_bucket = "s3://jacinto-iceberg/"
region = "eu-north-1"
database_name = "jacinto-glue"

catalog = load_catalog_iceberg(provider, warehouse_bucket, region)

# Airplanes
schema_airplanes = Schema(
    NestedField(1, "plate_number", StringType()),
    NestedField(2, "type", StringType()),
    NestedField(3, "last_maintenance_date", TimestampType()),
    NestedField(4, "next_maintenance_date", TimestampType()),
    NestedField(5, "capacity", IntegerType()),
    NestedField(6, "owner_id", StringType()),
    NestedField(7, "owner_name", StringType()),
    NestedField(8, "hangar_id", StringType()),
    NestedField(9, "fuel_capacity", IntegerType()),
)
data_airplanes = {
    "plate_number": ["ABC123", "DEF456"],
    "type": ["Jet", "Turbo"],
    "last_maintenance_date": np.array(["2023-10-01", "2023-11-01"], dtype="datetime64[us]"),
    "next_maintenance_date": np.array(["2024-04-01", "2024-05-01"], dtype="datetime64[us]"),
    "capacity": pd.Series([150, 120], dtype="Int32"),
    "owner_id": ["OWN01", "OWN02"],
    "owner_name": ["Jacinto", "Carla"],
    "hangar_id": ["H1", "H2"],
    "fuel_capacity": pd.Series([20000, 15000], dtype="Int32"),
}
process_table(catalog, database_name, "table_airplanes", schema_airplanes, data_airplanes)

# Flights
schema_flights = Schema(
    NestedField(1, "flight_id", StringType()),
    NestedField(2, "origin", StringType()),
    NestedField(3, "destination", StringType()),
    NestedField(4, "departure_time", TimestampType()),
    NestedField(5, "arrival_time", TimestampType()),
)
data_flights = {
    "flight_id": ["FL001", "FL002"],
    "origin": ["MAD", "BCN"],
    "destination": ["LIS", "LON"],
    "departure_time": np.array(["2024-07-01 10:00:00", "2024-07-02 15:00:00"], dtype="datetime64[us]"),
    "arrival_time": np.array(["2024-07-01 11:30:00", "2024-07-02 17:30:00"], dtype="datetime64[us]"),
}
process_table(catalog, database_name, "table_flights", schema_flights, data_flights)

# Flight_passengers
schema_flight_passengers = Schema(
    NestedField(1, "flight_id", StringType()),
    NestedField(2, "passenger_id", StringType()),
    NestedField(3, "seat_number", StringType()),
)
data_flight_passengers = {
    "flight_id": ["FL001", "FL001", "FL002"],
    "passenger_id": ["P1", "P2", "P3"],
    "seat_number": ["1A", "2B", "3C"],
}
process_table(catalog, database_name, "table_flights_passengers", schema_flight_passengers, data_flight_passengers)

# Passengers_info
schema_passengers_info = Schema(
    NestedField(1, "passenger_id", StringType()),
    NestedField(2, "name", StringType()),
    NestedField(3, "birthdate", TimestampType()),
)
data_passengers_info = {
    "passenger_id": ["P1", "P2", "P3"],
    "name": ["Ana", "Luis", "Carmen"],
    "birthdate": np.array(["1990-01-01", "1985-05-10", "2000-07-20"], dtype="datetime64[us]"),
}
process_table(catalog, database_name, "table_passengers_info", schema_passengers_info, data_passengers_info)

logging.info("Tablas creadas e insertadas correctamente.")