from pymongo import MongoClient
import psycopg2

client = MongoClient('mongodb://root:example@localhost:27017')

db = client['CHUCKY']
collection = db['chistes']


conn = psycopg2.connect(
    dbname="CHUCKY",
    user="postgres",
    password="Welcome01",
    host="localhost",
    port="5432" 
)
cursor = conn.cursor()

crear_tabla = """
    CREATE TABLE IF NOT EXISTS jokes (
        id SERIAL PRIMARY KEY,
        value TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""
cursor.execute(crear_tabla)
conn.commit()

resultado = collection.find()

for jokes in resultado:
    palabras = jokes["value"].split(" ")
    for palabra in palabras:
        insertar = f"INSERT INTO jokes (id, value, created_at) VALUES (%s, %s)"
        datos = (jokes{_id}, jokes{value}, jokes{current_date})
