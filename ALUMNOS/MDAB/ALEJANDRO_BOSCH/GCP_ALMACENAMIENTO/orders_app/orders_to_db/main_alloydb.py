import datetime
import logging
import os
import random
import sys
import time

import psycopg2
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
from google.cloud import storage

from orders_app.chatgpt_orders.orders_handler import (
    get_limited_products,
    get_limited_users,
    create_order,
    create_products_additional_info
)
from utils.events_manager import EventsManager


def upload_to_gcs(local_file_path, gcs_bucket_name, gcs_file_path):
    """
    Sube el archivo local a Google Cloud Storage.
    """
    client = storage.Client()
    bucket = client.bucket(gcs_bucket_name)
    blob = bucket.blob(gcs_file_path)
    blob.upload_from_filename(local_file_path)
    logging.info(f"File uploaded to GCS: gs://{gcs_bucket_name}/{gcs_file_path}")


def save_additional_info_to_parquet(products):
    """
    Crea un archivo parquet a partir de products y lo sube a GCS.
    """
    if not products:
        logging.warning("No products_additional_info found")
        return
    df = pd.DataFrame(products)
    table = pa.Table.from_pandas(df)
    local_parquet_file = "./products_additional_info.parquet"
    pq.write_table(table, local_parquet_file)
    upload_to_gcs(local_parquet_file, GCS_BUCKET_NAME, GCS_FILE_PATH)


def _create_tables():
    """
    Crea las tablas en la base de datos de PostgreSQL si no existen.
    (Base operativa)
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS customers (
            id SERIAL PRIMARY KEY,
            customer_name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL
        );
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY, 
            product_name VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL
        );
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            id SERIAL PRIMARY KEY, 
            customer_id INT NOT NULL,
            created_at TIMESTAMP NOT NULL,
            total_price DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
        );
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS order_products (
            order_id INT NOT NULL,
            product_id INT NOT NULL,
            quantity INT NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            PRIMARY KEY (order_id, product_id),
            FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
            FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
        );
        """
    )
    conn.commit()
    cursor.close()
    conn.close()


def insert_data(order):
    """
    Inserta la orden en la base de datos PostgreSQL (operacional).
    Retorna el order_id generado.
    """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        logging.info("Connection to Database Successful")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO customers (id, customer_name, email)
            VALUES (%s, %s, %s)
            ON CONFLICT (email) DO NOTHING
            RETURNING id;
            """,
            (order['user']['id'], order['user']['name'], order['user']['email'])
        )
        customer_id = cursor.fetchone()
        if not customer_id:
            cursor.execute(
                "SELECT id FROM customers WHERE email = %s;",
                (order['user']['email'],)
            )
            customer_id = cursor.fetchone()[0]
        else:
            customer_id = customer_id[0]

        cursor.execute(
            """
            INSERT INTO orders (customer_id, created_at, total_price)
            VALUES (%s, %s, %s)
            RETURNING id;
            """,
            (customer_id, order['timestamp'], order['totalPrice'])
        )
        order_id = cursor.fetchone()[0]

        for product in order['products']:
            cursor.execute(
                """
                INSERT INTO products (id, product_name, price)
                VALUES (%s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
                """,
                (product['productId'], product['name'], product['price'])
            )
            cursor.execute(
                """
                INSERT INTO order_products (order_id, product_id, quantity, price)
                VALUES (%s, %s, %s, %s);
                """,
                (order_id, product['productId'], product['quantity'], product['price'])
            )

        conn.commit()
        logging.info(f"Order {order_id} inserted successfully in PostgreSQL\n")
        return order_id

    except Exception as e:
        logging.error(f"Error inserting data: {e}")
        sys.exit(1)
    finally:
        cursor.close()
        conn.close()


def insert_data_alloydb(order_id, order):
    """
    Inserta la misma orden en AlloyDB.
    Se asume que las tablas en AlloyDB (customers, products, orders, order_products)
    tienen estructura similar a la de PostgreSQL.
    """
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(**ALLOYDB_CONFIG)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO customers (id, customer_name, email)
            VALUES (%s, %s, %s)
            ON CONFLICT (email) DO NOTHING
            RETURNING id;
            """,
            (order['user']['id'], order['user']['name'], order['user']['email'])
        )
        alloydb_customer_id = cursor.fetchone()
        if not alloydb_customer_id:
            cursor.execute(
                "SELECT id FROM customers WHERE email = %s;",
                (order['user']['email'],)
            )
            alloydb_customer_id = cursor.fetchone()[0]
        else:
            alloydb_customer_id = alloydb_customer_id[0]

        cursor.execute(
            """
            INSERT INTO orders (id, customer_id, created_at, total_price)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
            """,
            (order_id, alloydb_customer_id, order['timestamp'], order['totalPrice'])
        )

        for product in order['products']:
            cursor.execute(
                """
                INSERT INTO products (id, product_name, price)
                VALUES (%s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
                """,
                (product['productId'], product['name'], product['price'])
            )
            cursor.execute(
                """
                INSERT INTO order_products (order_id, product_id, quantity, price)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (order_id, product_id) DO NOTHING;
                """,
                (order_id, product['productId'], product['quantity'], product['price'])
            )

        conn.commit()
        logging.info(f"Order {order_id} inserted successfully in AlloyDB.")
    except Exception as e:
        logging.error(f"Error inserting order {order_id} in AlloyDB: {e}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
    logger = logging.getLogger()

    DB_CONFIG = {
        "dbname": "ecommerce",
        "user": "postgres",
        "password": "EDEM2425",
        "host": os.getenv('HOST_IP'),  
        "port": 5432,
    }


    ALLOYDB_CONFIG = {
        "dbname": "ecommerce",
        "user": "postgres",
        "password": "EDEM2425",
        "host": os.getenv("ALLOYDB_HOST"),
        "port": 5432
    }

    GCS_BUCKET_NAME = os.getenv('GCS_BUCKET_NAME')
    GCS_FILE_PATH = "raw_data/products_additional_info.parquet"

    _create_tables()

    num_orders_generated = 1
    logging.info("Fetching products and users...")
    products_with_details = get_limited_products(limit=20)
    logging.info("Updating DataLake content...")
    products_extra_info = create_products_additional_info(products_with_details)
    save_additional_info_to_parquet(products_extra_info)

    users = get_limited_users(limit=10)
    if not products_with_details or not users:
        logging.info("No products or users available. Exiting.")
        sys.exit(1)

    producer = EventsManager('order-events')
    producer.create_publisher()

    while True:
        user = random.choice(users)
        logging.info(f"Creating new order for customer {user}\n")
        order = create_order(user, products_with_details, num_orders_generated)

        logging.info("Inserting new order in PostgreSQL Database\n")
        order_id = insert_data(order)

        insert_data_alloydb(order_id, order)

        message = {'order_id': order_id, 'created_at': datetime.datetime.now().isoformat()}
        producer.send_message(message)

        num_orders_generated += 1
        time.sleep(random.randint(15, 40))
