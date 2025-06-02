from initial_info import flights, passengers, airplanes
import logging
import os

import psycopg2
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

RDS_HOST = os.environ['RDS_HOST']
RDS_PORT = os.environ['RDS_PORT']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']


def connect_to_postgres_rds() -> psycopg2.connect:
    conn = psycopg2.connect(
        host=RDS_HOST,
        port=RDS_PORT,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB
    )
    return conn


def create_database(conn: psycopg2.connect) -> None:
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname='info_aeropuertos';")
    exists = cur.fetchone()
    if not exists:
        cur.execute("CREATE DATABASE info_aeropuertos;")


def create_table_airplane(conn: psycopg2.connect) -> None:
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS airplane (plateNumber VARCHAR(50) PRIMARY KEY,
                type VARCHAR(50), lastMaintenanceDate TIMESTAMP, nextMaintenanceDate TIMESTAMP,
                capacity INT, ownerId VARCHAR(50), ownerName VARCHAR(250), hangarId VARCHAR(250), fuel_capacity INT);""")

def insert_data_airplane(conn: psycopg2.connect, airplane: dict) -> None:
    inserta_airplane(conn, airplane)

def inserta_airplane(conn, airplane):
    cur = conn.cursor()
    query = """
        INSERT INTO airplane (
            plateNumber, type, lastMaintenanceDate, nextMaintenanceDate,
            capacity, ownerId, ownerName, hangarId, fuel_capacity
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (plateNumber) DO NOTHING;
    """
    cur.execute(query, (
        airplane["plateNumber"],
        airplane["type"],
        airplane["lastMaintenanceDate"],
        airplane["nextMaintenanceDate"],
        airplane["capacity"],
        airplane["ownerId"],
        airplane["ownerName"],
        airplane["hangarId"],
        airplane["fuel_capacity"]
    ))
    conn.commit()

def create_table_flights(conn: psycopg2.connect) -> None:
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS flights (plateNumber VARCHAR(50) PRIMARY KEY,
                flightId VARCHAR(50), arrivalTime TIMESTAMP, departureTime TIMESTAMP,
                fuelConsumption INT, occupiedSeats INT, origin VARCHAR(250), destination VARCHAR(250), passengersIds VARCHAR(250));""")
    

def insert_data_flights(conn: psycopg2.connect, flight: dict) -> None:
    insert_flights(conn, flight)

def insert_flights(conn, flight):
    cur = conn.cursor()
    query = """
        INSERT INTO flights (
            plateNumber, flightId, arrivalTime, departureTime,
            fuelConsumption, occupiedSeats, origin, destination, passengersIds
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (plateNumber) DO NOTHING;
    """
    cur.execute(query, (
        flight["plateNumber"],
        flight["flightId"],
        flight["arrivalTime"],
        flight["departureTime"],
        flight["fuelConsumption"],
        flight["occupiedSeats"],
        flight["origin"],
        flight["destination"],
        ','.join([f"{pid[0]}:{pid[1]}" for pid in flight["passengerIds"]])
    ))
    conn.commit()


def create_table_passengers(conn: psycopg2.connect) -> None:
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS passengers (passengerId VARCHAR(50) PRIMARY KEY,
                name VARCHAR(250), nationalId VARCHAR(50), dateOfBirth DATE);""")

def insert_data_passengers(conn: psycopg2.connect, passenger: dict) -> None:
    insert_passenger(conn, passenger)


def insert_passenger(conn, passenger):
    cur = conn.cursor()
    query = """
        INSERT INTO passengers (
            passengerId, name, nationalId, dateOfBirth
        )
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (passengerId) DO NOTHING;
    """
    cur.execute(query, (
        passenger["passengerId"],
        passenger["name"],
        passenger["nationalId"],
        passenger["dateOfBirth"]
    ))
    conn.commit()
    

if __name__ == "__main__":
    logging.info("Connecting to RDS")
    conn = connect_to_postgres_rds()
    logging.info("Connected to RDS")

    logging.info("Creating tables")
    create_table_airplane(conn)
    create_table_flights(conn)
    logging.info("Tables created")

    logging.info("Inserting data")
    for airplane in airplanes:
        insert_data_airplane(conn, airplane)
    for flight in flights:
        insert_data_flights(conn, flight)
    logging.info("All data inserted")

    conn.close()