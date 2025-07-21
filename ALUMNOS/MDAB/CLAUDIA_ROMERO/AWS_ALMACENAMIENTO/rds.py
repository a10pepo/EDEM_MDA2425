import os
import psycopg2
from dotenv import load_dotenv
from datetime import datetime

from initial_info import airplanes, flights, passengers

load_dotenv()

RDS_HOST = os.environ['RDS_HOST']
RDS_PORT = os.environ['RDS_PORT']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']

def connect():
    return psycopg2.connect(
        host=RDS_HOST,
        port=RDS_PORT,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB
    )

def create_tables(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS airplanes (
                plate_number VARCHAR PRIMARY KEY,
                type VARCHAR,
                last_maintenance_date DATE,
                next_maintenance_date DATE,
                capacity INTEGER,
                owner_id VARCHAR,
                owner_name VARCHAR,
                hangar_id VARCHAR,
                fuel_capacity INTEGER
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS passengers (
                passenger_id VARCHAR PRIMARY KEY,
                name VARCHAR,
                national_id VARCHAR,
                date_of_birth DATE
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS flights (
                flight_id VARCHAR PRIMARY KEY,
                plate_number VARCHAR REFERENCES airplanes(plate_number),
                arrival_time TIMESTAMP,
                departure_time TIMESTAMP,
                fuel_consumption INTEGER,
                occupied_seats INTEGER,
                origin VARCHAR,
                destination VARCHAR
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS flight_passengers (
                flight_id VARCHAR REFERENCES flights(flight_id),
                passenger_id VARCHAR REFERENCES passengers(passenger_id),
                status VARCHAR,
                PRIMARY KEY (flight_id, passenger_id)
            );
        """)
        conn.commit()

def insert_airplanes(conn):
    with conn.cursor() as cur:
        for plane in airplanes:
            cur.execute("""
                INSERT INTO airplanes VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT (plate_number) DO NOTHING;
            """, (
                plane['plateNumber'],
                plane['type'],
                plane['lastMaintenanceDate'],
                plane['nextMaintenanceDate'],
                plane['capacity'],
                plane['ownerId'],
                plane['ownerName'],
                plane['hangarId'],
                plane['fuel_capacity']
            ))
    conn.commit()

def insert_passengers(conn):
    with conn.cursor() as cur:
        for p in passengers:
            cur.execute("""
                INSERT INTO passengers VALUES (%s,%s,%s,%s)
                ON CONFLICT (passenger_id) DO NOTHING;
            """, (
                p['passengerId'],
                p['name'],
                p['nationalId'],
                p['dateOfBirth']
            ))
    conn.commit()

def insert_flights(conn):
    with conn.cursor() as cur:
        for f in flights:
            cur.execute("""
                INSERT INTO flights VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT (flight_id) DO NOTHING;
            """, (
                f['flightId'],
                f['plateNumber'],
                f['arrivalTime'],
                f['departureTime'],
                f['fuelConsumption'],
                f['occupiedSeats'],
                f['origin'],
                f['destination']
            ))

            # Insertar pasajeros del vuelo
            for pid, status in f.get('passengerIds', []):
                cur.execute("""
                    INSERT INTO flight_passengers VALUES (%s, %s, %s)
                    ON CONFLICT DO NOTHING;
                """, (
                    f['flightId'], pid, status
                ))
    conn.commit()

if __name__ == "__main__":
    conn = connect()
    create_tables(conn)
    insert_airplanes(conn)
    insert_passengers(conn)
    insert_flights(conn)
    conn.close()
    print("Datos insertados en RDS.")