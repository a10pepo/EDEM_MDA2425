import sys

def main():
    if len(sys.argv) != 3:
        print("Uso: python script.py <num1> <num2>")
        sys.exit(1)
    
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print(f"Suma: {num1 + num2}")
    except ValueError:
        print("Error: Los dos argumentos deben ser números enteros.")
        sys.exit(1)

if __name__ == "__main__":
    main()
