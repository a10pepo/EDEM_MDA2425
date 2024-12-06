import string
import psycopg2
from datetime import datetime

letras = string.ascii_uppercase
abecedario = list(letras)

with open('palabras.txt','r') as fichero:
     palabras = fichero.read().splitlines()


conn_target = psycopg2.connect(
    dbname="AHORCADO",
    user="postgres",
    password="Welcome01",
    host="localhost",
    port="5432" 
)
cursor = conn_target.cursor()

crear_tabla = """
    CREATE TABLE IF NOT EXISTS ahorcado_palabras (
        palabra TEXT,
        letras_acertadas TEXT,
        letras_falladas TEXT,
        intentos INT,
        tiempo TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""
cursor.execute(crear_tabla)
conn_target.commit()


for palabra in palabras:
    intentos = 0
    aciertos = 0
    letras_acertadas = []
    letras_falladas = []
    for letra in abecedario:
        intentos = intentos + 1
        if letra in palabra:           
            print(letra + " en " + palabra)
            aciertos = aciertos + palabra.count(letra)
            letras_acertadas.append(letra)
            if aciertos == len(palabra):
                print('Acerté la palabra')
                aciertos = 0
                break
            else:
                letras_falladas.append(letra)

        insertar =  """
            INSERT INTO ahorcado_palabras (palabra, letras_acertadas, letras_falladas, intentos, tiempo)
            VALUES (%s, %s,%s, %s,%s)
            """
        cursor.execute(insertar, (palabra, ''.join(letras_acertadas), ''.join(letras_falladas), intentos, datetime.now()))

conn_target.commit()
cursor.close()
conn_target.close()

print("Datos insertados correctamente.")
