import sys

def main():
    if len(sys.argv) != 3:
        print("Se requiere como argumento de entrada dos números para ser sumados.")
        return
    
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    suma = num1 + num2
    print(f"La suma de {num1} y {num2} es: {suma}")


if __name__ == "__main__":
    main()