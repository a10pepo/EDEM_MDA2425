import sys

def sumar_dos_numeros(num1, num2):
    return num1 + num2

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

resultado = sumar_dos_numeros(num1, num2)
print(f"La suma de {num1} y {num2} es: {resultado}")
