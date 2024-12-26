from pymongo import MongoClient
import psycopg2
import re

# Función para limpiar y dividir las palabras (hay muchas comillas, capital letters etc)
def limpiar_y_dividir_palabras(frase):
    palabras = re.findall(r'\b\w+\b', frase.lower())
    return palabras

# Conexión a MongoDB
mongo_uri = "mongodb://root:example@localhost:27017/"
client = MongoClient(mongo_uri)

try:
    # Acceder a la base de datos y colección en MongoDB
    db = client["Chuck"]
    collection = db["Chiste"]
    documentos = collection.find()

    # Configuración de la conexión a PostgreSQL
    POSTGRES_CONFIG = {
        "host": "localhost", 
        "port": 5432,
        "database": "postgres",  
        "user": "postgres",
        "password": "Welcome01"
    }

    # Aquí creamos la database en postgres y hacemos el embeding
    with psycopg2.connect(**POSTGRES_CONFIG) as conn:
        conn.autocommit = True
        with conn.cursor() as cursor:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS public."Palabras_chuck" (
                "palabra" TEXT NOT NULL,
                "conteo" INT DEFAULT 0,
                CONSTRAINT palabra_unique UNIQUE ("palabra")
            );
            """
            cursor.execute(create_table_query)
            print("Tabla creada/verificada exitosamente.")

            # Procesar los documentos de MongoDB y extraer palabras
            for doc in documentos:
                if 'value' in doc:  
                    frase = doc['value']
                    lista_palabras = limpiar_y_dividir_palabras(frase)

                    # Esto lo he hecho para verificar por el VSC si lo estaba pillando bien (en postgres no se mostraban en un principio etc)
                    print(f"Frase: {frase}")
                    print(f"Lista de palabras: {lista_palabras}")

                    # Insertar las palabras en la tabla y actualizar el conteo
                    for palabra in lista_palabras:
                        insert_or_update_query = """
                        INSERT INTO public."Palabras_chuck" (palabra, conteo)
                        VALUES (%s, 1)
                        ON CONFLICT ("palabra") 
                        DO UPDATE SET conteo = public."Palabras_chuck".conteo + 1;
                        """
                        print(f"Inserting/Updating: {palabra}")  
                        cursor.execute(insert_or_update_query, (palabra,))
                else:
                    print(f"Documento sin el campo 'value': {doc}")
            print("Inserción y actualización de palabras completada.")

except Exception as e:
    print(f"Error: {e}")
finally:
    # Cerrar conexión a MongoDB cuando se hayan procesado todas las frases
    client.close()
    print("Conexión a MongoDB cerrada.")
