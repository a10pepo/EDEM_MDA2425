import sys
import os
import mysql.connector
from datetime import datetime

db_config = {
    'user': os.getenv('DB_USER', 'user'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'host': os.getenv('DB_HOST', 'mysql'),
    'database': os.getenv('DB_NAME', 'ahorcado_db')
}

def conectar_db():
    return mysql.connector.connect(**db_config)

def crear_tabla():
    conn = conectar_db()
    with conn.cursor() as micursor:
        
        micursor.execute("DROP TABLE IF EXISTS intentos_ahorcado")
        micursor.execute("""
            CREATE TABLE IF NOT EXISTS intentos_ahorcado (
                id INT AUTO_INCREMENT PRIMARY KEY,
                palabra VARCHAR(255),
                letras_acertadas TEXT,
                letras_falladas TEXT,
                intentos INT,
                tiempo TIMESTAMP
            )
        """)
        conn.commit()
    conn.close()

def registrar_intento(palabra, letras_acertadas, letras_falladas, intentos):
    conn = conectar_db()
    with conn.cursor() as micursor:
        tiempo_actual = datetime.now()
        micursor.execute("""
            INSERT INTO intentos_ahorcado (palabra, letras_acertadas, letras_falladas, intentos, tiempo)
            VALUES (%s, %s, %s, %s, %s)
        """, (palabra, letras_acertadas, letras_falladas, intentos, tiempo_actual))
        conn.commit()
    conn.close()

def adivinar_palabras(archivo):
    abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    total_intentos = 0
    
    with open(archivo, 'r') as f:
        for palabra in f:
            palabra = palabra.strip().upper()
            palabra_actual = ['_'] * len(palabra)
            letras_bien = ""
            letras_mal = ""
            intentos = 0

            for letra in abecedario:
                if '_' not in palabra_actual:
                    break
                fallo = True
                for i, caracter in enumerate(palabra):
                    if caracter == letra:
                        palabra_actual[i] = letra
                        fallo = False
                if fallo:
                    letras_mal += letra
                else:
                    letras_bien += letra
                intentos += 1
                registrar_intento(palabra, letras_bien, letras_mal, intentos)

            total_intentos += intentos    
            print(f"\nPalabra '{palabra}' adivinada en {intentos} intentos.")
            print(f"Letras bien {letras_bien}")
            print(f"Letras bien {letras_mal}")
    print(f"\nTotal de intentos utilizados en todas las palabras: {total_intentos}")

crear_tabla()    
file = sys.argv[1]
adivinar_palabras(file)