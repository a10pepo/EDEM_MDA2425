import pymongo
import re
import pg8000.native
from pymongo import MongoClient

# Conexión a PostgreSQL
con = pg8000.native.Connection(user="postgres", password="Welcome01", host="localhost")

# Crear tabla en PostgreSQL si no existe
con.run("""
    CREATE TABLE IF NOT EXISTS chuck (
        word VARCHAR(50) NOT NULL,
        time TIMESTAMP NOT NULL
    )
""")

# Conexión a MongoDB
client = MongoClient("mongodb://root:example@mongo:27017/")
db = client["chuck"]
collection = db["chuck"]

# Lista para almacenar los chistes
jokes = []

# Revisamos cada documento y obtenemos el valor de "value"
for document in collection.find():
    value = document.get("value")

    if value:
        # Limpiar el texto, eliminando caracteres no alfabéticos
        value_limpio = re.sub(r"[^a-zA-Z ]", "", value)
        jokes.append(value_limpio)

# Insertar palabras en PostgreSQL
for joke in jokes:
    for word in joke.split():
        if word:  # Ignorar palabras vacías
            # Usar parámetros en lugar de interpolación para evitar inyecciones SQL
            con.run(
                "INSERT INTO chuck (word, time) VALUES (:word, now())",
                {"word": word}
            )



