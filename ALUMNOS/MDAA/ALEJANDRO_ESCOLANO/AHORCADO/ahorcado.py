import sys
import pg8000.native
print(sys.argv)

con = pg8000.native.Connection("postgres", password="Welcome01", host="localhost")


abecedario = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
intentos=0
aciertos=0
letras_acertadas = ""
letras_falladas = ""

with open("palabras.txt", "r") as archivo:
    palabras = archivo.read().splitlines()
      
con.run("DROP TABLE ahorcado")
con.run("CREATE TABLE ahorcado (palabra VARCHAR, letras_acertadas VARCHAR, letras_falladas VARCHAR, intentos VARCHAR, tiempo DATE)")
            
for palabra in palabras:
    longitud=len(palabra)

    for letra in abecedario:
        if longitud>0:
                intentos=intentos+1
                if letra in palabra: 
                    longitud= longitud-1*palabra.count(letra)
                    print(longitud)
                    letras_acertadas= letras_acertadas + letra

                else:
                    letras_falladas= letras_falladas + letra
    
    for palabra in ("MURCIELAGO", "VIAJE" ,"EVADIR", "ZAPATO", "CIELO", "RECREO", "PIZARRA", "MATEMATICAS", "PROGRAMACION", "ORDENADOR"):
        con.run("INSERT INTO ahorcado (palabra, letras_acertadas, intentos, letras_falladas)  VALUES (:palabra, :letras_acertadas, :intentos, :letras_falladas)", palabra=palabra, letras_acertadas=letras_acertadas, intentos=intentos, letras_falladas=letras_falladas)

                    

                    

print(intentos)
print(letras_acertadas)
print(letras_falladas)

con.close()



