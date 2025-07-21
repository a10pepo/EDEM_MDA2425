import psycopg2
import pandas as pd

# Configuración PostgreSQL (origen)
POSTGRES_CONFIG = {
    'host': 'tu-rds-endpoint.amazonaws.com',
    'database': 'aviation_db',
    'user': 'postgres',
    'password': 'tu_password',
    'port': 5432
}

# Configuración Redshift (destino)
REDSHIFT_CONFIG = {
    'host': 'tu-redshift-cluster.amazonaws.com',
    'database': 'dev',
    'user': 'awsuser',
    'password': 'tu_password',
    'port': 5439
}

def extract_from_postgres():
    """Extraer datos de PostgreSQL"""
    conn = psycopg2.connect(**POSTGRES_CONFIG)
    
    # Extraer todas las tablas
    airplanes_df = pd.read_sql("SELECT * FROM airplanes", conn)
    passengers_df = pd.read_sql("SELECT * FROM passengers", conn)
    flights_df = pd.read_sql("SELECT * FROM flights", conn)
    
    conn.close()
    return airplanes_df, passengers_df, flights_df

def load_to_redshift(airplanes_df, passengers_df, flights_df):
    """Cargar datos en Redshift"""
    conn = psycopg2.connect(**REDSHIFT_CONFIG)
    cur = conn.cursor()
    
    # Crear tablas en Redshift
    cur.execute("""
        CREATE TABLE IF NOT EXISTS airplanes (
            plate_number VARCHAR(20),
            type VARCHAR(100),
            capacity INTEGER,
            owner_name VARCHAR(100)
        );
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS passengers (
            passenger_id VARCHAR(20),
            name VARCHAR(100),
            national_id VARCHAR(20)
        );
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS flights (
            flight_id VARCHAR(20),
            plate_number VARCHAR(20),
            origin VARCHAR(100),
            destination VARCHAR(100),
            occupied_seats INTEGER
        );
    """)
    
    # Limpiar tablas
    cur.execute("TRUNCATE airplanes, passengers, flights;")
    
    # Insertar datos
    for _, row in airplanes_df.iterrows():
        cur.execute("""
            INSERT INTO airplanes VALUES (%s, %s, %s, %s)
        """, tuple(row))
    
    for _, row in passengers_df.iterrows():
        cur.execute("""
            INSERT INTO passengers VALUES (%s, %s, %s)
        """, tuple(row))
    
    for _, row in flights_df.iterrows():
        cur.execute("""
            INSERT INTO flights VALUES (%s, %s, %s, %s, %s)
        """, tuple(row))
    
    conn.commit()
    cur.close()
    conn.close()

def main():
    try:
        print("Extrayendo datos de PostgreSQL...")
        airplanes_df, passengers_df, flights_df = extract_from_postgres()
        
        print("Cargando datos en Redshift...")
        load_to_redshift(airplanes_df, passengers_df, flights_df)
        
        print("¡EL a Redshift completado!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()