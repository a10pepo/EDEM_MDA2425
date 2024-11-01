abecedario = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

intentos = 0
aciertos = 0

with open('palabras.txt', 'r') as fichero:
    palabras = fichero.read().splitlines() 

for palabra in palabras:
    for letra in abecedario:
        intentos = intentos + 1
        if letra in palabra:
            print(letra + " en " + palabra) 
            aciertos = aciertos + palabra.count(letra)
            if aciertos == len(palabra):
                print ("Acerté la palabra")
                aciertos = 0
                break

print(intentos)
print(aciertos)
