from pymongo import MongoClient
import psycopg2

# Conexión a MongoDB (usa la base de datos 'chuck' y la colección 'chistes')
mongo_client = MongoClient('mongodb://root:example@localhost:27017')
mongo_db = mongo_client['chuck']
mongo_collection = mongo_db['chistes']

# Conexión a PostgreSQL (usa el dbname que se infiere de docker-compose, en este caso 'postgres')
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Welcome01",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Crear la tabla 'jokes' si no existe, con 'value' como VARCHAR y 'created_at' como TIMESTAMP
crear_tabla = """
CREATE TABLE IF NOT EXISTS jokes (
    value VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
cur.execute(crear_tabla)
conn.commit()

# Recuperar los documentos de la colección 'chistes'
resultado = mongo_collection.find()

# Por cada documento, insertar cada palabra del campo "value" en la tabla 'jokes'
for chiste in resultado:
    if "value" in chiste:
        palabras = chiste["value"].split()
        for palabra in palabras:
            insertar = """
            INSERT INTO jokes (value) 
            VALUES (%s);
            """
            cur.execute(insertar, (palabra,))

conn.commit()
cur.close()
conn.close()

print("Datos insertados correctamente.")
