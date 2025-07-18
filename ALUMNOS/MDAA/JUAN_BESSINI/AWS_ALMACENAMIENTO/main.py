from initial_info import flights, passengers, airplanes
from datetime import datetime
import logging
import argparse
import os

import psycopg2
from dotenv import load_dotenv

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
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


load_dotenv()

RDS_HOST = os.environ['RDS_HOST']
RDS_PORT = os.environ['RDS_PORT']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']

REDSHIFT_HOST = os.environ['REDSHIFT_HOST']
REDSHIFT_PORT = os.environ['REDSHIFT_PORT']
REDSHIFT_USER = os.environ['REDSHIFT_USER']
REDSHIFT_PASSWORD = os.environ['REDSHIFT_PASSWORD']
REDSHIFT_DB = os.environ['REDSHIFT_DB']



def show_object_info(obj):
    """Prints the information of a list of objects.

    Args:
        obj: A list of objects (dictionaries).
    """
    if isinstance(obj, list):
        if obj == flights:
            print("**Flight Information:**")
        elif obj == passengers:
            print("**Passenger Information:**")
        elif obj == airplanes:
            print("**Airplane Information:**")
        for item in obj:
            if isinstance(item, dict):
                for key, value in item.items():
                    print(f"{key}: {value}")
                print("-" * 40)


def register_airplane():
    """Registers a new airplane.

    Returns:
        A list of dictionaries, where each dictionary represents an airplane.
    """
    airplaneList = []
    while True:
        plate_number = input("Enter the airplane's plate number: ")
        airplane_type = input("Enter the airplane's type: ")
        while True:
            last_maintenance_date = input("Enter the last maintenance date (YYYY-MM-DD): ")
            try:
                last_maintenance_date = datetime.strptime(last_maintenance_date, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        while True:
            next_maintenance_date = input("Enter the next maintenance date (YYYY-MM-DD): ")
            try:
                next_maintenance_date = datetime.strptime(next_maintenance_date, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        capacity = input("Enter the airplane's capacity: ")
        try:
            capacity = int(capacity)
        except ValueError:
            print("Invalid input. Capacity must be an integer.")
            capacity = None
        owner_id = input("Enter the owner's ID: ")
        owner_name = input("Enter the owner's name: ")
        hangar_id = input("Enter the hangar ID: ")
        fuel_capacity = input("Enter the fuel capacity: ")
        try:
            fuel_capacity = int(fuel_capacity)
        except ValueError:
            print("Invalid input. Capacity must be an integer.")
            fuel_capacity = None

        airplane = {
            "plateNumber": plate_number,
            "type": airplane_type,
            "lastMaintenanceDate": last_maintenance_date,
            "nextMaintenanceDate": next_maintenance_date,
            "capacity": capacity,
            "ownerId": owner_id,
            "ownerName": owner_name,
            "hangarId": hangar_id,
            "fuel_capacity": fuel_capacity
        }
        airplaneList.append(airplane)
        contin = input("Do you want to add another airplane? (yes/no): ")
        if contin.lower() != "yes":
            break
    return airplaneList

        

def check_days(airplane):
    """Checks the number of days until the next maintenance date.

    Args:
        airplane: A dictionary representing an airplane.
    """
    days = airplane["nextMaintenanceDate"] - datetime.now().date()
    if days.days < 0:
        print("The airplane is overdue for maintenance.")
    else:
        print(f"The next maintenance date is in {days.days} days.")


def register_flight():
    """Registers a new flight.

    Returns:
        A list of dictionaries, where each dictionary represents a flight.
    """
    flightsList = []
    while True:
        flight_id = input("Enter the flightId: ")
        plateNumber = input("Enter the plateNumber: ")
        while True:
            last_maintenance_date = input("Enter the last arrivalTime (YYYY-MM-DDTHH:MM:SS): ")
            try:
                last_maintenance_date = datetime.strptime(last_maintenance_date, "%Y-%m-%dT%H:%M:%S").date()
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        while True:
            departureTime = input("Enter the next maintenance date (YYYY-MM-DDTHH:MM:SS): ")
            try:
                next_maintenance_date = datetime.strptime(departureTime, "%Y-%m-%dT%H:%M:%S").date()
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        fuelConsumption = input("Enter the airplane's capacity: ")
        try:
            fuelConsumption = int(fuelConsumption)
        except ValueError:
            print("Invalid input. Capacity must be an integer.")
            fuelConsumption = None

        occupiedSeats = input("Enter the airplane's capacity: ")
        try:
            occupiedSeats = int(occupiedSeats)
        except ValueError:
            print("Invalid input. Capacity must be an integer.")
            occupiedSeats = None

        origin = input("Enter the owner's ID: ")
        destination = input("Enter the owner's name: ")
        hangar_id = input("Enter the hangar ID: ")

        passengerIds = input("Enter the passenger IDs (comma separated): ")
        # forpassengerIds = input("Enter the number of passagers: ")
        # try:
        #     for i in range(int(forpassengerIds)):
        #         passengerId = input("Enter the passenger ID: ")
        #         status = input("Enter the status: ")
        #         passengerIds.append((passengerId, status))
        # except ValueError:
        #     print("Invalid input. Capacity must be an integer.")
        #     passengerIds = None

        flight = {
            "flightId": flight_id,
            "plateNumber": plateNumber,
            "arrivalTime": last_maintenance_date,
            "departureTime": departureTime,
            "fuelConsumption": fuelConsumption,
            "occupiedSeats": occupiedSeats,
            "origin": origin,
            "destination": destination,
            "passengerIds": passengerIds
        }
        flightsList.append(flight)
        contin = input("Do you want to add another flight? (yes/no): ")
        if contin.lower() != "yes":
            break
    return flightsList


def register_passenger():
    """Registers a new passenger.

    Returns:
        A list of dictionaries, where each dictionary represents a passenger.
    """
    passengerList = []
    while True:
        flight_id = input("Enter the passengerId: ")
        name = input("Enter the name: ")
        nationalId = input("Enter the nationalId: ")
        dateOfBirth = input("Enter the date of birth (YYYY-MM-DD): ")

        passenger = {
            "passengerId": flight_id,
            "name": name,
            "nationalId": nationalId,
            "dateOfBirth": dateOfBirth
        }
        passengerList.append(passenger)
        contin = input("Do you want to add another passenger? (yes/no): ")
        if contin.lower() != "yes":
            break
    return passengerList
        
        

        


def register_obj():
    """Registers a new object (airplane, flight, or passenger)."""
    while True:
        obj = input("What do you want to register? (airplane, flight, passenger): ")
        try:
            obj = str(obj)
            obj = obj.lower().strip()
        except ValueError:
            print("Invalid input. Please enter a valid option.")
            return

        if obj == "airplane":
            print("Registering an airplane...")
            airplanesList = register_airplane()
            for airplane in airplanesList:
                airplanes.append(airplane)

        elif obj == "flight":
            print("Registering a flight...")
            flightsList = register_flight()
            for flight in flightsList:
                flights.append(flight)
        elif obj == "passenger":
            print("Registering a passenger...")
            passengersList = register_passenger()
            for passenger in passengersList:
                passengers.append(passenger)
        else:
            print("Invalid option. Please choose 'airplane', 'flight', or 'passenger'.")
        if input("Do you want to register another object? (yes/no): ").lower() != "yes":
            break
    return airplanes, flights, passengers
    



def connect_to_postgres_rds() -> psycopg2.connect:
    """Connects to the PostgreSQL RDS database.

    Returns:
        A connection object.
    """
    conn = psycopg2.connect(
        host=RDS_HOST,
        port=RDS_PORT,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB
    )
    return conn


def create_database(conn: psycopg2.connect) -> None:
    """Creates a new database in PostgreSQL if it does not exist.

    Args:
        conn: A connection object.
    """
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname='aerodrom';")
    exists = cur.fetchone()
    if not exists:
        cur.execute("CREATE DATABASE aerodrom;")


def create_table(conn: psycopg2.connect, table, schema) -> None:
    """Creates a new table in PostgreSQL if it does not exist.

    Args:
        conn: A connection object.
        table: The name of the table to create.
        schema: The schema of the table.
    """
    conn.autocommit = True
    cur = conn.cursor()
    query = f"CREATE TABLE IF NOT EXISTS {table} {schema};"
    cur.execute(query)


def insert_data(conn: psycopg2.connect, table, data: str) -> None:
    """Inserts data into a PostgreSQL table.

    Args:
        conn: A connection object.
        table: The name of the table to insert data into.
        data: A dictionary representing the data to insert.
    """
    claves = ', '.join(data.keys())
    valores = tuple(data.values())
    placeholders = ', '.join(['%s'] * len(valores))

    cur = conn.cursor()
    query = f"INSERT INTO {table} ({claves}) VALUES ({placeholders});"
    cur.execute(query, valores)
    conn.commit()


def connect_to_redshift() -> psycopg2.connect:
    """Connects to the Redshift database.

    Returns:
        A connection object.
    """
    conn = psycopg2.connect(
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT,
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD,
        database=REDSHIFT_DB
    )
    return conn


def extract_data_from_postgres(conn: psycopg2.connect, table_name: str) -> None:
    """Extracts data from a PostgreSQL table.

    Args:
        conn: A connection object.
        table_name: The name of the table to extract data from.

    Returns:
        A list of tuples, where each tuple represents a row of data.
    """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name};")
    data = cur.fetchall()
    return data


def extract_schema_and_type_from_postgres(conn: psycopg2.connect, table_name: str) -> list:
    """Extracts the schema and data types from a PostgreSQL table.

    Args:
        conn: A connection object.
        table_name: The name of the table to extract the schema from.

    Returns:
        A list of tuples, where each tuple represents a column and its data type.
    """
    cur = conn.cursor()
    cur.execute(f"""SELECT column_name, data_type
                    FROM information_schema.columns
                    WHERE table_name = '{table_name}'
                    ORDER BY ordinal_position;""")  # Ensure correct column order
    data = cur.fetchall()
    return data


def create_table_from_schema_in_aws_redshift(conn: psycopg2.connect, table_name: str, schema: list) -> None:
    """Creates a new table in Redshift from a given schema.

    Args:
        conn: A connection object.
        table_name: The name of the table to create.
        schema: A list of tuples, where each tuple represents a column and its data type.
    """
    cur = conn.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                {', '.join([f'{column[0]} {column[1]}' for column in schema])}
                );"""
    cur.execute(query)
    conn.commit()


def insert_data_redshift(conn: psycopg2.connect, table_name: str, schema: list, data: tuple) -> None:
    """Inserts data into a Redshift table.

    Args:
        conn: A connection object.
        table_name: The name of the table to insert data into.
        schema: A list of tuples, where each tuple represents a column and its data type.
        data: A tuple representing the data to insert.
    """
    cur = conn.cursor()
    columns = ', '.join([column[0] for column in schema])
    placeholders = ', '.join(['%s'] * len(data))
    query = f"""INSERT INTO {table_name} ({columns})
                VALUES ({placeholders});
            """
    cur.execute(query, data)
    conn.commit()

def fligths_info():
    """Prints the information of all flights, passengers, and airplanes."""
    show_object_info(flights)
    show_object_info(passengers)
    show_object_info(airplanes)


def load_catalog_iceberg(provider: str, warehouse_bucket: str, region: str) -> Catalog:
    """Loads the Iceberg catalog.

    Args:
        provider: The type of catalog to load (e.g., "glue").
        warehouse_bucket: The S3 bucket to use as the warehouse.
        region: The AWS region.

    Returns:
        A Catalog object.
    """
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
    """Creates a new Iceberg table.

    Args:
        catalog: A Catalog object.
        schema: The schema of the table.
        table_name: The name of the table to create.
        table_location: The S3 location to store the table data.
        partition_spec: The partition spec for the table.
    """
    if catalog.table_exists(table_name):
        logging.info(f"Table '{table_name}' already exists!")
        return None
    catalog.create_table(
        identifier=table_name,
        location=table_location,
        schema=schema,
        partition_spec=partition_spec,
    )


def insert_data_iceberg(data: list[dict],
                        iceberg_table: Table) -> None:
    """Inserts data into an Iceberg table.

    Args:
        data: A list of dictionaries, where each dictionary represents a row of data.
        iceberg_table: The Iceberg table to insert data into.
    """
    df = pd.DataFrame(data)
    arrow_table = Table.from_pandas(df)
    with iceberg_table.transaction() as txn:
        txn.append(arrow_table)


def read_data_iceberg(table: Table) -> pd.DataFrame:
    """Reads data from an Iceberg table.

    Args:
        table: The Iceberg table to read data from.

    Returns:
        A pandas DataFrame containing the table data.
    """
    rows = table.scan().to_arrow().to_pandas()
    return rows
    

    



def main():
    """Main function to run the data pipeline."""
    fligths_info()
    airplanes, flights, passengers = register_obj()

    parser = argparse.ArgumentParser(description="Usar un perfil de AWS CLI desde Python")
    parser.add_argument('--type', type=str, required=True, help='Nombre del perfil AWS')
    args = parser.parse_args()

    if args.type == "iceberg":
        provider = "glue"
        warehouse_bucket = "s3://iceberg-bucket-joan/"
        region = "eu-north-1"
        catalog = load_catalog_iceberg(provider, warehouse_bucket, region)
        logging.info("Catalog loaded")

        database_name = "db1"

        while True:
            table_name = input("Enter the table you want to insert: ")
            if table_name == "airplane":
                iceberg_table_identifier = f"{database_name}.{table_name}"
                schema = Schema(
                    NestedField(field_id=1, name="plateNumber", field_type=StringType(), required=False),
                    NestedField(field_id=2, name="name", field_type=StringType(), required=False),
                    NestedField(field_id=3, name="type", field_type=StringType(), required=False),
                    NestedField(field_id=4, name="lastMaintenanceDate", field_type=StringType(), required=False),
                    NestedField(field_id=5, name="nextMaintenanceDate", field_type=StringType(), required=False),
                    NestedField(field_id=6, name="capacity", field_type=IntegerType(), required=False),
                    NestedField(field_id=7, name="ownerId", field_type=StringType(), required=False),
                    NestedField(field_id=8, name="ownerName", field_type=StringType(), required=False),
                    NestedField(field_id=9, name="hangarId", field_type=StringType(), required=False),
                    NestedField(field_id=10, name="fuel_capacity", field_type=IntegerType(), required=False),
                )
                partition_spec = PartitionSpec(spec_id=0)
                iceberg_table_location = f"{warehouse_bucket}{database_name}/{table_name}"
                create_table_iceberg(catalog, schema, iceberg_table_identifier,
                                     iceberg_table_location, partition_spec)
                logging.info("Table airplane created")
                data_list = airplanes

            elif table_name == "flight":
                iceberg_table_identifier = f"{database_name}.{table_name}"
                schema = Schema(
                    NestedField(field_id=1, name="flightId", field_type=StringType(), required=False),
                    NestedField(field_id=2, name="plateNumber", field_type=StringType(), required=False),
                    NestedField(field_id=3, name="arrivalTime", field_type=StringType(), required=False),
                    NestedField(field_id=4, name="departureTime", field_type=StringType(), required=False),
                    NestedField(field_id=5, name="fuelConsumption", field_type=IntegerType(), required=False),
                    NestedField(field_id=6, name="occupiedSeats", field_type=IntegerType(), required=False),
                    NestedField(field_id=7, name="origin", field_type=StringType(), required=False),
                    NestedField(field_id=8, name="destination", field_type=StringType(), required=False),
                    NestedField(field_id=9, name="passengerIds", field_type=StringType(), required=False),
                )
                partition_spec = PartitionSpec(spec_id=0)
                iceberg_table_location = f"{warehouse_bucket}{database_name}/{table_name}"
                create_table_iceberg(catalog, schema, iceberg_table_identifier,
                                     iceberg_table_location, partition_spec)
                logging.info("Table flight created")
                data_list = flights

            elif table_name == "passenger":
                iceberg_table_identifier = f"{database_name}.{table_name}"
                schema = Schema(
                    NestedField(field_id=1, name="passengerId", field_type=StringType(), required=False),
                    NestedField(field_id=2, name="name", field_type=StringType(), required=False),
                    NestedField(field_id=3, name="nationalId", field_type=StringType(), required=False),
                    NestedField(field_id=4, name="dateOfBirth", field_type=StringType(), required=False),
                )
                partition_spec = PartitionSpec(spec_id=0)
                iceberg_table_location = f"{warehouse_bucket}{database_name}/{table_name}"
                create_table_iceberg(catalog, schema, iceberg_table_identifier,
                                     iceberg_table_location, partition_spec)
                logging.info("Table flight created")
                data_list = passengers

            else:
                logging.info("Invalid table name")
                continue

            iceberg_table = catalog.load_table(iceberg_table_identifier)
            insert_data_iceberg(data_list, iceberg_table)
            logging.info("Data inserted")

            Next = input("Do you want to insert more data? (yes/no): ")
            if Next.lower() != "yes":
                break

        rows = read_data_iceberg(iceberg_table)
        logging.info(rows)

    elif args.type == "rds":
        logging.info("Connecting to RDS")
        conn = connect_to_postgres_rds()
        logging.info("Connected to RDS")
        logging.info("Creating database")
        create_database(conn)
        logging.info("Database created")
        logging.info("Creating table")

        while True:
            table = input("Enter the table you want to insert: ")
            if table == "airplane":
                schema = """(plateNumber VARCHAR(50),
                        name VARCHAR(50),
                        type VARCHAR(50),
                        lastMaintenanceDate TIMESTAMP,
                        nextMaintenanceDate TIMESTAMP,
                        capacity INTEGER,
                        ownerId VARCHAR(50),
                        ownerName VARCHAR(50),
                        hangarId VARCHAR(50),
                        fuel_capacity INTEGER)"""
                create_table(conn, table, schema)
                logging.info("Table created")
                logging.info("Inserting data")
                data_list = airplanes

            elif table == "flight":
                schema = """(flightId VARCHAR(50),
                        plateNumber VARCHAR(50),
                        arrivalTime TIMESTAMP,
                        departureTime TIMESTAMP,
                        fuelConsumption INTEGER,
                        occupiedSeats INTEGER,
                        origin VARCHAR(50),
                        destination VARCHAR(50),
                        passengerIds VARCHAR(255))"""

                create_table(conn, table, schema)
                logging.info("Table created")
                logging.info("Inserting data")
                data_list = flights

            elif table == "passenger":
                schema = """(passengerId VARCHAR(50),
                        name VARCHAR(50),
                        nationalId VARCHAR(50),
                        dateOfBirth TIMESTAMP)"""
                create_table(conn, table, schema)
                logging.info("Table created")
                logging.info("Inserting data")
                data_list = passengers

            else:
                logging.info("Invalid table name")
                continue

            for data in data_list:
                insert_data(conn, table, data)
            logging.info("Data inserted")

            Next = input("Do you want to insert more data? (yes/no): ")
            if Next.lower() != "yes":
                break
        conn.close()

        conn_postgres = connect_to_postgres_rds()
        conn_redshift = connect_to_redshift()
        logging.info("Connected to RDS")
        logging.info("Extracting data from postgres")
        tables_names = ['airplane', 'flight', 'passenger']
        for postgres_table in tables_names:
            data_rows = extract_data_from_postgres(conn_postgres, postgres_table)
            logging.info("Data extracted")
            logging.info("Extracting schema and type from postgres")
            schema = extract_schema_and_type_from_postgres(conn_postgres, postgres_table)
            print(schema)
            logging.info("Schema extracted")
            logging.info("Creating table in redshift")
            create_table_from_schema_in_aws_redshift(conn_redshift, postgres_table, schema)
            logging.info("Table created")
            logging.info("Inserting data in redshift")
            for row in data_rows:
                insert_data_redshift(conn_redshift, postgres_table, schema, row)
                logging.info("Data inserted: %s", row)
        logging.info("All data inserted into Redshift")
        conn_postgres.close()
        conn_redshift.close()

    else:
        logging.info("Invalid type")
        exit()


if __name__ == "__main__":
    main()