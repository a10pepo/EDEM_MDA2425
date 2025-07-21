import psycopg2
from initial_info import airplanes, flights, passengers

# Configuración de conexión (cambiar por tu RDS)
DB_CONFIG = {
    'host': 'tu-rds-endpoint.amazonaws.com',
    'database': 'aviation_db',
    'user': 'postgres',
    'password': 'tu_password',
    'port': 5432
}

def connect_db():
    return psycopg2.connect(**DB_CONFIG)

def create_tables():
    conn = connect_db()
    cur = conn.cursor()
    
    with open('schema.sql', 'r') as f:
        cur.execute(f.read())
    
    conn.commit()
    cur.close()
    conn.close()
    print("Tablas creadas")

def insert_data():
    conn = connect_db()
    cur = conn.cursor()
    
    # Insertar aviones
    for airplane in airplanes:
        cur.execute("""
            INSERT INTO airplanes (plate_number, type, capacity, owner_name) 
            VALUES (%s, %s, %s, %s)
        """, (airplane['plateNumber'], airplane['type'], airplane['capacity'], airplane['ownerName']))
    
    # Insertar pasajeros
    for passenger in passengers:
        cur.execute("""
            INSERT INTO passengers (passenger_id, name, national_id) 
            VALUES (%s, %s, %s)
        """, (passenger['passengerId'], passenger['name'], passenger['nationalId']))
    
    # Insertar vuelos
    for flight in flights:
        cur.execute("""
            INSERT INTO flights (flight_id, plate_number, origin, destination, occupied_seats) 
            VALUES (%s, %s, %s, %s, %s)
        """, (flight['flightId'], flight['plateNumber'], flight['origin'], flight['destination'], flight['occupiedSeats']))
    
    conn.commit()
    cur.close()
    conn.close()
    print("Datos insertados")

def main():
    try:
        create_tables()
        insert_data()
        print("¡End-to-end completado!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()