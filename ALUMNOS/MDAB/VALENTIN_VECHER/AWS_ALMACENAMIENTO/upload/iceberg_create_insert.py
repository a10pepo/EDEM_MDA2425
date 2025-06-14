import logging

import numpy as np
import pandas as pd
from pyarrow import Table
from pyiceberg.catalog import Catalog, load_catalog
from pyiceberg.partitioning import PartitionSpec
from pyiceberg.schema import Schema
from pyiceberg.types import (
    TimestampType,
    IntegerType,
    NestedField,
    StringType,
    DateType,
    DateType,
    MapType
)


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def schema_iceberg(table):
    if table == "airplanes":
        return Schema(
    NestedField(field_id=1, name="plateNumber",        field_type=StringType(),  required=False),
    NestedField(field_id=2, name="type",               field_type=StringType(),  required=False),
    NestedField(field_id=3, name="lastMaintenanceDate",field_type=TimestampType(),    required=False),
    NestedField(field_id=4, name="nextMaintenanceDate",field_type=TimestampType(),    required=False),
    NestedField(field_id=5, name="capacity",           field_type=IntegerType(), required=False),
    NestedField(field_id=6, name="ownerId",            field_type=StringType(),  required=False),
    NestedField(field_id=7, name="ownerName",          field_type=StringType(),  required=False),
    NestedField(field_id=8, name="hangarId",           field_type=StringType(),  required=False),
    NestedField(field_id=9, name="fuel_capacity",      field_type=IntegerType(), required=False)
)

    elif table == "flights":
        return Schema(
    NestedField(field_id=1, name="flightId",        field_type=StringType(),                    required=False),
    NestedField(field_id=2, name="plateNumber",     field_type=StringType(),                    required=False),
    NestedField(field_id=3, name="arrivalTime",     field_type=TimestampType(),                 required=False),
    NestedField(field_id=4, name="departureTime",   field_type=TimestampType(),                 required=False),
    NestedField(field_id=5, name="fuelConsumption", field_type=IntegerType(),                   required=False),
    NestedField(field_id=6, name="occupiedSeats",   field_type=IntegerType(),                   required=False),
    NestedField(field_id=7, name="origin",          field_type=StringType(),                    required=False),
    NestedField(field_id=8, name="destination",     field_type=StringType(),                    required=False),
)

    elif table == "passengers":
        return Schema(
    NestedField(field_id=1, name="passengerId",  field_type=StringType(), required=False),
    NestedField(field_id=2, name="name",         field_type=StringType(), required=False),
    NestedField(field_id=3, name="nationalId",   field_type=StringType(), required=False),
    NestedField(field_id=4, name="dateOfBirth",  field_type=TimestampType(),   required=False)
)
        
    elif table== "flight_passengers":
        return Schema(
    NestedField(field_id=1, name="flightId", field_type=StringType(), required=False),
    NestedField(field_id=2, name="passengerId", field_type=StringType(), required=False),
    NestedField(field_id=3, name="status", field_type=StringType()),
)

    else:
        raise ValueError(f"Unknown table: {table}")
    
def insert_table_data(table):
    if table == "airplanes":
        return {
    "plateNumber":        pd.Series(["EC-XYZ1"],            dtype="string"),
    "type":               pd.Series(["Cessna 208 Caravan"], dtype="string"),
    "lastMaintenanceDate": np.array(["2024-04-15"], dtype="datetime64[D]"),
    "nextMaintenanceDate": np.array(["2025-04-15"], dtype="datetime64[D]"),
    "capacity":           pd.Series([9],                    dtype="Int32"),
    "ownerId":            pd.Series(["O-12345"],            dtype="string"),
    "ownerName":          pd.Series(["Madrid Flying Club"], dtype="string"),
    "hangarId":           pd.Series(["H-01"],               dtype="string"),
    "fuel_capacity":      pd.Series([700],                  dtype="Int32"),
        }
    elif table == "flights":
        return {
    "flightId":        pd.Series(["FL-2025-001"], dtype="string"),
    "plateNumber":     pd.Series(["EC-XYZ1"],     dtype="string"),
    "arrivalTime":     np.array(["2025-03-01"], dtype="datetime64[D]"),
    "departureTime":   np.array(["2025-03-01"], dtype="datetime64[D]"),
    "fuelConsumption": pd.Series([350],           dtype="Int32"),
    "occupiedSeats":   pd.Series([7],             dtype="Int32"),
    "origin":          pd.Series(["Valencia"],    dtype="string"),
    "destination":     pd.Series(["Paris"],       dtype="string"),
}
    elif table == "passengers":
        return {
    "passengerId": pd.Series(["P-1001"],              dtype="string"),
    "name":        pd.Series(["Ana García Martínez"], dtype="string"),
    "nationalId":  pd.Series(["12345678A"],           dtype="string"),
    "dateOfBirth": np.array(["1991-05-15"], dtype="datetime64[D]"),
}
    elif table == "flight_passengers":
        return {
    "flightId": ["FL-2025-001"] * 6 + ["FL-2025-002"] * 8,
    "passengerId": ["P-1001", "P-1002", "P-1003", "P-1004", "P-1005", "P-1006",
                                "P-1010", "P-1011", "P-1012", "P-1013", "P-1014", "P-1015", "P-1016", "P-1017"],
    "status": ["Boarded"] * 6 + ["Boarded", "Boarded", "Cancelled", "Boarded", "Boarded", "Boarded", "Boarded", "Cancelled"]
}
    
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


def read_data_iceberg(table: Table) -> pd.DataFrame:
    rows = table.scan().to_arrow().to_pandas()
    return rows


if __name__ == "__main__":
    provider = "glue"
    warehouse_bucket = "s3://vavego-edem-e2e/"
    region = "eu-north-1"
    catalog = load_catalog_iceberg(provider, warehouse_bucket, region)
    logging.info("Catalog loaded")

    database_name = "db1"
    tables = ["airplanes", "passengers", "flights", "flight_passengers"]
    for table in tables:
        table_name = table
        iceberg_table_identifier = f"{database_name}.{table_name}"
        schema = schema_iceberg(table)
        
        partition_spec = PartitionSpec(spec_id=0)
        iceberg_table_location = f"{warehouse_bucket}{database_name}/{table}"
        create_table_iceberg(catalog, schema, iceberg_table_identifier,
                                         iceberg_table_location, partition_spec)
        logging.info("Table created")
        
        data = insert_table_data(table)
    
        iceberg_table = catalog.load_table(iceberg_table_identifier)
        insert_data_iceberg(data, iceberg_table)
        logging.info("Data inserted")

        rows = read_data_iceberg(iceberg_table)
        logging.info(rows)
