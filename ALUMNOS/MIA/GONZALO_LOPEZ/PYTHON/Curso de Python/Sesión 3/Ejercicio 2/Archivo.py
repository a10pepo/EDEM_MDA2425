# # Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100

def es_primo (n):
    if n < 2 :
        return False  # el 1 no es PRIMO

    if n ==2 :
        return True 


    for i in range(2,n):
        if n % i == 0 :
            return False  # si el numero se puede divir por algun numero y el modulo es 0, NO ES PRIMO


    return True   # si no encontramos divisores es primo

#BUCLE para encontrar los primos de 1 a 100
for num in range (1,101):
    if es_primo(num): # si el numero es primo lo mostramos   
        print(num)