from initial_info import flights as vuelos, passengers as viajeros, airplanes as aviones
import logging
import os
import psycopg2
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv()

PG_HOST = os.environ['RDS_HOST']
PG_PORT = os.environ['RDS_PORT']
PG_USER = os.environ['RDS_USER']
PG_PASS = os.environ['RDS_PASSWORD']
PG_DB = os.environ['RDS_DB']

def conexion_pg():
    return psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        user=PG_USER,
        password=PG_PASS,
        database=PG_DB
    )

def crear_db(conn):
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname='info_aeropuertos';")
    if not cur.fetchone():
        cur.execute("CREATE DATABASE info_aeropuertos;")

def tabla_avion(conn):
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS airplane (plateNumber VARCHAR(50) PRIMARY KEY, type VARCHAR(50), lastMaintenanceDate TIMESTAMP, nextMaintenanceDate TIMESTAMP, capacity INT, ownerId VARCHAR(50), ownerName VARCHAR(250), hangarId VARCHAR(250), fuel_capacity INT);""")

def insertar_avion(conn, avion):
    cur = conn.cursor()
    q = """
        INSERT INTO airplane (
            plateNumber, type, lastMaintenanceDate, nextMaintenanceDate,
            capacity, ownerId, ownerName, hangarId, fuel_capacity
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (plateNumber) DO NOTHING;
    """
    cur.execute(q, (
        avion["plateNumber"],
        avion["type"],
        avion["lastMaintenanceDate"],
        avion["nextMaintenanceDate"],
        avion["capacity"],
        avion["ownerId"],
        avion["ownerName"],
        avion["hangarId"],
        avion["fuel_capacity"]
    ))
    conn.commit()

def tabla_vuelos(conn):
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS flights (plateNumber VARCHAR(50) PRIMARY KEY, flightId VARCHAR(50), arrivalTime TIMESTAMP, departureTime TIMESTAMP, fuelConsumption INT, occupiedSeats INT, origin VARCHAR(250), destination VARCHAR(250), passengersIds VARCHAR(250));""")

def insertar_vuelo(conn, vuelo):
    cur = conn.cursor()
    q = """
        INSERT INTO flights (
            plateNumber, flightId, arrivalTime, departureTime,
            fuelConsumption, occupiedSeats, origin, destination, passengersIds
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (plateNumber) DO NOTHING;
    """
    cur.execute(q, (
        vuelo["plateNumber"],
        vuelo["flightId"],
        vuelo["arrivalTime"],
        vuelo["departureTime"],
        vuelo["fuelConsumption"],
        vuelo["occupiedSeats"],
        vuelo["origin"],
        vuelo["destination"],
        ','.join([f"{x[0]}:{x[1]}" for x in vuelo["passengerIds"]])
    ))
    conn.commit()

def tabla_viajeros(conn):
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS passengers (passengerId VARCHAR(50) PRIMARY KEY, name VARCHAR(250), nationalId VARCHAR(50), dateOfBirth DATE);""")

def insertar_viajero(conn, viajero):
    cur = conn.cursor()
    q = """
        INSERT INTO passengers (
            passengerId, name, nationalId, dateOfBirth
        )
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (passengerId) DO NOTHING;
    """
    cur.execute(q, (
        viajero["passengerId"],
        viajero["name"],
        viajero["nationalId"],
        viajero["dateOfBirth"]
    ))
    conn.commit()

if __name__ == "__main__":
    logging.info("Conectando a RDS")
    conn = conexion_pg()
    logging.info("Conectado a RDS")
    logging.info("Creando tablas")
    tabla_avion(conn)
    tabla_vuelos(conn)
    logging.info("Tablas creadas")
    logging.info("Insertando datos")
    for avion in aviones:
        insertar_avion(conn, avion)
    for vuelo in vuelos:
        insertar_vuelo(conn, vuelo)
    logging.info("Datos insertados")
    conn.close()