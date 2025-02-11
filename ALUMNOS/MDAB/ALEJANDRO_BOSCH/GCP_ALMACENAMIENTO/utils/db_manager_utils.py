import logging
import decimal
import datetime


import psycopg2
from google.cloud import bigquery

class DbManager:
    def __init__(self, OLTP_DB_CONFIG, OLAP_DB_CONFIG):
        self.OLTP_DB_CONFIG = OLTP_DB_CONFIG
        self.OLAP_DB_CONFIG = OLAP_DB_CONFIG
        self.conn_oltp = None
        self.conn_olap = None

    def _connect_postgres(self):
        try:
            self.conn_oltp = psycopg2.connect(**self.OLTP_DB_CONFIG)
            logging.info("Connected to PostgreSQL successfully.")
            return self.conn_oltp.cursor()
        except Exception as e:
            logging.error(f"Failed to connect to PostgreSQL: {e}")
            raise

    def _connect_bigquery(self):
        try:
            self.client_olap = bigquery.Client(**self.OLAP_DB_CONFIG)
            logging.info("Connected to BigQuery successfully.")
            return self.client_olap
        except Exception as e:
            logging.error(f"Failed to connect to BigQuery: {e}")
            raise
    
    @staticmethod
    def convert_value(value):
        """Convert values to JSON serializable formats."""
        if isinstance(value, decimal.Decimal):
            return float(value)  
        elif isinstance(value, datetime.datetime):
            return value.isoformat()  
        return value 
    
    def get_operational_data(self, table):
        try:
            cursor_oltp = self._connect_postgres()
            cursor_oltp.execute(f"SELECT * FROM {table}")
            data = cursor_oltp.fetchall()
            # Required for JSON serialization with incompatible data types
            processed_data = [tuple(self.convert_value(value)
                                    for value in row) for row in data]
            return processed_data
        except Exception as e:
            logging.error(f"Error during customer synchronization: {e}")
        finally:
            if cursor_oltp:
                cursor_oltp.close()
                logging.info("Closed PostgreSQL connection.")

    def write_tables_to_analytical_db(self, data, table, dataset_id, schema, write_disposition="WRITE_TRUNCATE"):
        try:
            client_olap = self._connect_bigquery()
            table_id = f"{self.OLAP_DB_CONFIG['project']}.{dataset_id}.{table}"
            
            job_config = bigquery.LoadJobConfig(schema=schema, write_disposition=write_disposition)
            
            # Convert data to BigQuery-compatible format (list of dictionaries)
            rows_to_insert = [dict(zip([field.name for field in schema], row)) for row in data]
            
            job = client_olap.load_table_from_json(rows_to_insert, table_id, job_config=job_config)
            job.result()  # Wait for the job to complete
            logging.info(f"Inserted {len(data)} records into {table_id}.")
        except Exception as e:
            logging.error(f"Error during BigQuery synchronization: {e}")