import sys

if len(sys.argv) == 3:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])

        print(f"La suma de {num1} y {num2} es: {num1+num2}")

    except ValueError:
        print("Ingrese sólo números")
else:
    print("El número de argumentos no es válido. Introduzca dos números.")
