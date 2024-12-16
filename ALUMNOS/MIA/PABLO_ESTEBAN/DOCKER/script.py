import sys

def main():
    if len(sys.argv) != 3:
        print("Uso: python script.py <num1> <num2>")
        sys.exit(1)
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        suma = num1 + num2
        print(f"El resultado de la suma es: {suma}")
    except ValueError:
        print("Por favor, ingrese dos números válidos.")
        sys.exit(1)

if __name__ == "__main__":
    main()
