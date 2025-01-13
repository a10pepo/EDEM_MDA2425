import sys

diccionario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', "Ñ", 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def leer_archivo():
    try:
        with open(sys.argv[1]) as archivo:
            palabras = archivo.read().splitlines() 
        return palabras
    except FileNotFoundError:
        print("El archivo 'palabras.txt' no se encuentra.")
        return []
    
palabras = leer_archivo()

import pg8000.native
con = pg8000.native.Connection(user='postgres',database='DatosAhorcado', password = "Welcome01", host="postgres_container")

intentos = 0
letras_acertadas=""
letras_falladas=""

for palabra in palabras:
    longitud = len(palabra)
    for letra in diccionario:
        if longitud > 0:
            con.run("INSERT INTO juego_ahorcado(palabra) VALUES (:palabra)", palabra=palabra)
            intentos +=1
            if letra in palabra:
                longitud = longitud - 1*palabra.count(letra)
                letras_acertadas += letra
            else:
                letras_falladas +=letra


print(intentos)

