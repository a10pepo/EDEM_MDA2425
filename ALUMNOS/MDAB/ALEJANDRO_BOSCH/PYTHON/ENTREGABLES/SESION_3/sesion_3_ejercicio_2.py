
#ejercicio 2

#Crea un programa en Python que sea capaz de calcular y mostrar por 
# consola todos los números primos de 1 - 100

def esPrimo(num: int):
    if num < 2:
        print(f"El número {num} no es primo")
        return  
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:  
            print(f"El número {num} no es primo")
            return  
    print(f"El número {num} es primo")  

numeros = list(range(1, 101))

for num in numeros:
    esPrimo(num)
