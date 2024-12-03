# Construir un script en python que acepte dos números como parámetros e imprima el resultado de la suma

import sys

if len(sys.argv) != 3:
    print("Uso: python script.py <num1> <num2>")
else:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    print(f"La suma de {num1} y {num2} es: {num1 + num2}")

# python sumar.py 10 20 (ejecutar en la terminal)
