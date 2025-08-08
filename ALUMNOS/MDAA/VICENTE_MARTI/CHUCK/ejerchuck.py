from pymongo import MongoClient
import time
import pg8000.native

# Configuración de conexión MongoDB
MONGO_HOST = "mongo"  # Dirección donde está corriendo el contenedor
MONGO_PORT = 27017        # Puerto expuesto en docker-compose
MONGO_USER = "root"       # Usuario root configurado en el archivo docker-compose
MONGO_PASS = "example"    # Contraseña configurada
MONGO_DB = "Chuck"        # Reemplaza con el nombre de tu base de datos

# Crear cliente MongoDB
client = MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/")

# Seleccionar la base de datos
db = client[MONGO_DB]

# Seleccionar una colección
collection = db["Chuck"]

# Conectar con PostgreSQL usando pg8000
# Cambié la base de datos de 'admin' a 'mydb' como está configurado en el docker-compose
# con = pg8000.native.Connection(user="admin", password="adminpassword", host="localhost")

# Conectar a la base de datos PostgreSQL
db_conn = pg8000.native.Connection(
    host='postgres',  # Cambié a 'localhost' porque quieres conectar desde la máquina local (no Docker)
    user='admin',      # Usuario de PostgreSQL
    password='adminpassword',  # Contraseña de PostgreSQL
    database='mydb',  # Aquí está el nombre correcto de la base de datos
    port=5432         # Puerto de PostgreSQL expuesto
)

# Crear un cursor para ejecutar SQL
# db_cursor = db_conn.cursor()

# Crear la tabla si no existe
db_conn.run("""
    CREATE TABLE IF NOT EXISTS palabras (
        palabra VARCHAR(255),
        frase VARCHAR(255),
        tiempo TIMESTAMP,
        PRIMARY KEY (palabra, frase, tiempo)
    );
""")

# Leer documentos de MongoDB
for documento in collection.find():
    frase = documento["value"]  # Asegúrate de que 'value' existe en el documento
    frase_recorrer = frase.split()  # Dividir la frase en palabras

    # Insertar cada palabra de la frase en PostgreSQL
    for palabra in frase_recorrer:
        print(f"Inserting palabra: {palabra}")

        # Aquí, debes utilizar parámetros en lugar de concatenación para evitar inyecciones de SQL
        db_conn.run('INSERT INTO palabras (palabra, frase, tiempo) VALUES (:palabra, :frase, now())', palabra=palabra, frase=frase)


# Cerrar las conexiones
# db_cursor.close()
db_conn.close()

