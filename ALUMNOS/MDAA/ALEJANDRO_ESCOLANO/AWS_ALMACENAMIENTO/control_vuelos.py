from initial_info import flights as vuelos, passengers as viajeros, airplanes as aviones
from datetime import datetime as dt
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

def pg_conexion():
    return psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        user=PG_USER,
        password=PG_PASS,
        database=PG_DB
    )

def mostrar_lista(obj):
    if isinstance(obj, list):
        for elem in obj:
            for k, v in elem.items():
                if isinstance(v, list):
                    print(f"{k}:")
                    for sub in v:
                        print(f"  {sub}")
                else:
                    print(f"{k}: {v}")

def datos_vuelos():
    mostrar_lista(vuelos)
    mostrar_lista(viajeros)
    mostrar_lista(aviones)

def alta_objeto():
    tipo = input("Registrar avion, vuelo o viajero: ")
    if tipo == "viajero":
        nuevo_viajero()
    elif tipo == "avion":
        nuevo_avion()
    elif tipo == "vuelo":
        nuevo_vuelo()
    else:
        print("Tipo no válido. Usa 'viajero', 'avion' o 'vuelo'.")

def nuevo_vuelo():
    vuelo = {
        "flightId": input("ID Vuelo: "),
        "plateNumber": input("Matrícula: "),
        "arrivalTime": input("Llegada (YYYY-MM-DDTHH:MM:SS): "),
        "departureTime": input("Salida (YYYY-MM-DDTHH:MM:SS): "),
        "fuelConsumption": int(input("Consumo: ")),
        "occupiedSeats": int(input("Ocupados: ")),
        "origin": input("Origen: "),
        "destination": input("Destino: "),
        "passengerIds": []
    }
    n = int(input("Nº pasajeros: "))
    for _ in range(n):
        pid = input("ID pasajero: ")
        st = input("Estado (Boarded/Cancelled): ")
        vuelo["passengerIds"].append((pid, st))
    vuelos.append(vuelo)
    print(f"Vuelo {vuelo['flightId']} registrado.")

def nuevo_avion():
    avion = {
        "plateNumber": input("Matrícula: "),
        "type": input("Tipo: "),
        "lastMaintenanceDate": input("Último mantenimiento (YYYY-MM-DD): "),
        "nextMaintenanceDate": input("Próximo mantenimiento (YYYY-MM-DD): "),
        "capacity": int(input("Capacidad: ")),
        "ownerId": input("ID Propietario: "),
        "ownerName": input("Propietario: "),
        "hangarId": input("Hangar: "),
        "fuel_capacity": int(input("Capacidad combustible: "))
    }
    aviones.append(avion)
    print(f"Avión {avion['plateNumber']} registrado.")

def nuevo_viajero():
    viajero = {
        "passengerId": input("ID Viajero: "),
        "name": input("Nombre: "),
        "nationalId": input("DNI: "),
        "dateOfBirth": input("Nacimiento (YYYY-MM-DD): ")
    }
    viajeros.append(viajero)
    print(f"Viajero {viajero['name']} registrado.")

def dias_mantenimiento(aviones):
    hoy = dt.today().date()
    for a in aviones:
        prox = dt.strptime(a["nextMaintenanceDate"], "%Y-%m-%d").date()
        print(f"Avión {a['plateNumber']} ({a['type']}): {(prox - hoy).days} días para mantenimiento.")

def asientos_libres(aviones, vuelos):
    for a in aviones:
        tot = a["capacity"]
        ocup = sum(v["occupiedSeats"] for v in vuelos if v["plateNumber"] == a["plateNumber"])
        print(f"Avión {a['plateNumber']} ({a['type']}): {tot - ocup} libres.")

def estado_embarque(vuelos):
    for v in vuelos:
        print(f"Vuelo {v['flightId']} ({v['origin']} - {v['destination']}):")
        for pid, st in v["passengerIds"]:
            print(f"  Pasajero {pid}: {st}")

def alerta_ocupacion(aviones, vuelos):
    for v in vuelos:
        a = next((x for x in aviones if x["plateNumber"] == v["plateNumber"]), None)
        if a:
            if v["occupiedSeats"] > 0.1 * a["capacity"]:
                logging.info(f"¡Alerta! Vuelo {v['flightId']} >10% asientos ocupados.")
            else:
                logging.info(f"Vuelo {v['flightId']} <10% asientos ocupados.")
        else:
            logging.warning(f"No existe avión {v['plateNumber']} para vuelo {v['flightId']}.")

def alerta_mantenimiento(aviones):
    hoy = dt.today().date()
    for a in aviones:
        prox = dt.strptime(a["nextMaintenanceDate"], "%Y-%m-%d").date()
        if (prox - hoy).days <= 100:
            logging.info(f"¡Alerta! Avión {a['plateNumber']} necesita mantenimiento <100 días.")

def alerta_combustible(aviones, vuelos):
    for v in vuelos:
        a = next((x for x in aviones if x["plateNumber"] == v["plateNumber"]), None)
        if a and v["fuelConsumption"] > 0.1 * a["fuel_capacity"]:
            logging.info(f"¡Alerta! Vuelo {v['flightId']} >10% consumo en avión {a['plateNumber']}.")
        else:
            logging.info(f"Vuelo {v['flightId']} <10% consumo en avión {v['plateNumber']}.")

def crear_db(conn):
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname='info_aeropuertos';")
    if not cur.fetchone():
        cur.execute("CREATE DATABASE info_aeropuertos;")

if __name__ == "__main__":
    datos_vuelos()
    alta_objeto()
    dias_mantenimiento(aviones)
    asientos_libres(aviones, vuelos)
    estado_embarque(vuelos)
    alerta_ocupacion(aviones, vuelos)
    alerta_mantenimiento(aviones)
    alerta_combustible(aviones, vuelos)