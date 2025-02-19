'''
    ---------- RETO 20 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Haciendo uso de enumerate() muestra por consola cada uno de los caracteres de la palabra Valencia junto al índice de su posición.
'''

def reto20Avanzado():
  palabra = "Madrid"

  for index, caracter in enumerate(palabra):
      print("Caracter: ", caracter, "\nÍndice", index )