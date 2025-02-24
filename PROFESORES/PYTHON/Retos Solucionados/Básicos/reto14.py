'''
    ---------- RETO 14 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro, 
obteniendo por parámetro la longitud del mismo.
'''

import math

def area_circulo(radio: float) -> float:
    return (math.pi*(radio**2))

def volumen_cilindro(radio:float, longitud: float) -> float:
    return area_circulo(radio)*longitud

def reto14Basico():
  print(f"El volumen del cilindro es: {volumen_cilindro(2, 3)}")