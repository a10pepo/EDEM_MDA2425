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
    DateType,
    LongType
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


def read_data_iceberg(table: Table) -> pd.DataFrame:
    rows = table.scan().to_arrow().to_pandas()
    return rows


if __name__ == "__main__":
    provider = "glue"
    warehouse_bucket = "s3://alboce-edem-e2e/"
    region = "eu-north-1"
    catalog = load_catalog_iceberg(provider, warehouse_bucket, region)
    logging.info("Catalog loaded")

    database_name = "db_e2e"
    partition_spec = PartitionSpec(spec_id=0)

    # Definición de las tablas (schema y data de ejemplo)
    table_definitions = {
        "airplanes": {
            "schema": Schema(
                NestedField(field_id=1, name="plateNumber", field_type=StringType(), required=False),
                NestedField(field_id=2, name="type", field_type=StringType()),
                NestedField(field_id=3, name="lastMaintenanceDate", field_type=DateType()),
                NestedField(field_id=4, name="nextMaintenanceDate", field_type=DateType()),
                NestedField(field_id=5, name="capacity", field_type=LongType()),
                NestedField(field_id=6, name="ownerId", field_type=StringType()),
                NestedField(field_id=7, name="ownerName", field_type=StringType()),
                NestedField(field_id=8, name="hangarId", field_type=StringType()),
                NestedField(field_id=9, name="fuel_capacity", field_type=LongType()),
            ),
            "data": {
                # Los strings se pasan como lista normal.
                "plateNumber": ["EC-XYZ1", "EC-ABC2"],
                "type": ["Cessna 208 Caravan", "Piper PA-31 Navajo"],
                # Convertir a objeto date para que coincida con DateType.
                "lastMaintenanceDate": [pd.Timestamp("2024-04-15").date(), pd.Timestamp("2025-02-10").date()],
                "nextMaintenanceDate": [pd.Timestamp("2025-04-15").date(), pd.Timestamp("2027-02-10").date()],
                # Usar enteros de 64 bits.
                "capacity": pd.Series([9, 7], dtype="int64"),
                "ownerId": ["O-12345", "O-23456"],
                "ownerName": ["Madrid Flying Club", "Catalina Aviation"],
                "hangarId": ["H-01", "H-01"],
                "fuel_capacity": pd.Series([700, 1000], dtype="int64"),
            }
        },
        "flights": {
            "schema": Schema(
                NestedField(field_id=1, name="flightId", field_type=StringType(), required=False),
                NestedField(field_id=2, name="plateNumber", field_type=StringType()),
                NestedField(field_id=3, name="arrivalTime", field_type=TimestampType()),
                NestedField(field_id=4, name="departureTime", field_type=TimestampType()),
                NestedField(field_id=5, name="fuelConsumption", field_type=IntegerType()),
                NestedField(field_id=6, name="occupiedSeats", field_type=IntegerType()),
                NestedField(field_id=7, name="origin", field_type=StringType()),
                NestedField(field_id=8, name="destination", field_type=StringType()),
            ),
            "data": {
                "flightId": ["FL-2025-001", "FL-2025-002"],
                "plateNumber": ["EC-XYZ1", "EC-ABC2"],
                # Para timestamp se puede usar np.array con dtype "datetime64[us]"
                "arrivalTime": np.array(["2025-03-01T09:30:00", "2025-03-02T11:15:00"], dtype="datetime64[us]"),
                "departureTime": np.array(["2025-03-01T14:45:00", "2025-03-02T16:30:00"], dtype="datetime64[us]"),
                "fuelConsumption": pd.Series([350, 850], dtype="int32"),
                "occupiedSeats": pd.Series([7, 8], dtype="int32"),
                "origin": ["Valencia", "Barcelona"],
                "destination": ["Paris", "London"],
            }
        },
        "flight_passengers": {
            "schema": Schema(
                NestedField(field_id=1, name="flightId", field_type=StringType(), required=False),
                NestedField(field_id=2, name="passengerId", field_type=StringType(), required=False),
                NestedField(field_id=3, name="status", field_type=StringType()),
            ),
            "data": {
                "flightId": ["FL-2025-001"] * 6 + ["FL-2025-002"] * 8,
                "passengerId": ["P-1001", "P-1002", "P-1003", "P-1004", "P-1005", "P-1006",
                                "P-1010", "P-1011", "P-1012", "P-1013", "P-1014", "P-1015", "P-1016", "P-1017"],
                "status": ["Boarded"] * 6 + ["Boarded", "Boarded", "Cancelled", "Boarded", "Boarded", "Boarded", "Boarded", "Cancelled"],
            }
        },
        "passengers": {
            "schema": Schema(
                NestedField(field_id=1, name="passengerId", field_type=StringType(), required=False),
                NestedField(field_id=2, name="name", field_type=StringType()),
                NestedField(field_id=3, name="nationalId", field_type=StringType()),
                NestedField(field_id=4, name="dateOfBirth", field_type=DateType()),
            ),
            "data": {
                "passengerId": [
                    "P-1001", "P-1002", "P-1003", "P-1004", "P-1005", "P-1006", "P-1007",
                    "P-1008", "P-1009", "P-1010", "P-1011", "P-1012", "P-1013", "P-1014",
                    "P-1015", "P-1016", "P-1017", "P-1018", "P-1019", "P-1020"
                ],
                "name": [
                    "Ana García Martínez", "Carlos Rodríguez López", "Elena Sánchez García",
                    "Javier Martínez Pérez", "María López Rodríguez", "Pedro García Sánchez",
                    "Sara Pérez Martínez", "Juan Sánchez López", "Lucía Martínez García",
                    "Antonio García López", "Beatriz López Sánchez", "Carmen Martínez Rodríguez",
                    "David Sánchez Martínez", "Elena García López", "Fernando López Martínez",
                    "Gloria Martínez Sánchez", "Hugo Sánchez García", "Isabel García López",
                    "Javier López Martínez", "Karla Martínez García"
                ],
                "nationalId": [
                    "12345678A", "87654321B", "11223344C", "44332211D", "33441122E", "22114433F",
                    "55443322G", "66554433H", "77665544I", "88776655J", "99887766K", "11001122L",
                    "22110033M", "33221100N", "44332211O", "55443322P", "66554433Q", "77665544R",
                    "88776655S", "99887766T"
                ],
                # Convertir a lista de objetos date para que coincida con DateType.
                "dateOfBirth": [pd.Timestamp(date).date() for date in [
                    "1991-05-15", "1973-11-30", "1988-03-25", "1995-07-10",
                    "1985-09-05", "1979-01-20", "1999-12-15", "1977-08-25",
                    "1990-02-10", "1980-06-05", "1983-04-30", "1975-10-15",
                    "1987-03-20", "1978-07-25", "1982-01-10", "1984-09-05",
                    "1986-02-20", "1976-12-15", "1981-08-25", "1989-02-10"
                ]]
            }
        }
    }

    for table_name, config in table_definitions.items():
        iceberg_table_identifier = f"{database_name}.{table_name}"
        iceberg_table_location = f"{warehouse_bucket}{database_name}/{table_name}"
        schema = config["schema"]

        create_table_iceberg(catalog, schema, iceberg_table_identifier, iceberg_table_location, partition_spec)

        data = config["data"]
        iceberg_table = catalog.load_table(iceberg_table_identifier)
        insert_data_iceberg(data, iceberg_table)
        logging.info(f"Data inserted for table {iceberg_table_identifier}")

        rows = read_data_iceberg(iceberg_table)
        logging.info(f"Data in table {iceberg_table_identifier}:\n{rows}")
