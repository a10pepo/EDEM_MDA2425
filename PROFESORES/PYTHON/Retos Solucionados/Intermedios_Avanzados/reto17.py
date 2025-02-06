'''
    ---------- RETO 17 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Crea un script que pueda mostrar la hora actual en milisegundos
'''
import time

def reto17Avanzado():

  mili_seg = int(round(time.time() * 1000))
  print(mili_seg)