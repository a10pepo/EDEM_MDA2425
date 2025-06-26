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

RDS_HOST = "default-workgroup.087016008104.eu-north-1.redshift-serverless.amazonaws.com"
RDS_PORT = 5439
RDS_USER = "admin"
RDS_PASSWORD = "Edem2425"
RDS_DB = "dev"

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

def create_analytics_table(conn):
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS flight_analytics (
            flight_id VARCHAR,
            passenger_id VARCHAR,
            passenger_status VARCHAR,
            arrival_status VARCHAR,
            arrival_time TIMESTAMP,
            departure_status VARCHAR,
            departure_time TIMESTAMP,
            plane_id VARCHAR,
            days_to_mainteinance INTEGER,
            weight_free_seats FLOAT,
            weight_remaining_consumption FLOAT,
            hangar_id VARCHAR,
            passenger_name VARCHAR,
            passenger_date_of_birth DATE,
            passenger_national_id VARCHAR,
            PRIMARY KEY (flight_id, passenger_id)
        );
    """)

def insert_analytics_dataframe(conn, df: pd.DataFrame):
    cur = conn.cursor()
    cols = ",".join(df.columns)
    values = ",".join(["%s"] * len(df.columns))
    insert_query = f"INSERT INTO flight_analytics ({cols}) VALUES ({values});"
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

            if not flights:
                continue

            df_airplanes = pd.DataFrame(airplanes)
            df_flights = pd.DataFrame(flights)
            df_passengers = pd.DataFrame(passengers)

            df_passengers.set_index("passengerId", inplace=True)

            now = datetime.now()
            records = []

            for _, row in df_flights.iterrows():
                plane_info = df_airplanes[df_airplanes["plateNumber"] == row["plateNumber"]].iloc[0]

                departure_time = pd.to_datetime(row["departureTime"])
                arrival_time = pd.to_datetime(row["arrivalTime"])

                days_to_mainteinance = (pd.to_datetime(plane_info["nextMaintenanceDate"]) - now).days
                departure_status = "departed" if departure_time < now else "not departed"
                arrival_status = "landed" if arrival_time < now else "not landed"
                weight_free_seats = round(1 - (row["occupiedSeats"] / plane_info["capacity"]), 2)
                weight_remaining_consumption = round(1 - (row["fuelConsumption"] / plane_info["fuel_capacity"]), 2)

                for pid, status in row["passengerIds"]:
                    passenger = df_passengers.loc[pid]
                    records.append({
                        "flight_id": row["flightId"],
                        "passenger_id": pid,
                        "passenger_status": status,
                        "arrival_status": arrival_status,
                        "arrival_time": arrival_time,
                        "departure_status": departure_status,
                        "departure_time": departure_time,
                        "plane_id": row["plateNumber"],
                        "days_to_mainteinance": days_to_mainteinance,
                        "weight_free_seats": weight_free_seats,
                        "weight_remaining_consumption": weight_remaining_consumption,
                        "hangar_id": plane_info["hangarId"],
                        "passenger_name": passenger["name"],
                        "passenger_date_of_birth": passenger["dateOfBirth"],
                        "passenger_national_id": passenger["nationalId"]
                    })

            df_flight_analytics = pd.DataFrame(records)

            # Guardar en PostgreSQL
            conn = connect_to_postgres_rds()
            create_analytics_table(conn)
            insert_analytics_dataframe(conn, df_flight_analytics)
            conn.close()

            logging.info("✅ Datos actualizados en Redshift.")
            time.sleep(10)

    except KeyboardInterrupt:
        logging.warning("🛑 Proceso detenido manualmente.")
