# Pedirle al usuario que introduzca un número
numero= int(input('Introduce un número entero: '))

# Volver a repetir las condiciones de antes

def num_primo(numero):
        if numero > 1:
            es_primo= True
            for j in range (2, int(numero**0.5)+1): # Otra condición para comprobar que sea primo o no
                if numero % j == 0:
                    es_primo= False
                    break
            if es_primo:
                print(f'El número {numero} es primo')
            else:
                print(f'El número {numero} no es primo')
num_primo(numero)