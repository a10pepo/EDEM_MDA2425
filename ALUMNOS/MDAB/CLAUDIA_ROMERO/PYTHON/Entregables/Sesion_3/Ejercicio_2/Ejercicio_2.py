#Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100

numeros = list(range(1, 101))

def numero_primo(n):
    if n < 2:
        return False
    
    for x in range(2, n): 
        if n % x == 0:
            return False
    
    return True

for n in numeros:
    if numero_primo(n):
        print(n)