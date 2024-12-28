import sys

def main():
    # Verificar si los parámetros son válidos
    if len(sys.argv) != 3:
        print("Uso: python sum.py <num1> <num2>")
        sys.exit(1)

    try:
        # Leer los números desde los argumentos
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        
        # Calcular y mostrar la suma
        result = num1 + num2
        print(f"Sum: {result}")
    except ValueError:
        print("Por favor, ingrese números válidos.")
        sys.exit(1)

if __name__ == "__main__":
    main()