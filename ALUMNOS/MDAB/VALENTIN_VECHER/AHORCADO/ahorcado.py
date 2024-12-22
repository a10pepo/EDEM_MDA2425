import pg8000
from datetime import datetime
import time

time.sleep(30)

CONFIG_DB = {
    "host": "postgres",
    "port": 5432,
    "database": "postgres",
    "user": "postgres",
    "password": "postgres",
}

# Conectar a PostgreSQL
def connect_to_db():
    conn = pg8000.connect(**CONFIG_DB)
    cursor = conn.cursor()
    return conn, cursor

# Crear tabla si no existe
def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ahorcado (
            palabra VARCHAR(255),
            letras_acertadas VARCHAR(255),
            letras_falladas VARCHAR(255),
            intentos INT,
            tiempo TIMESTAMP
        )
    """)

# Insertar datos en la tabla
def insert_data(cursor, palabra, letras_acertadas, letras_falladas, intentos, tiempo):
    cursor.execute(
        "INSERT INTO ahorcado (palabra, letras_acertadas, letras_falladas, intentos, tiempo) VALUES (%s, %s, %s, %s, %s)",
        (palabra, letras_acertadas, letras_falladas, intentos, tiempo)
    )

# Inicializar conexión y tabla
conn, cursor = connect_to_db()
create_table(cursor)

# Juego del ahorcado
abecedario_min = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
abecedario = [letra.upper() for letra in abecedario_min]

with open('palabras.txt', 'r') as fichero:
    palabras = fichero.read().splitlines()

intentos = 0
aciertos = 0
letras_acertadas = ""
letras_falladas = ""

for palabra in palabras:
    print(f"\nJugando con la palabra: {palabra}")
    for letra in abecedario:
        intentos += 1
        if letra in palabra:
            if letra not in letras_acertadas:
                letras_acertadas += letra
            aciertos += palabra.count(letra)
            print(f"✅ {letra} está en la palabra.")
        else:
            if letra not in letras_falladas:
                letras_falladas += letra
            print(f"❌ {letra} no está en la palabra.")
        
        # Registrar estado actual en la base de datos
        tiempo_actual = datetime.now()
        insert_data(
            cursor,
            palabra.upper(),
            letras_acertadas,
            letras_falladas,
            intentos,
            tiempo_actual
        )
        
        # Si se acierta toda la palabra
        if all(l.upper() in letras_acertadas for l in palabra):
            print(f"🎉 ¡Palabra acertada: {palabra.upper()}!")
            letras_acertadas = ""
            letras_falladas = ""
            break

# Confirmar cambios en la base de datos
conn.commit()

print(f"\nNúmero total de intentos: {intentos}")
cursor.close()
conn.close()
