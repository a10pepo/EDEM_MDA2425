DICCIONARIO = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
              'N','Ñ','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import pg8000
con = pg8000.native.Connection("postgres", password="Welcome01")

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
letras_acertadas =0
letras_falladas= 0

for palabra in palabras:
    longitud = len(palabra)
    for letra in DICCIONARIO:
        if longitud >0:
            intentos += 1
            con.run("INSERT INTO book (ahorcado) VALUES (:ahorcado)", title=title)
            if letra in palabra:
                longitud= longitud - 1 * palabra.count(letra)
                print(longitud)
                #letras_acertadas += letra
            #else:
                #letras_falladas += letra
    

print(intentos)

