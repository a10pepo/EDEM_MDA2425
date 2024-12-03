abec = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open("palabras.txt","r+") as fichero:
    palabras = fichero.read().splitlines()

intentos = 0
aciertos = 0

for palabra in palabras:
    for letra in abec:
        intentos = intentos + 1
        if letra in palabra:
            aciertos = aciertos + palabra.count(letra)
            if aciertos == len(palabra):
                print("acerté la palabra")
                aciertos = 0
                break
print(intentos)
