import logging
import os

from utils.db_manager_utils import DbManager


def syncronize_customers(db_conn_manager, data):
    customers_ddl = """CREATE TABLE analytics_db.customers_temp (id UInt32,
                                                                 customer_name String,
                                                                 email String)
                                                                 ENGINE = MergeTree()
                                                                 ORDER BY id"""
    customer_values = ", ".join(
                f"({row[0]}, '{row[1]}', '{row[2]}')" for row in data
            )
    db_conn_manager.write_tables_to_analytical_db(data, 'customers', customers_ddl,
                                                  customer_values)


def syncronize_products(db_conn_manager, data):
    products_ddl = """CREATE TABLE analytics_db.products_temp (id UInt32,
                                                               product_name String,
                                                               price Float32)
                                                               ENGINE = MergeTree()
                                                               ORDER BY id"""
    products_value = ", ".join(
                f"""({row[0]}, '{row[1].replace("'", "")}', {row[2]})""" for row in data
            )
    db_conn_manager.write_tables_to_analytical_db(data, 'products', products_ddl,
                                                  products_value)


def syncronize_orders(db_conn_manager, data):
    orders_ddl = """CREATE TABLE analytics_db.orders_temp (id UInt32, customer_id UInt32,
                                                           created_at DateTime,
                                                           total_price Float32)
                                                           ENGINE = MergeTree()
                                                           ORDER BY id """
    orders_value = ", ".join(
                f"""({row[0]}, {row[1]}, '{row[2].strftime('%Y-%m-%d %H:%M:%S')}',
                     {row[3]})""" for row in data
            )
    db_conn_manager.write_tables_to_analytical_db(data, 'orders', orders_ddl, orders_value)


def syncronize_order_products(db_conn_manager, data):
    order_products_ddl = """CREATE TABLE analytics_db.order_products_temp
                            (order_id UInt32, product_id UInt32, quantity UInt32,
                             price Float32) ENGINE = MergeTree()
                             ORDER BY (order_id, product_id)"""
    order_products_value = ", ".join(
                f"""({row[0]}, {row[1]}, {row[2]}, {row[3]})""" for row in data
            )
    db_conn_manager.write_tables_to_analytical_db(data, 'order_products',
                                                  order_products_ddl, order_products_value)


if __name__ == "__main__":
    logging.basicConfig(
                        level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.StreamHandler()
                        ]
    )
    logger = logging.getLogger()
    OLTP_DB_CONFIG = {
        "dbname": "ecommerce",
        "user": "user",
        "password": "password",
        "host": os.getenv('POSTGRES_IP'),
        "port": 5432,
    }
    OLAP_DB_CONFIG = {
        "host": os.getenv('HOST_IP'),
        "port": 9001,
        "database": "analytics_db",
        "user": "user",
        "password": "password",
        "send_receive_timeout": 10
    }
    logging.info("Starting syncronization.")
    db_conn_manager = DbManager(OLTP_DB_CONFIG, OLAP_DB_CONFIG)

    customers = db_conn_manager.get_operational_data('customers')
    syncronize_customers(db_conn_manager, customers)

    products = db_conn_manager.get_operational_data('products')
    syncronize_products(db_conn_manager, products)

    orders = db_conn_manager.get_operational_data('orders')
    syncronize_orders(db_conn_manager, orders)

    order_products = db_conn_manager.get_operational_data('order_products')
    syncronize_order_products(db_conn_manager, order_products)
    logging.info("Synchronization completed.")
