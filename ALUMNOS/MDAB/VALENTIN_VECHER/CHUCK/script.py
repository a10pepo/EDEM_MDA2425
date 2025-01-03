from pymongo import MongoClient

# Configuración de la conexión
MONGO_URI = "mongodb://root:example@localhost:27017"
DATABASE_NAME = "chuck-db"
COLLECTION_NAME = "chuckcol"

def count_jokes():
    try:
        # Conectar a MongoDB
        client = MongoClient(MONGO_URI)
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        
        # Contar documentos en la colección
        joke_count = collection.count_documents({})
        
        # Mostrar el resultado
        print(f"El número total de chistes en la base de datos es: {joke_count}")
        
        # Cerrar la conexión
        client.close()
    except Exception as e:
        print(f"Error al conectar con MongoDB: {e}")

# Ejecutar la función
count_jokes()

def split_jokes_to_lines():
    try:
        # Conectar a MongoDB
        client = MongoClient(MONGO_URI)
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        
        # Obtener todos los documentos de la colección
        jokes = collection.find({}, {"_id": 0, "joke": 1})
        
        # Procesar cada chiste y dividir en palabras
        for joke in jokes:
            text = joke.get("joke", "")
            words = text.split()  # Dividir el texto en palabras
            for word in words:
                print(word)
        
        # Cerrar la conexión
        client.close()
    except Exception as e:
        print(f"Error al conectar con MongoDB o procesar los datos: {e}")

# Ejecutar la función
split_jokes_to_lines()


import pg8000

# Configuración de MongoDB
MONGO_URI = "mongodb://<username>:<password>@<host>:<port>"
DATABASE_NAME = "nombre_de_tu_base_de_datos"
COLLECTION_NAME = "nombre_de_tu_coleccion"

# Configuración de PostgreSQL
POSTGRES_HOST = "localhost"  # Cambia si estás usando otro host
POSTGRES_PORT = 5432
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "Welcome01"
POSTGRES_DB = "nombre_de_tu_base_de_datos"

def insert_words_into_postgres():
    try:
        # Conectar a MongoDB
        mongo_client = MongoClient(MONGO_URI)
        mongo_db = mongo_client[DATABASE_NAME]
        mongo_collection = mongo_db[COLLECTION_NAME]

        # Conectar a PostgreSQL
        pg_conn = pg8000.connect(
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            dbname=POSTGRES_DB
        )
        pg_cursor = pg_conn.cursor()

        # Leer los chistes de MongoDB
        jokes = mongo_collection.find({}, {"_id": 0, "joke": 1})
        
        for joke in jokes:
            text = joke.get("joke", "")
            words = text.split()  # Dividir en palabras
            
            for word in words:
                # Limpia las palabras (opcional)
                clean_word = word.strip().lower()

                # Inserta o actualiza el contador en PostgreSQL
                query = """
                    INSERT INTO words (word, count)
                    VALUES (%s, 1)
                    ON CONFLICT (word) 
                    DO UPDATE SET count = words.count + 1;
                """
                pg_cursor.execute(query, (clean_word,))
        
        # Confirmar transacción
        pg_conn.commit()
        print("Las palabras se han insertado/actualizado correctamente.")

        # Cerrar conexiones
        pg_cursor.close()
        pg_conn.close()
        mongo_client.close()

    except Exception as e:
        print(f"Error: {e}")

# Ejecutar la función
insert_words_into_postgres()


