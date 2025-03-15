import sys

def suma(a, b):
    return a + b

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python suma.py <num1> <num2>")
        sys.exit(1)
    
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    
    resultado = suma(num1, num2)
    print(f"La suma de {num1} y {num2} es {resultado}")