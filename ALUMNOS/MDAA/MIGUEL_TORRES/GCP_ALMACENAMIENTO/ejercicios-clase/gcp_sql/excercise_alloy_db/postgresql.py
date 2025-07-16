import psycopg2
from psycopg2.extras import execute_batch
import random
import time
from datetime import datetime, timedelta
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

# Connection parameters
DB_HOST = "34.175.112.182"
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "EDEM2425"

# Connect to AlloyDB
try:
    logging.info("Connecting to the database...")
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    conn.autocommit = False
    cursor = conn.cursor()
    logging.info("Connected to the database successfully.")
except Exception as e:
    logging.error(f"Error connecting to the database: {e}")
    exit()

# Step 1: Create tables
try:
    logging.info("Creating tables...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS currencies (
            id SERIAL PRIMARY KEY,
            currency_code VARCHAR(10) UNIQUE NOT NULL,
            currency_name VARCHAR(50) NOT NULL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id SERIAL PRIMARY KEY,
            currency_id INT NOT NULL,
            base_currency_code VARCHAR(10) NOT NULL,
            rate NUMERIC(10, 6) NOT NULL,
            timestamp TIMESTAMP DEFAULT NOW(),
            FOREIGN KEY (currency_id) REFERENCES currencies (id) ON DELETE CASCADE
        );
    """)
    conn.commit()
    logging.info("Tables created successfully.")
except Exception as e:
    conn.rollback()
    logging.error(f"Error creating tables: {e}")
    cursor.close()
    conn.close()
    exit()

# Step 2: Insert data into currencies table
currency_data = [
    ("USD", "United States Dollar"),
    ("EUR", "Euro"),
    ("JPY", "Japanese Yen"),
    ("GBP", "British Pound Sterling"),
    ("AUD", "Australian Dollar"),
    ("CAD", "Canadian Dollar"),
    ("CHF", "Swiss Franc"),
    ("CNY", "Chinese Yuan"),
    ("SEK", "Swedish Krona"),
    ("NZD", "New Zealand Dollar")
]

try:
    logging.info("Inserting data into currencies table...")
    execute_batch(cursor, "INSERT INTO currencies (currency_code, currency_name) VALUES (%s, %s) ON CONFLICT (currency_code) DO NOTHING", currency_data)
    conn.commit()
    logging.info("Inserted data into currencies table successfully.")
except Exception as e:
    conn.rollback()
    logging.error(f"Error inserting data into currencies table: {e}")

# Step 3: Insert data into exchange_rates table
try:
    logging.info("Fetching currency IDs for exchange rate insertion...")
    cursor.execute("SELECT id, currency_code FROM currencies")
    currencies = cursor.fetchall()

    exchange_data = []
    base_currency = "USD"
    start_time = datetime.now()

    logging.info("Generating and inserting exchange rate data...")
    while True:
        for _ in range(10000):  # 10,000 rows
            currency_id, currency_code = random.choice(currencies)
            rate = round(random.uniform(0.5, 1.5), 6)  # Random exchange rate
            timestamp = start_time - timedelta(minutes=random.randint(0, 10000))
            exchange_data.append((currency_id, base_currency, rate, timestamp))

        execute_batch(cursor, """
            INSERT INTO exchange_rates (currency_id, base_currency_code, rate, timestamp)
            VALUES (%s, %s, %s, %s)
        """, exchange_data)
        conn.commit()
        logging.info(f"Inserted {len(exchange_data)} exchange rate rows successfully.")
except Exception as e:
    conn.rollback()
    logging.error(f"Error inserting exchange rate data: {e}")
finally:
    cursor.close()
    conn.close()
    logging.info("Database connection closed.")
