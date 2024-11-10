with open('palabras.txt', 'r') as fichero:
    palabras = [palabra.strip().upper() for palabra in fichero.readlines()]

intentos = 0
aciertos = 0
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

for palabra in palabras:
    letras_encontradas = set()
    for letra in abecedario:
        intentos += 1
        if letra in palabra:
            print(letra + " en " + palabra)
            letras_encontradas.add(letra)
            aciertos += palabra.count(letra)

            if len(letras_encontradas) == len(set(palabra)):
                print ("acerte la palabra" + palabra)
                aciertos = 0
                break
print (intentos)