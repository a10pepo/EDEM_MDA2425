
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True


rango = range (1,101)
print('El listado de números primos del 1 al 100 es:')
for a in rango:
    if es_primo(a) == True:
        print (f'{a}')
