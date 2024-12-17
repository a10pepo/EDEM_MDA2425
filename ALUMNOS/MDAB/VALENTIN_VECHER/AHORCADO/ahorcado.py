abecedario_min= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
abecedario=[letra.upper() for letra in abecedario_min]

with open('palabras.txt','r') as fichero:
    palabras=fichero.read().splitlines()


intentos=0
aciertos=0
fallos=0 

num_aciertos=[]


for palabra in palabras:
    for letra in abecedario:
        intentos= intentos+1
        if letra in palabra:
            print(letra + ' en ' + palabra)
            aciertos= aciertos+ palabra.count(letra)
            if aciertos==len(palabra):
                print('Oleee, has acertado la palabra')
                num_aciertos.append(aciertos)
                aciertos=0
                
                break
                
total_aciertos=sum(num_aciertos)
print(f'el numero de intentos es de: {intentos}')
print(f'el numero de aciertos es de: {total_aciertos}')

