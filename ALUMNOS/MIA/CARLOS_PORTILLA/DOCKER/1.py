import sys

def sum_two_numbers(a, b):
    return a + b

def main():
    # Verifica que se hayan proporcionado exactamente dos argumentos
    if len(sys.argv) != 3:
        print("Error: Debes proporcionar exactamente dos números.")
        print("Uso: python 1.py <número1> <número2>")
        sys.exit(1)

    try:
        # Convierte los argumentos a números enteros
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])

        # Calcula la suma
        result = sum_two_numbers(num1, num2)
        print(f"La suma de {num1} y {num2} es: {result}")
    except ValueError:
        print("Error: Ambos argumentos deben ser números enteros válidos.")
        sys.exit(1)

if __name__ == "__main__":
    main()