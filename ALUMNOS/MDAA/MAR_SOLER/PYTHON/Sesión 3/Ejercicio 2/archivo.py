# Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100

for num in range (1,101):
    if num < 2:
        continue
    for i in range(2, num):
            if num % i ==0:
                    break
    else:
        print(num)