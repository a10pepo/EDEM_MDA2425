import pymongo
import pg8000.native
import re
from datetime import datetime

def conectar_mongo(uri, db_name, collection_name):
    cliente = pymongo.MongoClient(uri)
    db = cliente[db_name]
    return db[collection_name]

def conectar_postgres(usuario, contrasena, host):
    return pg8000.native.Connection(user=usuario, password=contrasena, host=host)

def crear_tabla_si_no_existe(conexion):
    sql = '''CREATE TABLE IF NOT EXISTS palabras_chistes (
        palabra VARCHAR(50) NOT NULL,
        fecha_insercion TIMESTAMP NOT NULL
    )'''
    conexion.run(sql)

def extraer_palabras(texto):
    # Elimina caracteres no alfanuméricos y separa por espacios
    texto_limpio = re.sub(r'[^\w\s]', '', texto)
    return [palabra for palabra in texto_limpio.split() if palabra]

def insertar_palabras_en_postgres(conexion, palabras):
    for palabra in palabras:
        conexion.run(
            "INSERT INTO palabras_chistes(palabra, fecha_insercion) VALUES(%s, %s)",
            (palabra, datetime.now())
        )

def main():
    # Parámetros de conexión
    mongo_uri = "mongodb://root:example@localhost:27017/"
    db_mongo = "Chuck"
    coleccion = "Database_Chuck"
    usuario_pg = "postgres"
    contrasena_pg = "Welcome01"
    host_pg = "localhost"

    # Conexiones
    col = conectar_mongo(mongo_uri, db_mongo, coleccion)
    conn_pg = conectar_postgres(usuario_pg, contrasena_pg, host_pg)
    crear_tabla_si_no_existe(conn_pg)

    total_palabras = 0
    for doc in col.find():
        valor = doc.get('value')
        if valor:
            palabras = extraer_palabras(valor)
            insertar_palabras_en_postgres(conn_pg, palabras)
            total_palabras += len(palabras)
    print(f"Total de palabras insertadas: {total_palabras}")

if __name__ == "__main__":
    main()
    