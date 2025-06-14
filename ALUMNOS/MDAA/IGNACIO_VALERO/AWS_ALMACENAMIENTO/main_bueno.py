import logging
import os
import psycopg2
import time
from initial_info import airplanes, flights, passengers
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

RDS_HOST = os.environ['RDS_HOST']
RDS_PORT = os.environ['RDS_PORT']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']

REDSHIFT_HOST = os.environ['REDSHIFT_HOST']
REDSHIFT_PORT = os.environ['REDSHIFT_PORT']
REDSHIFT_USER = os.environ['REDSHIFT_USER']
REDSHIFT_PASSWORD = os.environ['REDSHIFT_PASSWORD']
REDSHIFT_DB = os.environ['REDSHIFT_DB']

conn = psycopg2.connect(
    dbname=RDS_DB,
    user=RDS_USER,
    password=RDS_PASSWORD,
    host=RDS_HOST,
    port=RDS_PORT
)

def connect_to_redshift() -> psycopg2.connect:
    conn = psycopg2.connect(
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT,
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD,
        database=REDSHIFT_DB
    )
    return conn

def extract_data_from_postgres(conn: psycopg2.connect, table_name: str) -> None:
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name};")
    data = cur.fetchall()
    cur.close()
    return data

def extract_schema_and_type_from_postgres(conn: psycopg2.connect, table_name: str) -> list:
    cur = conn.cursor()
    cur.execute(f"""SELECT column_name, data_type
                    FROM information_schema.columns 
                    WHERE table_name = '{table_name}'
                    ORDER BY ordinal_position;""")
    data = cur.fetchall()
    cur.close()
    return data

def create_table_from_schema_in_aws_redshift(conn: psycopg2.connect, table_name: str, schema: list) -> None:
    cur = conn.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                {', '.join([f'{column[0]} {column[1]}' for column in schema])}
                );"""
    cur.execute(query)
    conn.commit()
    cur.close()

def insert_data_redshift(conn: psycopg2.connect, table_name: str, schema: list, data: tuple) -> None:
    cur = conn.cursor()
    columns = ', '.join([column[0] for column in schema])
    placeholders = ', '.join(['%s'] * len(data))
    query = f"""INSERT INTO {table_name} ({columns})
                VALUES ({placeholders});
            """
    cur.execute(query, data)
    conn.commit()
    cur.close()

def create_tables(conn):
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS airplanes (
        plateNumber VARCHAR(20) PRIMARY KEY,
        type VARCHAR(100),
        lastMaintenanceDate DATE,
        nextMaintenanceDate DATE,
        capacity INTEGER,
        ownerId VARCHAR(20),
        ownerName VARCHAR(100),
        hangarId VARCHAR(20),
        fuel_capacity INTEGER
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS passengers (
        passengerId VARCHAR(20) PRIMARY KEY,
        name VARCHAR(100),
        nationalId VARCHAR(20),
        dateOfBirth DATE
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS flights (
        flightId VARCHAR(30) PRIMARY KEY,
        plateNumber VARCHAR(20) REFERENCES airplanes(plateNumber),
        arrivalTime TIMESTAMP,
        departureTime TIMESTAMP,
        fuelConsumption INTEGER,
        occupiedSeats INTEGER,
        origin VARCHAR(100),
        destination VARCHAR(100)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS flight_passengers (
        flightId VARCHAR(30) REFERENCES flights(flightId),
        passengerId VARCHAR(20) REFERENCES passengers(passengerId),
        status VARCHAR(20),
        PRIMARY KEY (flightId, passengerId)
    );
    """)
    cur.close()

def insert_data(conn, airplanes, flights, passengers):
    cur = conn.cursor()

    for a in airplanes:
        cur.execute("""
            INSERT INTO airplanes (plateNumber, type, lastMaintenanceDate, nextMaintenanceDate, capacity, ownerId, ownerName, hangarId, fuel_capacity)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (plateNumber) DO UPDATE SET
                type = EXCLUDED.type,
                lastMaintenanceDate = EXCLUDED.lastMaintenanceDate,
                nextMaintenanceDate = EXCLUDED.nextMaintenanceDate,
                capacity = EXCLUDED.capacity,
                ownerId = EXCLUDED.ownerId,
                ownerName = EXCLUDED.ownerName,
                hangarId = EXCLUDED.hangarId,
                fuel_capacity = EXCLUDED.fuel_capacity;
        """, (
            a["plateNumber"],
            a["type"],
            a["lastMaintenanceDate"],
            a["nextMaintenanceDate"],
            a["capacity"],
            a["ownerId"],
            a["ownerName"],
            a["hangarId"],
            a["fuel_capacity"]
        ))

    for p in passengers:
        cur.execute("""
            INSERT INTO passengers (passengerId, name, nationalId, dateOfBirth)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (passengerId) DO UPDATE SET
                name = EXCLUDED.name,
                nationalId = EXCLUDED.nationalId,
                dateOfBirth = EXCLUDED.dateOfBirth;
        """, (
            p["passengerId"],
            p["name"],
            p["nationalId"],
            p["dateOfBirth"]
        ))

    for f in flights:
        cur.execute("""
            INSERT INTO flights (flightId, plateNumber, arrivalTime, departureTime, fuelConsumption, occupiedSeats, origin, destination)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (flightId) DO UPDATE SET
                plateNumber = EXCLUDED.plateNumber,
                arrivalTime = EXCLUDED.arrivalTime,
                departureTime = EXCLUDED.departureTime,
                fuelConsumption = EXCLUDED.fuelConsumption,
                occupiedSeats = EXCLUDED.occupiedSeats,
                origin = EXCLUDED.origin,
                destination = EXCLUDED.destination;
        """, (
            f["flightId"],
            f["plateNumber"],
            f["arrivalTime"],
            f["departureTime"],
            f["fuelConsumption"],
            f["occupiedSeats"],
            f["origin"],
            f["destination"]
        ))

        for pid, status in f["passengerIds"]:
            cur.execute("""
                INSERT INTO flight_passengers (flightId, passengerId, status)
                VALUES (%s, %s, %s)
                ON CONFLICT (flightId, passengerId) DO UPDATE SET
                    status = EXCLUDED.status;
            """, (
                f["flightId"],
                pid,
                status
            ))

    conn.commit()
    cur.close()

def ver_aviones_en_hangares():
    print("📦 Aviones en hangares:")
    cur = conn.cursor()
    cur.execute("""
        SELECT plateNumber, type, hangarId, ownerName
        FROM airplanes;
    """)
    aviones = cur.fetchall()
    for avion in aviones:
        plateNumber, type_, hangarId, ownerName = avion
        print(f"  - Matrícula: {plateNumber}, Tipo: {type_}, Hangar: {hangarId}, Propietario: {ownerName}")
    cur.close()
    time.sleep(1)

def ver_vuelos_que_han_aterrizado():
    print("\n🛬 Vuelos que han aterrizado:")
    cur = conn.cursor()
    cur.execute("""
        SELECT flightId, origin, destination, arrivalTime, plateNumber
        FROM flights
        WHERE arrivalTime IS NOT NULL;
    """)
    vuelos = cur.fetchall()
    for vuelo in vuelos:
        flightId, origin, destination, arrivalTime, plateNumber = vuelo
        print(f"  - ID Vuelo: {flightId}, Origen: {origin}, Destino: {destination}, Llegada: {arrivalTime}, Avión: {plateNumber}")
    cur.close()
    time.sleep(1)

def ver_pasajeros_que_han_llegado():
    print("\n👤 Pasajeros que han llegado al aeródromo:")
    cur = conn.cursor()
    # Obtener pasajeros con estado 'Boarded'
    cur.execute("""
        SELECT DISTINCT fp.passengerId
        FROM flight_passengers fp
        WHERE fp.status = 'Boarded';
    """)
    pasajeros_llegados_ids = {row[0] for row in cur.fetchall()}

    if not pasajeros_llegados_ids:
        print("  - No hay pasajeros que hayan llegado.")
        cur.close()
        time.sleep(1)
        return

    format_ids = ','.join(["%s"] * len(pasajeros_llegados_ids))
    query = f"""
        SELECT passengerId, name
        FROM passengers
        WHERE passengerId IN ({format_ids});
    """
    cur.execute(query, tuple(pasajeros_llegados_ids))
    pasajeros = cur.fetchall()

    for pasajero in pasajeros:
        passengerId, name = pasajero
        print(f"  - {name} (ID: {passengerId})")
    cur.close()
    time.sleep(1)

def registrar_avion():
    print("\n✈️ Registrar un nuevo avión en un hangar:")
    avion = {
        "plateNumber": input("Matrícula: "),
        "type": input("Tipo de avión: "),
        "lastMaintenanceDate": input("Fecha última mant. (YYYY-MM-DD): "),
        "nextMaintenanceDate": input("Fecha próxima mant. (YYYY-MM-DD): "),
        "capacity": int(input("Capacidad: ")),
        "ownerId": input("ID del propietario: "),
        "ownerName": input("Nombre del propietario: "),
        "hangarId": input("ID del hangar: "),
        "fuel_capacity": int(input("Capacidad de combustible (L): "))
    }

    airplanes.append(avion)

    cur = conn.cursor()
    cur.execute("""
        INSERT INTO airplanes (plateNumber, type, lastMaintenanceDate, nextMaintenanceDate, capacity, ownerId, ownerName, hangarId, fuel_capacity)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (plateNumber) DO UPDATE SET
            type = EXCLUDED.type,
            lastMaintenanceDate = EXCLUDED.lastMaintenanceDate,
            nextMaintenanceDate = EXCLUDED.nextMaintenanceDate,
            capacity = EXCLUDED.capacity,
            ownerId = EXCLUDED.ownerId,
            ownerName = EXCLUDED.ownerName,
            hangarId = EXCLUDED.hangarId,
            fuel_capacity = EXCLUDED.fuel_capacity;
    """, (
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
    cur.close()

    print("✅ Avión registrado correctamente.")

def registrar_vuelo():
    print("\n🛬 Registrar un nuevo vuelo:")
    vuelo = {
        "flightId": input("ID del vuelo: "),
        "plateNumber": input("Matrícula del avión: "),
        "arrivalTime": input("Hora de llegada (YYYY-MM-DDTHH:MM:SS): "),
        "departureTime": input("Hora de salida (YYYY-MM-DDTHH:MM:SS): "),
        "fuelConsumption": int(input("Consumo de combustible (L): ")),
        "occupiedSeats": int(input("Asientos ocupados: ")),
        "origin": input("Origen: "),
        "destination": input("Destino: "),
        "passengerIds": []
    }

    num_pasajeros = int(input("¿Cuántos pasajeros? "))
    for _ in range(num_pasajeros):
        pid = input("  - ID del pasajero: ")
        estado = input("    Estado ('Boarded' o 'Cancelled'): ")
        vuelo["passengerIds"].append((pid, estado))

    flights.append(vuelo)

    cur = conn.cursor()
    cur.execute("""
        INSERT INTO flights (flightId, plateNumber, arrivalTime, departureTime, fuelConsumption, occupiedSeats, origin, destination)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (flightId) DO UPDATE SET
            plateNumber = EXCLUDED.plateNumber,
            arrivalTime = EXCLUDED.arrivalTime,
            departureTime = EXCLUDED.departureTime,
            fuelConsumption = EXCLUDED.fuelConsumption,
            occupiedSeats = EXCLUDED.occupiedSeats,
            origin = EXCLUDED.origin,
            destination = EXCLUDED.destination;
    """, (
        vuelo["flightId"],
        vuelo["plateNumber"],
        vuelo["arrivalTime"],
        vuelo["departureTime"],
        vuelo["fuelConsumption"],
        vuelo["occupiedSeats"],
        vuelo["origin"],
        vuelo["destination"]
    ))

    for pid, status in vuelo["passengerIds"]:
        cur.execute("""
            INSERT INTO flight_passengers (flightId, passengerId, status)
            VALUES (%s, %s, %s)
            ON CONFLICT (flightId, passengerId) DO UPDATE SET
                status = EXCLUDED.status;
        """, (
            vuelo["flightId"],
            pid,
            status
        ))

    conn.commit()
    cur.close()

    print("✅ Vuelo registrado correctamente.")

def main():
    print("\nBienvenido al sistema del aeródromo\n")
    while True:
        print("""
        1. Ver aviones en hangares
        2. Ver vuelos que han aterrizado
        3. Ver pasajeros que han llegado
        4. Registrar un avión nuevo
        5. Registrar un vuelo nuevo
        6. Salir
        """)
        choice = input("Elige una opción: ")
        if choice == "1":
            ver_aviones_en_hangares()
        elif choice == "2":
            ver_vuelos_que_han_aterrizado()
        elif choice == "3":
            ver_pasajeros_que_han_llegado()
        elif choice == "4":
            registrar_avion()
        elif choice == "5":
            registrar_vuelo()
        elif choice == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    # create_tables(conn)
    # insert_data(conn, airplanes, flights, passengers)
    main()


#Si le paso argumentos puedo hacer que se ejecute directamente el script segun sea DLH o DWH