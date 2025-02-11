import logging
import os
import time
from utils.db_manager_utils import DbManager
from decimal import Decimal
from datetime import datetime

def convert_types(row, schema):
    formatted_row = {}
    for field, value in zip(schema, row):
        if isinstance(value, Decimal):
            formatted_value = float(value)  # Convert Decimal to float
        elif isinstance(value, datetime):
            formatted_value = value.strftime('%Y-%m-%dT%H:%M:%S')  # ISO format
        else:
            formatted_value = value  # Keep other values unchanged
        formatted_row[field.name] = formatted_value
    return formatted_row

def get_table_schema(client, dataset_id, table_name):
    """Fetches the schema of an existing BigQuery table."""
    table_id = f"{client.project}.{dataset_id}.{table_name}"
    try:
        table = client.get_table(table_id)
        logging.info(f"Fetched schema for {table_id}.")
        return table.schema
    except Exception as e:
        logging.error(f"Failed to fetch schema for {table_id}: {e}")
        return None

def sync_table(db_conn_manager, table_name):
    logging.info(f"Fetching data from OLTP for {table_name}.")
    data = db_conn_manager.get_operational_data(table_name)
    # print(data)
    if not data:
        logging.warning(f"No data found for {table_name}, skipping.")
        return
    
    client = db_conn_manager._connect_bigquery()
    schema = get_table_schema(client, "orders_bronze", table_name)
    
    if schema:
        logging.info(f"Converting data for {table_name}.")
        
        try:
            db_conn_manager.write_tables_to_analytical_db(
                data, table_name, "orders_bronze", schema, write_disposition="WRITE_TRUNCATE"
            )
            logging.info(f"Successfully wrote {len(data)} records to BigQuery table {table_name}.")
        except Exception as e:
            logging.error(f"Error during BigQuery synchronization for {table_name}: {e}")
    else:
        logging.error(f"Skipping {table_name} because schema could not be retrieved.")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
    logger = logging.getLogger()
    OLTP_DB_CONFIG = {
        "dbname": "ecommerce",
        "user": "postgres",
        "password": "EDEM2425",
        "host": os.getenv('POSTGRES_IP'),
        "port": 5432,
    }
    OLAP_DB_CONFIG = {
        "project": os.getenv('GCP_PROJECT')
    }
    logging.info("Starting synchronization.")
    db_conn_manager = DbManager(OLTP_DB_CONFIG, OLAP_DB_CONFIG)

    tables = ["customers", "orders", "order_products", "products"]

    while True:
        try:
            for table_name in tables:
                sync_table(db_conn_manager, table_name)
            
            logging.info("Synchronization completed.")
            logging.info("Waiting for 60 seconds...")
            time.sleep(60)
        except KeyboardInterrupt as _:
            logging.warning("Synchronization interrupted by user.")
            break
        except Exception as e:
            logging.error(f"Error during synchronization: {e}")
            break