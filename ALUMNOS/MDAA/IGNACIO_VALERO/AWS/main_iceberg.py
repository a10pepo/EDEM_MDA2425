import boto3
import pyarrow as pa
from pyiceberg.catalog import load_catalog
from pyiceberg.schema import Schema, NestedField
from pyiceberg.types import StringType, LongType
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_database_if_not_exists(glue_client, database_name):
    try:
        glue_client.get_database(Name=database_name)
        logger.info(f"Database '{database_name}' already exists.")
    except glue_client.exceptions.EntityNotFoundException:
        glue_client.create_database(DatabaseInput={"Name": database_name})
        logger.info(f"Database '{database_name}' created.")

def create_table_if_not_exists(catalog, table_id, schema, location):
    if table_id not in catalog.list_tables():
        catalog.create_table(
            table_identifier=table_id,
            schema=schema,
            location=location,
            properties={"format-version": "2"},
        )
        logger.info(f"Table '{table_id}' created at '{location}'.")
    else:
        logger.info(f"Table '{table_id}' already exists.")

def insert_data(table, data):
    arrow_table = pa.Table.from_pylist(data)
    with table.new_transaction() as txn:
        txn.append(arrow_table)
        txn.commit()
    logger.info(f"Inserted {len(data)} records into table '{table.identifier}'.")

def main():
    database = "db1"
    warehouse_bucket = "s3://icebergg/"
    region = "us-east-1"
    
    airplanes_schema = Schema(
        NestedField(1, "plateNumber", StringType(), required=True),
        NestedField(2, "type", StringType(), required=False),
        NestedField(3, "lastMaintenanceDate", StringType(), required=False),
        NestedField(4, "nextMaintenanceDate", StringType(), required=False),
        NestedField(5, "capacity", LongType(), required=False),
        NestedField(6, "ownerId", StringType(), required=False),
        NestedField(7, "ownerName", StringType(), required=False),
        NestedField(8, "hangarId", StringType(), required=False),
        NestedField(9, "fuel_capacity", LongType(), required=False),
    )

    airplanes_table_id = f"{database}.airplanes"
    airplanes_location = f"{warehouse_bucket}{database}/airplanes"

    glue_client = boto3.client("glue", region_name=region)
    create_database_if_not_exists(glue_client, database)

    catalog_conf = {
        "catalog-name": "glue_catalog",
        "region": region,
    }
    catalog = load_catalog("glue", catalog_conf)

    create_table_if_not_exists(catalog, airplanes_table_id, airplanes_schema, airplanes_location)

    airplanes_data = [
        {
            "plateNumber": "ABC123",
            "type": "Jet",
            "lastMaintenanceDate": "2024-10-01",
            "nextMaintenanceDate": "2025-04-01",
            "capacity": 180,
            "ownerId": "owner_1",
            "ownerName": "Owner One",
            "hangarId": "hangar_9",
            "fuel_capacity": 5000,
        },
    ]

    airplanes_table = catalog.load_table(airplanes_table_id)
    insert_data(airplanes_table, airplanes_data)

if __name__ == "__main__":
    main()
