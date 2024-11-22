#rograma en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100

for numero in range(1, 101):
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                break
        else:
            print(numero)



