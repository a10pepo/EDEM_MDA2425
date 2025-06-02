import sys

def main():
    if len(sys.argv) != 3:
        print("Uso: python sum.py <num1> <num2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        print(f"Sum: {num1 + num2}")
    except ValueError:
        print("Error: Ambos argumentos deben ser números.")
        sys.exit(1)

if __name__ == "__main__":
    main()
