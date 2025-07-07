from initial_info import flights, passengers, airplanes
from datetime import datetime
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

def show_objects(obj):
    if isinstance(obj, list):
        for item in obj:
            for key, value in item.items():
                if isinstance(value, list):
                    print(f"{key}:")
                    for sub_item in value:
                        print(f"  {sub_item}")
                else:
                    print(f"{key}: {value}")
        

def fligts_data():
    show_objects(flights)
    show_objects(passengers)
    show_objects(airplanes)


def register_passenge_objr():

    obj=input("Register airplane, fligt or passenger: ")
    if obj == "passenger":
        input_passenger_info()
    elif obj == "airplane":
        input_airplane_info()
    elif obj == "flight":
        input_flight_info()
    else:
        print("Invalid object type. Please enter 'passenger', 'airplane', or 'flight'.")

def input_flight_info():
    flight = {
            "flightId": input("Flight ID: "),
            "plateNumber": input("Plate Number: "),
            "arrivalTime": input("Arrival Time (YYYY-MM-DDTHH:MM:SS): "),
            "departureTime": input("Departure Time (YYYY-MM-DDTHH:MM:SS): "),
            "fuelConsumption": int(input("Fuel Consumption: ")),
            "occupiedSeats": int(input("Occupied Seats: ")),
            "origin": input("Origin: "),
            "destination": input("Destination: "),
            "passengerIds": []
        }
    num_passengers = int(input("Number of passengers: "))
    for _ in range(num_passengers):
        passenger_id = input("Passenger ID: ")
        status = input("Status (Boarded/Cancelled): ")
        flight["passengerIds"].append((passenger_id, status))
    flights.append(flight)
    print(f"Flight {flight['flightId']} registered successfully.")

def input_airplane_info():
    airplane = {
            "plateNumber": input("Plate Number: "),
            "type": input("Type: "),
            "lastMaintenanceDate": input("Last Maintenance Date (YYYY-MM-DD): "),
            "nextMaintenanceDate": input("Next Maintenance Date (YYYY-MM-DD): "),
            "capacity": int(input("Capacity: ")),
            "ownerId": input("Owner ID: "),
            "ownerName": input("Owner Name: "),
            "hangarId": input("Hangar ID: "),
            "fuel_capacity": int(input("Fuel Capacity: "))
        }
    airplanes.append(airplane)
    print(f"Airplane {airplane['plateNumber']} registered successfully.")

def input_passenger_info():
    passenger = {
            "passengerId": input("Passenger ID: "),
            "name": input("Name: "),
            "nationalId": input("National ID: "),
            "dateOfBirth": input("Date of Birth (YYYY-MM-DD): ")
        }
    passengers.append(passenger)
    print(f"Passenger {passenger['name']} registered successfully.")


def days_until_next_maintenance(airplanes):
    days_until_next(airplanes)

def days_until_next(airplanes):
    today = datetime.today().date()
    for plane in airplanes:
        next_maintenance = datetime.strptime(plane["nextMaintenanceDate"], "%Y-%m-%d").date()
        days_left = (next_maintenance - today).days
        print(f"Avión {plane['plateNumber']} ({plane['type']}): {days_left} días hasta el próximo mantenimiento.")


def emty_seats(airplanes, flights):
    empty_seats(airplanes, flights)

def empty_seats(airplanes, flights):
    for plane in airplanes:
        total_seats = plane["capacity"]
        occupied_seats = sum(flight["occupiedSeats"] for flight in flights if flight["plateNumber"] == plane["plateNumber"])
        empty_seats = total_seats - occupied_seats
        print(f"Avión {plane['plateNumber']} ({plane['type']}): {empty_seats} asientos libres.")
    

def boarding_status(flights):
    boarding_status(flights)

def boarding_status(flights):
    for flight in flights:
        print(f"Vuelo {flight['flightId']} ({flight['origin']} - {flight['destination']}):")
        for passenger_id, status in flight["passengerIds"]:
            print(f"  Pasajero {passenger_id}: {status}")

def alert_seats(airplanes, flights):
    for flight in flights:
        plane = next((p for p in airplanes if p["plateNumber"] == flight["plateNumber"]), None)
        if plane:
            if flight["occupiedSeats"] > 0.1 * plane["capacity"]:
                logging.info(f"¡Alerta! El vuelo {flight['flightId']} tiene más del 10% de asientos ocupados.")
            else:
                logging.info(f"El vuelo {flight['flightId']} tiene menos del 10% de asientos ocupados.")
        else:
            logging.warning(f"No se encontró el avión con matrícula {flight['plateNumber']} para el vuelo {flight['flightId']}.")


def alert_maintenance(airplanes):
    today = datetime.today().date()
    for plane in airplanes:
        next_maintenance = datetime.strptime(plane["nextMaintenanceDate"], "%Y-%m-%d").date()
        if (next_maintenance - today).days <= 100:
            logging.info(f"¡Alerta! El avión {plane['plateNumber']} necesita mantenimiento en menos de 100 días.")

def alert_fuel(airplanes, flights):
    for flight in flights:
        plane = next((p for p in airplanes if p["plateNumber"] == flight["plateNumber"]), None)
        if plane and flight["fuelConsumption"] > 0.1 * plane["fuel_capacity"]:
            logging.info(f"¡Alerta! El vuelo {flight['flightId']} tiene un consumo mayor del 10% frente al total en el avion {plane['plateNumber']}.")
        else:
            logging.info(f"El vuelo {flight['flightId']} tiene un consumo de combustible menor del 10% en el avion {plane['plateNumber']}.")


def create_database(conn: psycopg2.connect) -> None:
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname='info_aeropuertos';")
    exists = cur.fetchone()
    if not exists:
        cur.execute("CREATE DATABASE info_aeropuertos;")



if __name__== "__main__":
    fligts_data()
    register_passenge_objr()
    days_until_next_maintenance(airplanes)
    emty_seats(airplanes, flights)
    boarding_status(flights)
    alert_seats(airplanes, flights)
    alert_maintenance(airplanes)
    alert_fuel(airplanes, flights)



