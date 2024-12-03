# Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no

def esPrimo (num:int):
    if num < 2:
        print(f"El número {num} no es primo")
        return 
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"El número {num} no es primo")
            return  
    print(f"El número {num} es primo")

for num in list(range(1,101)):
    esPrimo(num)

