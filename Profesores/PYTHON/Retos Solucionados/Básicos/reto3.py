'''
    ---------- RETO 3 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
'''

def reto3Basico():
  rango_1_100 = range(1,101)

  for i in reversed(rango_1_100):
      print(f"- {i}")