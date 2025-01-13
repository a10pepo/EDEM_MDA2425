def es_primo(n):
    if n <= 1:
        return False
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True

def es_primo_rango():
    init = int (input ('Dime inicio del rango: '))
    fin = int (input ('Dime fin del rango: '))

    rango = range (init,fin + 1)
    print('El listado de números primos del 1 al 100 es:')
    for a in rango:
        if es_primo(a) == True:
            print (f'{a}')

es_primo_rango()