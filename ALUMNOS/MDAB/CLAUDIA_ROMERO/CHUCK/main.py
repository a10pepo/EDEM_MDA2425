import pymongo
import psycopg2
import re
from collections import Counter

MONGO_URI = "mongodb://root:example@localhost:27017"
MONGO_DB = "CHUCKY"
MONGO_COLLECTION = "chistes"

PG_HOST = "localhost"
PG_PORT = 5432
PG_DB = "chucky"
PG_USER = "postgres"
PG_PASSWORD = "Welcome01"

def limpiar_y_dividir(texto):
    # Pasa a minúsculas, elimina signos y separa palabras
    texto = texto.lower()
    palabras = re.findall(r'\b\w+\b', texto)
    return palabras

def main():
    # Conectar a Mongo
    cliente_mongo = pymongo.MongoClient(MONGO_URI)
    coleccion = cliente_mongo[MONGO_DB][MONGO_COLLECTION]

    # Leer todos los chistes
    chistes = [doc['value'] for doc in coleccion.find() if 'value' in doc]

    # Contar palabras de todos los chistes
    todas_palabras = []
    for chiste in chistes:
        palabras = limpiar_y_dividir(chiste)
        todas_palabras.extend(palabras)
    contador = Counter(todas_palabras)

    # Conectar a Postgres
    conn = psycopg2.connect(host=PG_HOST, port=PG_PORT, dbname=PG_DB,
                            user=PG_USER, password=PG_PASSWORD)
    cur = conn.cursor()

    # Crear tabla si no existe
    cur.execute("""
        CREATE TABLE IF NOT EXISTS palabras_chuck (
            palabra TEXT PRIMARY KEY,
            contador INT NOT NULL
        )
    """)
    conn.commit()

    # Insertar o actualizar conteo de palabras
    for palabra, cantidad in contador.items():
        cur.execute("""
            INSERT INTO palabras_chuck (palabra, contador)
            VALUES (%s, %s)
            ON CONFLICT (palabra)
            DO UPDATE SET contador = palabras_chuck.contador + EXCLUDED.contador
        """, (palabra, cantidad))
    conn.commit()

    cur.close()
    conn.close()
    cliente_mongo.close()

    print(f"Procesadas {len(contador)} palabras y actualizadas en PostgreSQL.")

if __name__ == "__main__":
    main()
