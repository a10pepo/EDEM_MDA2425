'''
    ---------- RETO 16 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Crea un script que sea capaz de restar dos fechas y muestra el resultado por consola
'''

from datetime import date

def reto16Basico():
  fechaA = date(2000,2,28)
  fechaB = date(2001,2,28)

  print(fechaB-fechaA)