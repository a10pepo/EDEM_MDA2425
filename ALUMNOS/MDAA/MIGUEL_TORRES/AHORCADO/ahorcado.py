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

import pg8000
con = pg8000.native.Connection("postgres", password = "Welcome01")

intentos = 0

for palabra in palabras:
    longitud = len(palabra)
    for letra in diccionario:
        if longitud > 0:
            con.run("INSERT INTO book (title) VALUES (:title)", title=title)
            intentos +=1
            if letra in palabra:
                longitud = longitud - 1*palabra.count(letra)
                #print(longitud)

print(intentos)

