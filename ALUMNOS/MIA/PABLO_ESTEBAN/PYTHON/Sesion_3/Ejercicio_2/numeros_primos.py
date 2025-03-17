import math

# Lista para almacenar los números primos encontrados
lista_primos = []

# Comenzamos con 2, el primer número primo
i = 2

while i <= 100:

    primo = True
    # Solo revisar los primos hasta la raíz cuadrada de i
    limite = int(math.sqrt(i)) + 1

    for j in lista_primos:
        if j > limite:
            break
        if i % j == 0:
            primo = False
            break

    if primo:
        lista_primos.append(i)

    # Si es 2, incrementamos en 1 para comprobar 3, y luego solo probamos impares
    i += 1 if i == 2 else 2  # Incrementa en 2 para omitir pares

print(f"Números primos encontrados: {lista_primos}")
