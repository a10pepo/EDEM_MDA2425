diccionario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

intentos = 0
aciertos = 0 

with open ('palabras.txt', 'r') as fichero:
    for palabra in fichero:
        for letra in diccionario:
            intentos = intentos + 1
            if letra in palabra:
                print(letra.strip() + ' en ' + palabra.strip())
                aciertos = aciertos + palabra.count(letra)
                if aciertos == len(palabra.strip()):
                    print ('Acerté la palabra')
                    aciertos = 0
                    break
                



print (intentos)
print (aciertos)