import sys

def sumar(numero_1, numero_2):
    return numero_1 + numero_2

numero_1 = float(sys.argv[1])
numero_2 = float(sys.argv[2])

Resultado_suma = sumar(numero_1, numero_2)
print(f'(Si sumamos tanto el valor {numero_1} y el valor {numero_2} obtenemos {Resultado_suma})')