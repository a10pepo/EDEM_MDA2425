# Los números primos son aquellos que solo son divisibles entre 1 y entre si mismo. (El numero 1 no es primo)

lista_numeros=[]
while True:
    datos_usuario=input('Añade un número, cuando quieras salir pulsa cualquier otro caracter:')
    if datos_usuario.isdigit():
        lista_numeros.append(int(datos_usuario)) # Que añada un número hasta que introduzca un valor que no es un numero
    else:
        print("Carácter no numérico detectado. Terminando la entrada.")
        break

def num_primo(lista_numeros):
    lista_primos=[]
    for i in lista_numeros:
        if i > 1:
            es_primo= True
            for j in range (2, int(i**0.5)+1): # Otra condición para comprobar que sea primo o no
                if i % j == 0:
                    es_primo= False
                    break
            if es_primo:
                lista_primos.append(i)

    print(f'La lista de números primos es: {lista_primos}')

num_primo(lista_numeros)