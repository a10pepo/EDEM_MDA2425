abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


#Leer fichero palabras
with open('palabras.txt', 'r') as fichero:
    palabras = fichero.read().splitlines()

intentos = 0
aciertos = 0
contador = 0

for palabra in palabras:
    for letra in abecedario:
        intentos = intentos + 1
        if letra in palabra:
            print(letra + " en " + palabra)
            aciertos = aciertos + palabra.count(letra)
            #print(aciertos)
            if aciertos == len(palabra):
                print("Acerté la palabra")
                contador = contador + aciertos
                aciertos = 0
                break

print(intentos)
print(contador)
