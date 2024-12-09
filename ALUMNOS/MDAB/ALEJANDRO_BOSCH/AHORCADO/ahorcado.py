

with open("palabras.txt", "r") as fichero:
    palabras = fichero.read().splitlines()

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
              'n', "ñ", 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for i in range(len(palabras)):
#     print(palabras[i].strip())

acierto  = 0
intentos = 0
contador = 0

for palabra in palabras:
    for letra in abecedario:
        intentos = intentos + 1
        if letra in palabra:
            print(letra  + " en " + palabra)
            acierto = acierto + palabra.count(letra) 
            if acierto == len(palabra):
                print("Acerté la palabra")
                contador = contador + acierto
                acierto = 0
                break         

print(intentos)
print(contador)





#controlar si he acabado la palabra, 
#cuantas veces he hecho acierto en la palabra
#resetar aciertos cuando se complete la palabra












