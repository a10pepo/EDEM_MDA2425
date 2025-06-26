import logging
import os

import psycopg2
from dotenv import load_dotenv

from initial_info import flights as original_flights 
from initial_info import passengers as original_passengers
from initial_info import airplanes as original_airplanes 

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
    cur.execute("SELECT 1 FROM pg_database WHERE datname='testdb';")
    exists = cur.fetchone()
    if not exists:
        cur.execute("CREATE DATABASE testdb;")

def create_table(conn: psycopg2.connect) -> None:
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS airplanes (
        plateNumber VARCHAR(50) PRIMARY KEY,
        type VARCHAR(50),
        lastMaintenanceDate DATE,
        nextMaintenanceDate DATE,
        capacity INTEGER,
        ownerId VARCHAR(50),
        ownerName VARCHAR(50),
        hangarId VARCHAR(50),
        fuel_capacity INTEGER
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS passengers (
        passengerId VARCHAR(50) PRIMARY KEY,
        name VARCHAR(100),
        nationalId VARCHAR(20),
        dateOfBirth DATE
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS flights (
        flightId VARCHAR(50) PRIMARY KEY,
        plateNumber VARCHAR(50),
        arrivalTime TIMESTAMP,
        departureTime TIMESTAMP,
        fuelConsumption INTEGER,
        occupiedSeats INTEGER,
        origin VARCHAR(100),
        destination VARCHAR(100),
        FOREIGN KEY (plateNumber) REFERENCES airplanes(plateNumber)
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS flight_passengers (
        flightId VARCHAR(50),
        passengerId VARCHAR(50),
        status VARCHAR(20),
        PRIMARY KEY (flightId, passengerId),
        FOREIGN KEY (flightId) REFERENCES flights(flightId),
        FOREIGN KEY (passengerId) REFERENCES passengers(passengerId)
    );
    """)
    conn.commit()


def insert_data_airplanes(conn: psycopg2.connect, data: dict) -> None:
    """
    Inserta datos en la tabla airplanes.
    """
    cur = conn.cursor()
    query = """
    INSERT INTO airplanes (plateNumber, type, lastMaintenanceDate, nextMaintenanceDate,
                           capacity, ownerId, ownerName, hangarId, fuel_capacity)
    VALUES (%(plateNumber)s, %(type)s, %(lastMaintenanceDate)s, %(nextMaintenanceDate)s,
            %(capacity)s, %(ownerId)s, %(ownerName)s, %(hangarId)s, %(fuel_capacity)s)
    ON CONFLICT (plateNumber) DO NOTHING;
    """
    cur.execute(query, data)
    conn.commit()
    cur.close()


def insert_data_passengers(conn: psycopg2.connect, data: dict) -> None:
    """
    Inserta datos en la tabla passengers.
    """
    cur = conn.cursor()
    query = """
    INSERT INTO passengers (passengerId, name, nationalId, dateOfBirth)
    VALUES (%(passengerId)s, %(name)s, %(nationalId)s, %(dateOfBirth)s)
    ON CONFLICT (passengerId) DO NOTHING;
    """
    cur.execute(query, data)
    conn.commit()
    cur.close()


def insert_data_flights(conn: psycopg2.connect, data: dict) -> None:
    cur = conn.cursor()
    flight_query = """
    INSERT INTO flights (flightId, plateNumber, arrivalTime, departureTime,
                         fuelConsumption, occupiedSeats, origin, destination)
    VALUES (%(flightId)s, %(plateNumber)s, %(arrivalTime)s, %(departureTime)s,
            %(fuelConsumption)s, %(occupiedSeats)s, %(origin)s, %(destination)s)
    ON CONFLICT (flightId) DO NOTHING;
    """
    cur.execute(flight_query, data)
    
    if "passengerIds" in data:
        passenger_query = """
        INSERT INTO flight_passengers (flightId, passengerId, status)
        VALUES (%s, %s, %s);
        """
        for passenger in data["passengerIds"]:
            passengerId, status = passenger
            cur.execute(passenger_query, (data["flightId"], passengerId, status))
    
    conn.commit()
    cur.close()


if __name__ == "__main__":
    logging.info("Connecting to RDS")
    conn = connect_to_postgres_rds()
    logging.info("Connected to RDS")
    logging.info("Creating database")
    create_database(conn)
    logging.info("Database created")
    logging.info("Creating tables")
    create_table(conn)
    logging.info("Tables created")
    logging.info("Inserting data")
    for airplane in original_airplanes:
        insert_data_airplanes(conn, airplane)
    for passenger in original_passengers:
        insert_data_passengers(conn, passenger)
    for flights in original_flights:
        insert_data_flights(conn, flights)
    logging.info("Data inserted")
    conn.close()