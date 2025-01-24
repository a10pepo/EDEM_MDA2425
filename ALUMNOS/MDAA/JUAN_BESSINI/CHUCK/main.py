import pymongo
import psycopg2
import re
from datetime import datetime

# Conexión a MongoDB
#myclient = pymongo.MongoClient("mongodb://root:example@localhost:27017/")
myclient = pymongo.MongoClient("mongodb://root:example@mongo:27017/")
mydb = myclient["chucknorris"]  # Base de datos
mycol = mydb["jokes"]           # Colección

# Conexión a PostgreSQL
pg_conn = psycopg2.connect(
    #host="localhost",
    host="postgres",
    database="chucknorris_sql",
    user="postgres",
    password="example"
)
pg_cursor = pg_conn.cursor()

# Crear tabla en PostgreSQL si no existe
pg_cursor.execute("""
CREATE TABLE IF NOT EXISTS palabras_chistes (
    palabra TEXT,
    hora_insercion TIMESTAMP
);
""")
pg_conn.commit()

# Consulta para buscar todos los chistes en MongoDB
myquery = {}  # Consulta vacía: obtendrá todos los documentos
mydoc = mycol.find(myquery)

# Procesar cada chiste
for chiste in mydoc:
    texto = chiste.get("value", "")  # Obtener el texto del chiste
    palabras = re.findall(r'\b\w+\b', texto)  # Dividir el texto en palabras

    # Insertar cada palabra en PostgreSQL
    for palabra in palabras:
        hora_insercion = datetime.now()  # Hora actual
        pg_cursor.execute("""
            INSERT INTO palabras_chistes (palabra, hora_insercion)
            VALUES (%s, %s);
        """, (palabra, hora_insercion))
        print(f"Insertada palabra: {palabra} a las {hora_insercion}")

# Confirmar los cambios y cerrar conexiones
pg_conn.commit()
pg_cursor.close()
pg_conn.close()
print("Proceso completado.")