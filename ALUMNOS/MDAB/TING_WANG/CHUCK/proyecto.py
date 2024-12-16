from pymongo import MongoClient
import psycopg2

client = MongoClient('mongodb://root:example@localhost:27017')

db = client['CHUCKY']
collection = db['chistes']


conn_target = psycopg2.connect(
    dbname="CHUCKY",
    user="postgres",
    password="Welcome01",
    host="localhost",
    port="5432" 
)
cursor = conn_target.cursor()


crear_tabla = """
    CREATE TABLE IF NOT EXISTS jokes (
        value TEXT
    )
"""
cursor.execute(crear_tabla)
conn_target.commit()

resultado = collection.find()

for jokes in resultado:
    palabras = jokes["value"].split(" ")
    for palabra in palabras:
        insertar = """
        INSERT INTO jokes (value) 
        VALUES (%s)
        """   
        cursor.execute(insertar,(palabra,))

conn_target.commit()

cursor.close()
conn_target.close()

print("Datos insertados correctamente.")
