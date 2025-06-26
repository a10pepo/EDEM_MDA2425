import os
import random
import string
import time
import logging
from datetime import datetime, timedelta

from faker import Faker
import pandas as pd
import psycopg2
from dotenv import load_dotenv

# Configuración
fake = Faker('es_ES')
logging.basicConfig(level=logging.INFO)
load_dotenv()

RDS_HOST = os.environ['RDS_HOST']
RDS_PORT = os.environ['RDS_PORT']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']

# Datos en memoria
airplanes, flights, passengers = [], [], []

# Funciones de generación
def random_plate():
    return f"EC-{''.join(random.choices(string.ascii_uppercase, k=3))}{random.randint(1, 9)}"

def generate_airplane(index):
    types = ["Cessna 208 Caravan", "Piper PA-31 Navajo", "Beechcraft King Air", "Diamond DA42", "Pilatus PC-12"]
    owners = [("O-54321", "Andalucía Air"), ("O-67890", "Ibiza Sky Club"), ("O-98765", "Basque Flyers")]
    type_ = random.choice(types)
    ownerId, ownerName = random.choice(owners)
    maintenance_date = fake.date_between(start_date='-2y', end_date='today')
    next_maintenance_date = maintenance_date + timedelta(days=365 * 2)
    airplanes.append({
        "plateNumber": random_plate(),
        "type": type_,
        "lastMaintenanceDate": str(maintenance_date),
        "nextMaintenanceDate": str(next_maintenance_date),
        "capacity": random.randint(6, 12),
        "ownerId": ownerId,
        "ownerName": ownerName,
        "hangarId": f"H-{random.randint(1, 5):02}",
        "fuel_capacity": random.randint(600, 1200)
    })

def generate_passenger(index):
    name = fake.name()
    nationalId = ''.join(random.choices(string.digits, k=8)) + random.choice(string.ascii_uppercase)
    dob = fake.date_of_birth(minimum_age=18, maximum_age=75)
    passengers.append({
        "passengerId": f"P-{1020 + index + 1}",
        "name": name,
        "nationalId": nationalId,
        "dateOfBirth": str(dob)
    })

def generate_flight(index):
    if not airplanes or not passengers:
        return
    flight_id = f"FL-2025-{str(index + 3).zfill(3)}"
    airplane = random.choice(airplanes)
    capacity = airplane['capacity']
    plate = airplane['plateNumber']
    dep_date = fake.date_time_between(start_date='now', end_date='+30d')
    arr_date = dep_date + timedelta(hours=random.randint(1, 5))
    origin, destination = fake.city(), fake.city()
    while destination == origin:
        destination = fake.city()
    selected_passengers = random.sample(passengers, k=min(random.randint(3, capacity), len(passengers)))
    passenger_ids = [(p["passengerId"], random.choice(['Boarded', 'Cancelled'])) for p in selected_passengers]
    flights.append({
        "flightId": flight_id,
        "plateNumber": plate,
        "arrivalTime": arr_date.isoformat(),
        "departureTime": dep_date.isoformat(),
        "fuelConsumption": random.randint(200, 1000),
        "occupiedSeats": sum(1 for _, status in passenger_ids if status == 'Boarded'),
        "origin": origin,
        "destination": destination,
        "passengerIds": passenger_ids
    })

# PostgreSQL
def connect_to_postgres_rds():
    return psycopg2.connect(
        host=RDS_HOST,
        port=RDS_PORT,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB
    )

def create_tables(conn):
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS passengers (
            passenger_id VARCHAR PRIMARY KEY,
            name VARCHAR,
            date_of_birth DATE,
            national_id VARCHAR
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS flights (
            flight_id VARCHAR PRIMARY KEY,
            arrival_time TIMESTAMP,
            departure_time TIMESTAMP,
            arrival_status VARCHAR,
            departure_status VARCHAR,
            plane_id VARCHAR,
            days_to_mainteinance INTEGER,
            weight_free_seats FLOAT,
            weight_remaining_consumption FLOAT,
            hangar_id VARCHAR
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS flight_passengers (
            flight_id VARCHAR REFERENCES flights(flight_id),
            passenger_id VARCHAR REFERENCES passengers(passenger_id),
            passenger_status VARCHAR,
            PRIMARY KEY (flight_id, passenger_id)
        );
    """)

def insert_dataframe(conn, df: pd.DataFrame, table_name: str):
    cur = conn.cursor()
    cols = ",".join(df.columns)
    values = ",".join(["%s"] * len(df.columns))
    insert_query = f"INSERT INTO {table_name} ({cols}) VALUES ({values}) ON CONFLICT DO NOTHING;"
    for row in df.itertuples(index=False, name=None):
        cur.execute(insert_query, row)
    conn.commit()

# Main
if __name__ == "__main__":
    sequence = ["P", "P", "A", "P", "P", "A", "V"]
    i = 0

    logging.info("⏳ Iniciando simulación y carga...")

    try:
        while True:
            tipo = sequence[i % len(sequence)]
            if tipo == "P":
                generate_passenger(i)
            elif tipo == "A":
                generate_airplane(i)
            elif tipo == "V":
                generate_flight(i)
            
            i += 1
            time.sleep(5)

            # Preparar DataFrames
            df_airplanes = pd.DataFrame(airplanes)
            df_flights = pd.DataFrame(flights)
            df_passengers = pd.DataFrame(passengers)
            if df_flights.empty:
                continue

            df_passengers.set_index("passengerId", inplace=True)

            flight_passenger_rows = []
            for _, row in df_flights.iterrows():
                for pid, status in row['passengerIds']:
                    p = df_passengers.loc[pid]
                    flight_passenger_rows.append({
                        "flight_id": row["flightId"],
                        "passenger_id": pid,
                        "passenger_status": status,
                        "name": p["name"],
                        "date_of_birth": p["dateOfBirth"],
                        "national_id": p["nationalId"]
                    })

            df_flight_passengers = pd.DataFrame(flight_passenger_rows)
            df_flight_info = df_flights.merge(df_airplanes, on="plateNumber", suffixes=("", "_plane"))

            now = datetime.now()
            df_flight_info["departure_time_dt"] = pd.to_datetime(df_flight_info["departureTime"])
            df_flight_info["arrival_time_dt"] = pd.to_datetime(df_flight_info["arrivalTime"])
            df_flight_info["next_maintenance_dt"] = pd.to_datetime(df_flight_info["nextMaintenanceDate"])
            df_flight_info["days_to_mainteinance"] = (df_flight_info["next_maintenance_dt"] - now).dt.days
            df_flight_info["departure_status"] = df_flight_info["departure_time_dt"].apply(lambda x: "departed" if x < now else "not departed")
            df_flight_info["arrival_status"] = df_flight_info["arrival_time_dt"].apply(lambda x: "landed" if x < now else "not landed")
            df_flight_info["weight_free_seats"] = (1 - (df_flight_info["occupiedSeats"] / df_flight_info["capacity"])).round(2)
            df_flight_info["weight_remaining_consumption"] = (1 - (df_flight_info["fuelConsumption"] / df_flight_info["fuel_capacity"])).round(2)

            df_flights_sql = df_flight_info[[
                "flightId", "arrival_status", "departure_status", "plateNumber", 
                "days_to_mainteinance", "weight_free_seats", "weight_remaining_consumption", "hangarId", 
                "arrival_time_dt", "departure_time_dt"
            ]].rename(columns={
                "flightId": "flight_id",
                "plateNumber": "plane_id",
                "hangarId": "hangar_id",
                "arrival_time_dt": "arrival_time",
                "departure_time_dt": "departure_time"
            })

            df_passengers_sql = df_passengers.reset_index().rename(columns={
                "passengerId": "passenger_id",
                "dateOfBirth": "date_of_birth",
                "nationalId": "national_id"
            })

            df_flight_passengers_sql = df_flight_passengers[[
                "flight_id", "passenger_id", "passenger_status"
            ]]

            # Guardar en PostgreSQL
            conn = connect_to_postgres_rds()
            create_tables(conn)
            insert_dataframe(conn, df_passengers_sql, "passengers")
            insert_dataframe(conn, df_flights_sql, "flights")
            insert_dataframe(conn, df_flight_passengers_sql, "flight_passengers")
            conn.close()

            logging.info("✅ Datos actualizados en RDS.")
            time.sleep(10)

    except KeyboardInterrupt:
        logging.warning("🛑 Proceso detenido manualmente.")
