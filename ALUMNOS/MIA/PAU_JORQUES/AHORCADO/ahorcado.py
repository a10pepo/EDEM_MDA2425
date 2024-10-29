import sys
from datetime import datetime
import psycopg2

conexion = psycopg2.connect(
    host="localhost",       
    database="palabras",
    user="postgres",
    password="Welcome01",
    port="5432"            
)

def crear_tabla(nombre_tabla):
    cursor = conexion.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {nombre_tabla} (
            id SERIAL PRIMARY KEY,
            palabra TEXT,
            letras_acertadas TEXT,
            letras_falladas TEXT,
            intentos INTEGER,
            tiempo TIMESTAMP
        )
    """)
    conexion.commit()
    cursor.close()

def insertar_sql(nombre,palabra, letra_acertada, letra_fallada, intentos, tiempo):
    cursor = conexion.cursor()
    cursor.execute(f"INSERT INTO {nombre} (palabra, letras_acertadas, letras_falladas, intentos, tiempo) VALUES (%s, %s, %s, %s, %s)", (palabra,letra_acertada,letra_fallada,intentos,tiempo))
    conexion.commit()
    cursor.close()


try:
    nombre_fichero = sys.argv[1]
    fichero = open(f'{nombre_fichero}','r')
    lineas = fichero.readlines()
except IndexError:
    print("Debes introducir un fichero para leerlo")
    exit()
except NameError:
    print("El fichero no se puede leer")
    exit()

nombre = nombre_fichero.split(".")[0]
crear_tabla(nombre)

palabras = []
abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
num_intentos_totales = 0
num_intentos_locales = 0
letras_acertadas = ""
letras_falladas = ""

for palabra in lineas:
    palabras.append(palabra.strip().upper())

for aux in palabras:
    palabra = set(aux)
    num_intentos_locales = 0
    
    for letra in abecedario:
        if (letra in palabra):
            letras_acertadas += f"{letra}"
            palabra.discard(letra)
        else:
            letras_falladas += f"{letra}"
        num_intentos_totales += 1
        num_intentos_locales += 1
        insertar_sql(nombre,aux,letras_acertadas,letras_falladas,num_intentos_locales,datetime.now())
        if (len(palabra) == 0):
            break
    print(f'Se ha encontrado la palabra {aux} en {num_intentos_locales} intentos.')

print(f'Se han necesitado {num_intentos_totales} intentos totales')
fichero.close()