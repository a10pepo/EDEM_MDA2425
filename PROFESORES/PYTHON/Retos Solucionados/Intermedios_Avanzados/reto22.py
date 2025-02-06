'''
    ---------- RETO 22 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    -------------------------------------------------
'''

'''
A partir de:

listaTuplas = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
miDiccionario = {}

Realiza una iteración para poder pasar de una lista de tuplas a un diccionario llamado miDiccionario

'''

def reto22Avanzado():
  listaTuplas = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
  miDiccionario = {}

  for a, b in listaTuplas:
      miDiccionario.setdefault(a, []).append(b)

  print (miDiccionario)