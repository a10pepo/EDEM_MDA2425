'''
    ---------- RETO 18 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
A partir de la siguiente lista:

colores = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),("Yellow", "#FFFF00", "rgb(255, 255, 0)")]

Crea un script que pueda almacenar cada uno de los elementos (tuplas) de la lista en variable1, variable2 y variable3 para después imprimirlas por consola.
'''

def reto18Avanzado():
  colores = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),("Yellow", "#FFFF00", "rgb(255, 255, 0)")]

  variable1, variable2, variable3 = colores
  
  print(variable1)
  print(variable2)
  print(variable3)