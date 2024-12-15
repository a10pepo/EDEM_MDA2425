'''
    ---------- RETO 2 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
'''

def reto2Basico():
  numero_inicial: int = int(input('Introduce un número: '))
  numero_final: int = int(input('Inroduce otro número: '))
  numeros_impares: [int] = []

  while numero_final <= numero_inicial:
      numero_final: int = int(input('El segundo número debe ser mayor que el primero. Inroduce otro número: '))

  for i in range(numero_inicial, numero_final+1):
      if(i % 2 != 0):
          numeros_impares.append(i)

  print(f"Lista de Números impares entre {numero_inicial} y {numero_final}:")
  print(numeros_impares)