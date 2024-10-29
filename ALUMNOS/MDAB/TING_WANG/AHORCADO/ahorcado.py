# Importar abecedario
import string
letras = string.ascii_uppercase

abecedario = list(letras)


# Vincular el archivo txt al py.
with open('palabras.txt','r') as fichero:
     palabras = fichero.read().splitlines()


intentos = 0
aciertos = 0
for palabra in palabras:
     for letra in abecedario:
        intentos = intentos + 1
        if letra in palabra:
            print(letra + " en " + palabra)
            aciertos = aciertos + palabra.count(letra)
            if aciertos == len(palabra):
                print('Acerté la palabra')
                aciertos = 0
                break
            # else:
            #     print(aciertos)
            #     print(len(palabra))
            #     print(intentos)


print(intentos)
