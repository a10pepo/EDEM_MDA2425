import logging
import os
import psycopg2
from dotenv import load_dotenv
import numpy as np
import pandas as pd
import pyarrow as pa
from pyarrow import Table
from pyiceberg.catalog import Catalog, load_catalog
from pyiceberg.partitioning import PartitionSpec
from pyiceberg.schema import Schema
from pyiceberg.types import (
    IntegerType,
    NestedField,
    StringType,
    TimestampType,
    DateType
)
import boto3

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()


def extract_data_from_postgres(conn: psycopg2.connect, table_name: str) -> None:
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name};")
    data = cur.fetchall()
    return data


def set_aws_region(region: str):
    os.environ["AWS_REGION"] = region
    os.environ["AWS_DEFAULT_REGION"] = region  
    logging.info(f"AWS region set to {region}")


def load_catalog_iceberg(provider: str, warehouse_bucket: str, region: str) -> Catalog:
    set_aws_region(region)

    session = boto3.session.Session()
    s3_client = boto3.client("s3", region_name=region)

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


def map_postgres_type_to_arrow(pg_type: str) -> pa.DataType:
    type_mapping = {
        "integer": pa.int32(),
        "bigint": pa.int64(),
        "smallint": pa.int16(),
        "real": pa.float32(),
        "double precision": pa.float64(),
        "numeric": pa.float64(),
        "boolean": pa.bool_(),
        "text": pa.string(),
        "varchar": pa.string(),
        "timestamp without time zone": pa.timestamp("s"),
        "timestamp with time zone": pa.timestamp("s", tz="UTC"),
        "date": pa.date32()
    }
    return type_mapping.get(pg_type, pa.string()) 


def insert_data_iceberg(conn: psycopg2.connect, data: tuple, iceberg_table: Table, table_name: str) -> None:
    cur = conn.cursor()
    cur.execute(f"""SELECT column_name, data_type
                    FROM information_schema.columns 
                    WHERE table_name = '{table_name}'
                    ORDER BY ordinal_position;""")  # Ensure correct column order
    schema_info = cur.fetchall()

    arrow_schema = pa.schema([
        pa.field(col, map_postgres_type_to_arrow(pg_type))
        for col, pg_type in schema_info
    ])

    df = pd.DataFrame(list(data), columns=[col for col, _ in schema_info])

    if "created_at" in df.columns:
        df["created_at"] = df["created_at"].astype("datetime64[s]")  

    arrow_table = Table.from_pandas(df, schema=arrow_schema)

    with iceberg_table.transaction() as txn:
        txn.append(arrow_table)



def read_data_iceberg(table: Table) -> pd.DataFrame:
    rows = table.scan().to_arrow().to_pandas()
    return rows
