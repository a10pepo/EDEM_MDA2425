import logging

import psycopg2
from clickhouse_driver import Client


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

    def _connect_clickhouse(self):
        try:
            self.conn_olap = Client(**self.OLAP_DB_CONFIG)
            logging.info("Connected to ClickHouse successfully.")
            return self.conn_olap
        except Exception as e:
            logging.error(f"Failed to connect to ClickHouse: {e}")
            raise

    def get_operational_data(self, table):
        try:
            cursor_oltp = self._connect_postgres()
            cursor_oltp.execute(f"SELECT * FROM {table}")
            data = cursor_oltp.fetchall()
            return data
        except Exception as e:
            logging.error(f"Error during customer synchronization: {e}")
        finally:
            if cursor_oltp:
                cursor_oltp.close()
                logging.info("Closed PostgreSQL connection.")

    def write_tables_to_analytical_db(self, data, table, table_ddl, values):
        try:
            client_olap = self._connect_clickhouse()
            logging.info(f"Fetched {len(data)} {table} from PostgreSQL.")
            client_olap.execute(f"DROP TABLE IF EXISTS {table}_temp")
            client_olap.execute(table_ddl)
            logging.info(f"Created table {table}_temp in ClickHouse.")
            query = f"INSERT INTO analytics_db.{table}_temp VALUES {values}"
            client_olap.execute(query)
            logging.info(f"Inserted data into {table}_temp table.")
            client_olap.execute(f"""
                RENAME TABLE {table} TO {table}_old, {table}_temp TO {table}
            """)
            client_olap.execute(f"DROP TABLE IF EXISTS {table}_old")
            logging.info(f"Successfully synchronized {table}  table.")
        except Exception as e:
            logging.error(f"Error during customer synchronization: {e}")

    def write_events_to_analytical_db(self, data, table, values):
        try:
            client_olap = self._connect_clickhouse()
            logging.info(f"Fetched {len(data)} {table} from PubSub.")
            query = f"INSERT INTO analytics_db.{table} VALUES {values}"
            client_olap.execute(query)
            logging.info(f"Successfully synchronized {table}  table.")
        except Exception as e:
            logging.error(f"Error during customer synchronization: {e}")
