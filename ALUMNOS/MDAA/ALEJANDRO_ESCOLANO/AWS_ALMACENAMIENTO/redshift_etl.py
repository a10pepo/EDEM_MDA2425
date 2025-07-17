import logging
import os
from datetime import datetime as dt
from initial_info import flights as vuelos, passengers as viajeros, airplanes as aviones
import psycopg2
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv()

PG_HOST = os.environ['RDS_HOST']
PG_PORT = os.environ['RDS_PORT']
PG_USER = os.environ['RDS_USER']
PG_PASS = os.environ['RDS_PASSWORD']
PG_DB = os.environ['RDS_DB']

RS_HOST = os.environ['REDSHIFT_HOST']
RS_PORT = os.environ['REDSHIFT_PORT']
RS_USER = os.environ['REDSHIFT_USER']
RS_PASS = os.environ['REDSHIFT_PASSWORD']
RS_DB = os.environ['REDSHIFT_DB']

def conexion_pg():
    return psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        user=PG_USER,
        password=PG_PASS,
        database=PG_DB
    )

def conexion_rs():
    return psycopg2.connect(
        host=RS_HOST,
        port=RS_PORT,
        user=RS_USER,
        password=RS_PASS,
        database=RS_DB
    )

def crear_db(conn):
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname='info_aeropuertos';")
    if not cur.fetchone():
        cur.execute("CREATE DATABASE info_aeropuertos;")

def extraer_tabla(conn, tabla):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {tabla};")
    return cur.fetchall()

def extraer_schema(conn, tabla):
    cur = conn.cursor()
    cur.execute(f"""SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{tabla}' ORDER BY ordinal_position;""")
    return cur.fetchall()

def crear_tabla_rs(conn, tabla, schema):
    cur = conn.cursor()
    q = f"""CREATE TABLE IF NOT EXISTS {tabla} ({', '.join([f'{col[0]} {col[1]}' for col in schema])});"""
    cur.execute(q)
    conn.commit()

def insertar_rs(conn, tabla, schema, fila):
    cur = conn.cursor()
    cols = ', '.join([col[0] for col in schema])
    vals = ', '.join(['%s'] * len(fila))
    q = f"""INSERT INTO {tabla} ({cols}) VALUES ({vals});"""
    cur.execute(q, fila)
    conn.commit()

if __name__ == "__main__":
    tabla_pg = 'airplane'
    logging.info("Conectando a RDS")
    cpg = conexion_pg()
    crs = conexion_rs()
    logging.info("Conectado a RDS")
    logging.info("Extrayendo datos de postgres")
    filas = extraer_tabla(cpg, tabla_pg)
    print(filas)
    logging.info("Datos extraídos")
    logging.info("Extrayendo esquema de postgres")
    esquema = extraer_schema(cpg, tabla_pg)
    print(esquema)
    logging.info("Esquema extraído")
    logging.info("Creando tabla en redshift")
    crear_tabla_rs(crs, tabla_pg, esquema)
    logging.info("Tabla creada")
    logging.info("Insertando datos en redshift")
    for f in filas:
        insertar_rs(crs, tabla_pg, esquema, f)
        logging.info("Dato insertado")
    cpg.close()
    crs.close()