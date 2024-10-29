import sys
from ahorcado import Ahorcado

ABECEDARIO = "abcdefghijklmnñopqrstuvwxyz"


def main():
    
    filename = sys.argv[1] if len(sys.argv) > 1 else "palabras.txt"
    numero_intentos = 0

    with open(filename) as f:
        for palabra in f.readlines():
            palabra = palabra.strip()
            print("\n", palabra)
            ahorcado = Ahorcado(palabra)

            for letra in ABECEDARIO:
                if ahorcado.try_letter(letra):
                    if ahorcado.won():
                        numero_intentos += ahorcado.tries
                        break

            print(ahorcado)

    print(f"Intentos Totales: {numero_intentos}")

if __name__ == "__main__":
    main()