import sys

try:
    nombre_fichero = sys.argv[1]
    fichero = open(f'{nombre_fichero}','r')
    lineas = fichero.readlines()
except IndexError:
    print("Debes introducir un fichero para leerlo")
    exit()
except NameError:
    print("El fichero no se puede leer")
    exit()

palabras = []
abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
num_intentos_totales = 0
num_intentos_locales = 0

for palabra in lineas:
    palabras.append(palabra.strip().upper())

for aux in palabras:
    palabra = set(aux)
    num_intentos_locales = 0
    for letra in abecedario:
        palabra.discard(letra)
        if (len(palabra) == 0):
            break
        num_intentos_totales += 1
        num_intentos_locales += 1
    print(f'Se ha encontrado la palabra {aux} en {num_intentos_locales} intentos.')

print(f'Se han necesitado {num_intentos_totales} intentos totales')
fichero.close()