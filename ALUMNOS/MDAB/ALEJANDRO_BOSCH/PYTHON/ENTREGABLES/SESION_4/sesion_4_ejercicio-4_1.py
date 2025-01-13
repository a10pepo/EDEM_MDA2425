# Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente 
# los valores primos

lista_primos = []

def esPrimo(num:int):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5 ) + 1):
        if num % i == 0:
            return False
    return True

for num in list(range(1,101)):
    if esPrimo(num):
        lista_primos.append(num)

print(lista_primos)
