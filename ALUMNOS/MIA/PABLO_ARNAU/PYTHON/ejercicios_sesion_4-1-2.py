def es_primo(n):
    if n <= 1:
        return False
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True

parametro = int(input ('Dame un número para saber si es primo o no:'))
resultado = es_primo(parametro)
print (f' El número {parametro} es primo: {resultado}')
