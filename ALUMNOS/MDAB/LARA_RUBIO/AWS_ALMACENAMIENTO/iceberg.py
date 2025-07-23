import os
import logging
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from pyarrow import Table
from pyiceberg.schema import Schema
from pyiceberg.catalog import load_catalog
from pyiceberg.partitioning import PartitionSpec
from pyiceberg.types import (
    IntegerType, StringType, NestedField
)

# Configuración inicial
load_dotenv()
logging.basicConfig(level=logging.INFO)

# Variables de entorno
RDS_HOST = os.environ['RDS_HOST']
RDS_PORT = os.environ['RDS_PORT']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']
BUCKET = "s3://athena-edem-angel/"
REGION = "eu-north-1"
CATALOG_PROVIDER = "glue"
DB_NAME = "db1"

# Conexión a PostgreSQL
def connect_to_postgres_rds() -> psycopg2.connect:
    return psycopg2.connect(
        host=RDS_HOST,
        port=RDS_PORT,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB
    )

# Catálogo Iceberg
def get_catalog():
    return load_catalog(
        CATALOG_PROVIDER,
        type=CATALOG_PROVIDER,
        warehouse=BUCKET,
        region=REGION
    )

# Lectura desde PostgreSQL
def read_table(conn, table_name):
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM {table_name}")
        return cur.fetchall()

# Inserción en Iceberg
def insert_into_iceberg(data: dict, iceberg_table):
    df = pd.DataFrame(data)
    arrow_tbl = Table.from_pandas(df, preserve_index=False)
    with iceberg_table.transaction() as txn:
        txn.append(arrow_tbl)

# Creación de tabla en Iceberg si no existe
def create_table_if_needed(catalog, schema, table_name):
    location = f"{BUCKET}{DB_NAME}/{table_name}"
    identifier = f"{DB_NAME}.{table_name}"
    if catalog.table_exists(identifier):
        logging.info(f"Tabla '{identifier}' ya existe.")
        return
    catalog.create_table(
        identifier=identifier,
        location=location,
        schema=schema,
        partition_spec=PartitionSpec(spec_id=0)
    )
    logging.info(f"Tabla '{identifier}' creada.")

# Mapeos
def map_aviones(rows):
    return {
        "plateNumber": [r[0] for r in rows],
        "type": [r[1] for r in rows],
        "lastMaintenanceDate": [str(r[2]) if r[2] else None for r in rows],
        "nextMaintenanceDate": [str(r[3]) if r[3] else None for r in rows],
        "capacity": [r[4] for r in rows],
        "ownerId": [r[5] for r in rows],
        "ownerName": [r[6] for r in rows],
        "hangarId": [r[7] for r in rows],
        "fuel_capacity": [r[8] for r in rows],
    }

def map_vuelos(rows):
    return {
        "flightId": [r[0] for r in rows],
        "plateNumber": [r[1] for r in rows],
        "arrivalTime": [str(r[2]) if r[2] else None for r in rows],
        "departureTime": [str(r[3]) if r[3] else None for r in rows],
        "fuelConsumption": [r[4] for r in rows],
        "occupiedSeats": [r[5] for r in rows],
        "origin": [r[6] for r in rows],
        "destination": [r[7] for r in rows],
    }

def map_pasajeros(rows):
    return {
        "passengerId": [r[0] for r in rows],
        "name": [r[1] for r in rows],
        "nationalId": [r[2] for r in rows],
        "dateOfBirth": [str(r[3]) if r[3] else None for r in rows],
    }

# Esquemas
SCHEMAS = {
    "aviones": Schema(
        NestedField(1, "plateNumber", StringType()),
        NestedField(2, "type", StringType()),
        NestedField(3, "lastMaintenanceDate", StringType()),
        NestedField(4, "nextMaintenanceDate", StringType()),
        NestedField(5, "capacity", IntegerType()),
        NestedField(6, "ownerId", StringType()),
        NestedField(7, "ownerName", StringType()),
        NestedField(8, "hangarId", StringType()),
        NestedField(9, "fuel_capacity", IntegerType())
    ),
    "vuelos": Schema(
        NestedField(1, "flightId", StringType()),
        NestedField(2, "plateNumber", StringType()),
        NestedField(3, "arrivalTime", StringType()),
        NestedField(4, "departureTime", StringType()),
        NestedField(5, "fuelConsumption", IntegerType()),
        NestedField(6, "occupiedSeats", IntegerType()),
        NestedField(7, "origin", StringType()),
        NestedField(8, "destination", StringType())
    ),
    "pasajeros": Schema(
        NestedField(1, "passengerId", StringType()),
        NestedField(2, "name", StringType()),
        NestedField(3, "nationalId", StringType()),
        NestedField(4, "dateOfBirth", StringType())
    )
}

MAPPERS = {
    "aviones": map_aviones,
    "vuelos": map_vuelos,
    "pasajeros": map_pasajeros
}

def run():
    conn = None
    try:
        conn = connect_to_postgres_rds()
        catalog = get_catalog()
        for table_name in ["aviones", "vuelos", "pasajeros"]:
            logging.info(f"Procesando tabla '{table_name}'...")
            rows = read_table(conn, table_name)
            data = MAPPERS[table_name](rows)
            schema = SCHEMAS[table_name]
            create_table_if_needed(catalog, schema, table_name)
            iceberg_table = catalog.load_table(f"{DB_NAME}.{table_name}")
            insert_into_iceberg(data, iceberg_table)
            logging.info(f"Datos insertados en Iceberg ({table_name})")
    except Exception as e:
        logging.error(f"Error en el proceso: {e}")
    finally:
        if conn:
            conn.close()
        logging.info("Proceso completado.")
if __name__ == "__main__":
    run()
