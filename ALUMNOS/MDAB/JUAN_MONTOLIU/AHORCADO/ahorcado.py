
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open("palabras.txt", "r") as fichero:
    palabras = fichero.read().splitlines()

intentos = 0
aciertos = 0 

print(palabras)
for palabra in palabras:
    for letra in alfabeto:
        intentos = intentos + 1
        if letra in palabra:
            print(letra + " en " + palabra)
            aciertos = aciertos + palabra.count(letra)
            if aciertos == len(palabra):
                print("Acerté la palabra")
                aciertos = 0
                break
print(intentos)
print(aciertos)