'''
    ---------- RETO 13 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo
'''

import math

def area_triangulo(altura: float, base: float) -> float:
    return ((altura*base)/2)

def area_circulo(radio: float) -> float:
    return (math.pi*(radio**2))


def reto13Basico():
  print(f"Área de triangulo: {area_triangulo(2,2)}")
  print(f"Área del círculo: {area_circulo(4)}")