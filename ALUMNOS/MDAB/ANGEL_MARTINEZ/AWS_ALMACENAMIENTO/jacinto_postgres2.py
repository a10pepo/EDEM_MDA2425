import logging
import os

import psycopg2
from dotenv import load_dotenv
from initial_info import airplanes, flights, passengers

logging.basicConfig(level=logging.INFO)

load_dotenv()

RDS_HOST = os.environ['RDS_HOST']
RDS_PORT = os.environ['RDS_PORT']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']

def airplane_values(airplane: dict) -> tuple:
    return (
        airplane["plateNumber"],
        airplane["type"],
        airplane["lastMaintenanceDate"],
        airplane["nextMaintenanceDate"],
        airplane["capacity"],
        airplane["ownerId"],
        airplane["ownerName"],
        airplane["hangarId"],
        airplane["fuel_capacity"]
    )

def flight_values(flight: dict) -> tuple:
    return (
        flight["flightId"],
        flight["plateNumber"],
        flight["arrivalTime"],
        flight["departureTime"],
        flight["fuelConsumption"],
        flight["occupiedSeats"],
        flight["origin"],
        flight["destination"]
    )

def passenger_values(passenger: dict) -> tuple:
    return (
        passenger["passengerId"],
        passenger["name"],
        passenger["nationalId"],
        passenger["dateOfBirth"]
    )

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


def create_tables(conn: psycopg2.connect) -> None:
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS aviones (plateNumber VARCHAR(50), type VARCHAR(50), lastMaintenanceDate DATE, nextMaintenanceDate DATE, capacity INT, ownerID VARCHAR(10), ownerName VARCHAR(50), hangarID VARCHAR(10), fuel_capacity INT);")
    cur.execute("CREATE TABLE IF NOT EXISTS vuelos (flightId VARCHAR(20), plateNumber VARCHAR(50), arrivalTime TIMESTAMP, departureTime TIMESTAMP, fuelConsumption INT, occupiedSeats INT, origin VARCHAR(50), destination VARCHAR(50));")
    cur.execute("CREATE TABLE IF NOT EXISTS pasajeros (passengerId VARCHAR(20), name VARCHAR(100), nationalId VARCHAR(20), dateOfBirth DATE);")
    conn.commit()
    

def insert_airplanes(conn: psycopg2.connect, values) -> None:
    cur = conn.cursor()
    query = """
        INSERT INTO aviones (plateNumber, type, lastMaintenanceDate, nextMaintenanceDate, capacity, ownerID, ownerName, hangarID, fuel_capacity)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    for plane in values:
        cur.execute(query, airplane_values(plane))
    conn.commit()

def insert_flights(conn: psycopg2.connect, values) -> None:
    cur = conn.cursor()
    query = """
        INSERT INTO vuelos (flightId, plateNumber, arrivalTime, departureTime, fuelConsumption, occupiedSeats, origin, destination)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    for flight in values:
        cur.execute(query, flight_values(flight))
    conn.commit()

def insert_passengers(conn: psycopg2.connect, values) -> None:
    cur = conn.cursor()
    query = """
        INSERT INTO pasajeros (passengerId, name, nationalId, dateOfBirth)
        VALUES (%s, %s, %s, %s);
    """
    for passenger in values:
        cur.execute(query, passenger_values(passenger))
    conn.commit()

if __name__ == "__main__":
    logging.info("Connecting to RDS")
    conn = connect_to_postgres_rds()
    logging.info("Connected to RDS")
    logging.info("Creating tables")
    create_tables(conn)
    logging.info("Tables created")
    logging.info("Inserting airplane data")
    insert_airplanes(conn, airplanes)
    logging.info("Airplane data inserted")
    logging.info("Inserting flight data")
    insert_flights(conn, flights)
    logging.info("Flight data inserted")
    logging.info("Inserting passenger data")
    insert_passengers(conn, passengers)
    logging.info("Passenger data inserted")
    
    conn.close()