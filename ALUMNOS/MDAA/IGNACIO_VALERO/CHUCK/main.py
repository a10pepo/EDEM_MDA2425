import re
import pymongo
import pg8000.native
from pymongo import MongoClient

# Conexión a PostgreSQL
conexion = pg8000.native.Connection(
    user="postgres",
    password="Welcome01",
    host="localhost"
)

# Conexión a MongoDB
cliente_mongo = MongoClient("mongodb://root:example@localhost:27017/")
basedatos = cliente_mongo["Chuck"]
coleccion = basedatos["Database_Chuck"]

# Crear tabla en PostgreSQL si no existe
sql_crear_tabla = """
CREATE TABLE IF NOT EXISTS chuck (
    palabras VARCHAR(50) NOT NULL,
    tiempo TIMESTAMP NOT NULL
)
"""
conexion.run(sql_crear_tabla)

# Extraer y limpiar textos de MongoDB
chistes_limpios = []

for doc in coleccion.find():
    texto = doc.get("value")
    if texto:
        texto_sin_signos = re.sub(r"[^\w\s]", "", texto)
        chistes_limpios.append(texto_sin_signos)

# Insertar palabras individualmente en PostgreSQL
for chiste in chistes_limpios:
    palabras = chiste.split()
    for palabra in palabras:
        consulta = f"INSERT INTO chuck(palabras, tiempo) VALUES ('{palabra}', now())"
        conexion.run(consulta)
        print(palabra)
