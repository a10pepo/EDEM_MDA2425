'JUEGO DEL AHORCADO'

import psycopg2

#PARA LEER UN DOCUMENTO EN PYTHON 
with open("palabras.txt", "r") as file:

    palabras= file.read() .splitlines()
    abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    intentos = 0
    aciertos = 0

    for palabra in palabras:
        for letra in abecedario:
            intentos = intentos + 1
            if letra in palabra:
                print(letra + " en " + palabra)
                aciertos = aciertos + palabra.count(letra)
                if aciertos == len(palabra):
                    print('Acerte la palabra')
                    aciertos = 0
                    break
print(intentos)
print(aciertos)

#como conectar
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="ahorcado",
    user="postgres",
    password="Welcome01"
)

def insertar_tabla(palabra, letras_acertadas, letras_falladas, intentos, tiempo):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ahorcado (alabra, letras_acertadas, letras_falladas, intentos, tiempo);")







