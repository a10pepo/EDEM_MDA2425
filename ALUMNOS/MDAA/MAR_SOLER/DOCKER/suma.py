"""
1. Construir un script en python que acepte dos números como parámetros e imprima el resultado de la suma
2. Construir una imagen docker que contenga dicho python script
3. Cuando se ejecute el contendor docker, este debe invocar al script pasando como parámetro ambos números. 

Ejemplo de invocación del contenedor Docker
docker run pysum 3 4

Ejemplo de salida del resultado esperado
Sum: 7 

"""

import sys

def suma (num1,num2):
    print(f'La suma de {num1} y {num2} es {num1 + num2}')

if len(sys.argv) != 3:
    print("Introduce dos números de una cifra cada uno")

else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    suma(num1, num2)