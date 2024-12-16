import sys

def realizar_suma():
    if len(sys.argv) < 3:
        print("Error: Se requieren exactamente 2 números como argumentos.")
        return
    try:
        numero1 = float(sys.argv[1])
        numero2 = float(sys.argv[2])
        resultado = numero1 + numero2
        print(f"La suma de {numero1} y {numero2} es: {resultado}")
    except ValueError:
        print("Por favor, ingrese números válidos.")
        return

if __name__ == "__main__":
    realizar_suma()

