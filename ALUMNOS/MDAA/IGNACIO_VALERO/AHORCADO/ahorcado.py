DICCIONARIO = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
              'N','Ñ','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import pg8000.native
con = pg8000.native.Connection("postgres", password="Welcome01",host="postgres_container")

import sys
def leer_archivo():
    try:
        with open((sys.argv[1])) as archivo:
            palabras = archivo.read().splitlines()
        return palabras
    except FileNotFoundError:
        print("El archivo 'palabras.txt' no se encuentra.")
        return []
   
palabras = leer_archivo()
print(palabras)
intentos = 0


for palabra in palabras:
    letras_acertadas = ""
    letras_falladas= ""
    longitud = len(palabra)
    for letra in DICCIONARIO:
        if longitud >0:
            intentos += 1
            con.run("INSERT INTO ahorcado (palabra,letras_acertadas,letras_falladas) VALUES (:palabra,:letras_acertadas,:letras_falladas)", palabra=palabra,letras_acertadas=letras_acertadas,letras_falladas=letras_falladas)
            if letra in palabra:
                longitud= longitud - 1 * palabra.count(letra)
                print(longitud)
                letras_acertadas += letra
            else:
                letras_falladas += letra
    

print(intentos)

