import pg8000
from datetime import datetime

mi_abecedario = "AROEICMDPTLGVZNUJSBFHKQWXY"

def leer_palabras(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().upper() for line in file.readlines()]

def adivinar_palabra(palabra, db_cursor):
    letras_acertadas = ""
    letras_falladas = ""
    intentos = 0

    for letra in mi_abecedario:
        if all(l in letras_acertadas for l in palabra):
            break
        intentos += 1
        if letra in palabra:
            letras_acertadas += letra
        else:
            letras_falladas += letra

        tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db_cursor.execute("""
            INSERT INTO intentos (palabra, letras_acertadas, letras_falladas, intentos, tiempo)
            VALUES (%s, %s, %s, %s, %s)
        """, (palabra, letras_acertadas, letras_falladas, intentos, tiempo))

    # Tiempo final después de completar la palabra
    tiempo_final = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Imprimir el resultado final después de todos los intentos para la palabra
    print(f"Palabra: {palabra}, Letras acertadas: {letras_acertadas}, "
          f"Letras falladas: {letras_falladas}, Total Intentos: {intentos}, "
          f"Tiempo final: {tiempo_final}")
    
    return intentos  # Devolver el número de intentos para acumular en el total

def main():
    db_conn = pg8000.connect(
        host='localhost',  # Cambia a 'db' si estás usando Docker Compose
        user='user',
        password='password',
        database='ahorcado_db',
        port=5432
    )
    db_cursor = db_conn.cursor()

    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS intentos (
            id SERIAL PRIMARY KEY,
            palabra VARCHAR(255),
            letras_acertadas VARCHAR(255),
            letras_falladas VARCHAR(255),
            intentos INT,
            tiempo TIMESTAMP
        )
    """)
    db_conn.commit()

    file_path = 'palabras.txt'
    palabras = leer_palabras(file_path)
    intentos_totales = 0  # Variable para acumular el total de intentos

    # Procesar cada palabra y mostrar el resultado
    for palabra in palabras:
        intentos = adivinar_palabra(palabra, db_cursor)
        intentos_totales += intentos
        db_conn.commit()

    # Imprimir el total de intentos después de procesar todas las palabras
    print(f"Total número de intentos: {intentos_totales}")

    db_cursor.close()
    db_conn.close()

if __name__ == "__main__":
    main()
