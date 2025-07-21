import os
import logging
import psycopg2
from dotenv import load_dotenv
from initial_info import airplanes, flights, passengers

# Configuración de logs y entorno
logging.basicConfig(level=logging.INFO)
load_dotenv()

# Variables de entorno RDS
RDS_HOST = os.environ['RDS_HOST']
RDS_PORT = os.environ['RDS_PORT']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']

# Conexión
def connect_to_postgres_rds() -> psycopg2.connect:
    return psycopg2.connect(
        host=RDS_HOST,
        port=RDS_PORT,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB
    )

# Crear base de datos si no existe (aunque no se use por defecto)
def create_database(conn: psycopg2.connect) -> None:
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute("SELECT 1 FROM pg_database WHERE datname='testdb';")
        if not cur.fetchone():
            cur.execute("CREATE DATABASE testdb;")

# Crear tablas
def create_all_tables(conn: psycopg2.connect) -> None:
    queries = [
        """CREATE TABLE IF NOT EXISTS aviones (
            plateNumber VARCHAR(50),
            type VARCHAR(50),
            lastMaintenanceDate DATE,
            nextMaintenanceDate DATE,
            capacity INT,
            ownerID VARCHAR(10),
            ownerName VARCHAR(50),
            hangarID VARCHAR(10),
            fuel_capacity INT
        );""",
        """CREATE TABLE IF NOT EXISTS vuelos (
            flightId VARCHAR(20),
            plateNumber VARCHAR(50),
            arrivalTime TIMESTAMP,
            departureTime TIMESTAMP,
            fuelConsumption INT,
            occupiedSeats INT,
            origin VARCHAR(50),
            destination VARCHAR(50)
        );""",
        """CREATE TABLE IF NOT EXISTS pasajeros (
            passengerId VARCHAR(20),
            name VARCHAR(100),
            nationalId VARCHAR(20),
            dateOfBirth DATE
        );"""
    ]
    with conn.cursor() as cur:
        for query in queries:
            cur.execute(query)
    conn.commit()

# Helpers
def prepare_airplane(a): return (
    a["plateNumber"], a["type"], a["lastMaintenanceDate"], a["nextMaintenanceDate"],
    a["capacity"], a["ownerId"], a["ownerName"], a["hangarId"], a["fuel_capacity"]
)

def prepare_flight(f): return (
    f["flightId"], f["plateNumber"], f["arrivalTime"], f["departureTime"],
    f["fuelConsumption"], f["occupiedSeats"], f["origin"], f["destination"]
)

def prepare_passenger(p): return (
    p["passengerId"], p["name"], p["nationalId"], p["dateOfBirth"]
)

# Inserciones
def insert_data(conn, table, query, values, formatter):
    with conn.cursor() as cur:
        for v in values:
            cur.execute(query, formatter(v))
    conn.commit()

def main():
    try:
        logging.info("Conectando a PostgreSQL RDS...")
        conn = connect_to_postgres_rds()

        logging.info("Creando tablas...")
        create_all_tables(conn)

        logging.info("Insertando datos de aviones...")
        insert_data(conn, 'aviones',
            """INSERT INTO aviones (plateNumber, type, lastMaintenanceDate, nextMaintenanceDate, capacity, ownerID, ownerName, hangarID, fuel_capacity)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);""",
            airplanes, prepare_airplane
        )

        logging.info("Insertando datos de vuelos...")
        insert_data(conn, 'vuelos',
            """INSERT INTO vuelos (flightId, plateNumber, arrivalTime, departureTime, fuelConsumption, occupiedSeats, origin, destination)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",
            flights, prepare_flight
        )

        logging.info("Insertando datos de pasajeros...")
        insert_data(conn, 'pasajeros',
            """INSERT INTO pasajeros (passengerId, name, nationalId, dateOfBirth)
               VALUES (%s, %s, %s, %s);""",
            passengers, prepare_passenger
        )

        logging.info("Carga de datos completada correctamente.")

    except Exception as e:
        logging.error(f"Error durante la carga: {e}")
    finally:
        conn.close()
        logging.info("Conexión cerrada.")

if __name__ == "__main__":
    main()
