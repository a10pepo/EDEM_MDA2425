#leer lista de palabras
p = open("palabras.txt", "r")
archivo=p.read()
lista_palabras = archivo.split(",")

#leer abecedario
a = open("abecedario.txt", "r")
archivo=a.read()
abecedario = archivo.split(" ")

intentos=0
letras_correctas=[]
letras_incorrects=[]
#Acceder a cada palabra del de la lista
for palabra in lista_palabras:
    NLC=0
    #crear la lista de letras no repetidas de la palabra
    lis_dif_let=[]
    for letra in palabra:
        if letra not in lis_dif_let:
            lis_dif_let.append(letra)

    #numero de letras correctas
    
    for letra in abecedario:
        if NLC == len(lis_dif_let):
            break
        intentos=intentos+1
        if letra in palabra.lower():
            NLC=NLC+1
            letras_correctas.append(letra)
        else:
            letras_incorrects.append(letra)
            
print(intentos) 

