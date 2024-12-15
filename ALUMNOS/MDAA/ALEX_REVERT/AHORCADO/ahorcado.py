diccionario=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

import sys
import pg8000.native 
from datetime import datetime


con = pg8000.native.Connection("postgres", password="Welcome01", host='localhost')



with open(sys.argv[1],'r') as archivo:
    palabras = archivo.read().splitlines() 

print(palabras)    

intentos = 0

for palabra in palabras:
    long=len(palabra)
    letras_acertadas=''
    letras_falladas=''
    for letra in diccionario:
        if long>0:
            tiempo = datetime.now()
            intentos=intentos+1
            if letra in palabra:
                letras_acertadas=letras_acertadas+letra
                long = long-palabra.count(letra)
                print(long)
            else:
                letras_falladas=letras_falladas+letra
                con.run("insert into ahorcado(palabra, letras_acertadas, letras_falladas, intentos, tiempo) VALUES (:palabra, :letras_acertadas, :letras_falladas, :intentos, :tiempo)", palabra=palabra, letras_acertadas=letras_acertadas, letras_falladas=letras_falladas, intentos=intentos, tiempo=tiempo)

print(intentos)