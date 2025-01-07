# sum.py
import sys

# Verifica que se hayan pasado dos argumentos
if len(sys.argv) != 3:
    print("Error: Debes pasar exactamente dos números como argumentos.")
    sys.exit(1)

# Convierte los argumentos a números enteros
try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
except ValueError:
    print("Error: Ambos argumentos deben ser números enteros.")
    sys.exit(1)

# Realiza la suma e imprime el resultado
result = num1 + num2
print(f"Sum: {result}")