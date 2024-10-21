import sys

if len(sys.argv) != 3:
    print("No has introducido dos parametros.")
    sys.exit(-1)

try:
    resultado = float(sys.argv[1]) + float(sys.argv[2])
except ValueError:
    print("No has introducido valores nuericos.")
    sys.exit(-1)

print("La suma es: " + str(resultado))

    