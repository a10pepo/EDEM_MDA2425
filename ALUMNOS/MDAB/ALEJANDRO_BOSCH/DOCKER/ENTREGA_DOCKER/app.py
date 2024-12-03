
import sys

print("Hola, bienvenido a este programa de sumas!")

def sumar (a, b):
    resultado = a + b
    print(f"El resultado de la suma es {resultado}")

if len(sys.argv) != 3:
    print("Por favor, introduzca solo dos numeros como parámetros.")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    sumar(num1, num2)






