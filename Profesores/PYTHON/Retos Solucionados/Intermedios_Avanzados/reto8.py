'''
    ---------- RETO 8 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe una función que reciba un número entero positivo y devuelva su factorial.

Ejemplo Factorial 5 es 5*4*3*2*1
'''

def factorial(numero: int) -> int:
  factorial: int = 1
  
  if(numero <= 0):
    print('Queremos un número positivo distinto de 0')
    return None
  
  for n in range(1,numero+1):
    factorial *= n
  
  return factorial

def reto8Avanzado():
  print(f"El Factorial de 6 es {factorial(6)}")