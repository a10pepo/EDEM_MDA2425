
abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Leer fichero palabras.txt
# Iterar palabras e imprimir una
# Por cada palabra --> iterar letras 

with open("palabras.txt") as fichero:
    palabras = fichero.read().splitlines()
    #print(palabras)

intentos = 0
aciertos = 0
    

for palabra in palabras:
    for letra in abecedario:
        intentos = intentos + 1
        if letra in palabra:
            print(letra+" en "+palabra)
            aciertos = aciertos + palabra.count(letra)
            if aciertos == len(palabra):
                print("Acerté la palabra")
                aciertos = 0
                break
            else:
                print(aciertos)
                print(len(palabra))
                print(intentos)
    
print(intentos)


