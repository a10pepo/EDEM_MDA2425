import pymongo
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from collections import Counter
import string
import os

# Configuración de MongoDB
MONGO_URI = "mongodb://root:example@localhost:27017/"
MONGO_DB = "jokesDB"
MONGO_COLLECTION = "jokesCollection"

# Configuración de PostgreSQL
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_DB = os.getenv("POSTGRES_DB", "jokes")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "Welcome01")


def create_database_if_not_exists(host, user, password, db_name):
    """Crea una base de datos en PostgreSQL si no existe."""
    try:
        with psycopg2.connect(host=host, user=user, password=password) as conn:
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
                if not cursor.fetchone():
                    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
                    print(f"Base de datos '{db_name}' creada exitosamente.")
                else:
                    print(f"Base de datos '{db_name}' ya existe.")
    except Exception as e:
        print(f"Error al crear la base de datos: {e}")
        raise


def create_tables(cursor):
    """Crea las tablas necesarias en PostgreSQL."""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS joke_words (
        word VARCHAR(255) PRIMARY KEY,
        count INT DEFAULT 0
    );

    CREATE TABLE IF NOT EXISTS processed_jokes (
        joke_id VARCHAR(255) PRIMARY KEY,
        joke_date TIMESTAMP
    );
    """)


# def process_jokes(mongo_collection, cursor):
#     """Procesa las bromas de MongoDB y actualiza las tablas en PostgreSQL."""
#     documents = mongo_collection.find()
#     all_words = []

#     for doc in documents:
#         joke_id = str(doc["_id"])
#         joke_date = doc.get("date")
#         joke_text = doc.get("joke", "")

#         # Verificar si ya se procesó esta broma
#         cursor.execute("SELECT 1 FROM processed_jokes WHERE joke_id = %s", (joke_id,))
#         if cursor.fetchone():
#             continue

#         # Procesar texto: limpiar puntuación, normalizar y dividir en palabras
#         words = joke_text.translate(str.maketrans("", "", string.punctuation)).lower().split()
#         all_words.extend(words)

#         # Registrar la broma como procesada
#         cursor.execute("""
#         INSERT INTO processed_jokes (joke_id, joke_date)
#         VALUES (%s, %s)
#         """, (joke_id, joke_date))

#     return Counter(all_words)


# def update_word_counts(word_counts, cursor):
#     """Actualiza la tabla de conteo de palabras en PostgreSQL."""
#     for word, count in word_counts.items():
#         cursor.execute("""
#         INSERT INTO joke_words (word, count)
#         VALUES (%s, %s)
#         ON CONFLICT (word)
#         DO UPDATE SET count = joke_words.count + EXCLUDED.count
#         """, (word, count))


# def main():
#     # Crear base de datos si no existe
#     create_database_if_not_exists(POSTGRES_HOST, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB)

#     # Conexión a MongoDB
#     client = pymongo.MongoClient(MONGO_URI)
#     mongo_db = client[MONGO_DB]
#     collection = mongo_db[MONGO_COLLECTION]

#     # Conexión a PostgreSQL
#     try:
#         with psycopg2.connect(
#             host=POSTGRES_HOST,
#             database=POSTGRES_DB,
#             user=POSTGRES_USER,
#             password=POSTGRES_PASSWORD,
#         ) as conn:
#             with conn.cursor() as cursor:
#                 # Crear tablas si no existen
#                 create_tables(cursor)
#                 conn.commit()

#                 # Procesar bromas de MongoDB
#                 word_counts = process_jokes(collection, cursor)

#                 # Actualizar conteo de palabras
#                 update_word_counts(word_counts, cursor)
#                 conn.commit()

#                 print("Procesamiento completado exitosamente.")
#     except Exception as e:
#         print(f"Error durante la ejecución: {e}")
#     finally:
#         client.close()


# if __name__ == "__main__":
#     main()