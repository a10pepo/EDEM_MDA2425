#Leer fichero palabras
#Iterar las palabras e imprimir una cada vez
#Por cada palabra hay que iterar las letras

abecedario= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open("palabras.txt", 'r') as fichero:
    palabras = fichero.read().splitlines()
    #print(palabras)

intentos = 0
aciertos = 0

print(palabras)

for palabra in palabras:
    print("Probando:" + palabra)
    for letra in abecedario:
        intentos = intentos + 1
        if letra in palabra:
            print(letra + " en " + palabra)
            aciertos= aciertos + palabra.count(letra)
            if aciertos == len(palabra):
                print('Acerté la palabra')
                aciertos = 0
                break
            else:
                print(aciertos)
                print(len(palabra))
                print(intentos)


print(intentos)


