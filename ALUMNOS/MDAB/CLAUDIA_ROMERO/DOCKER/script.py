import sys

#Función suma
def suma(numero1, numero2):
    resultado = numero1 + numero2
    print(f'El resultado de sumar {numero1} y {numero2} es: {resultado}')

# Verificar los dos argumentos
if len(sys.argv) != 3:
    print("Terminal: python script.py <numero1> <numero2>")
    sys.exit()

#Convertir argumentos a números
try:
    numero1 = float(sys.argv[1])
    numero2 = float(sys.argv[2])
    suma(numero1, numero2)
except ValueError:
    print("Por favor, ingrese solo dos números.")
