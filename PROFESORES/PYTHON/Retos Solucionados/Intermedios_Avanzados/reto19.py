'''
    ---------- RETO 19 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa capaz de imprimir los próximos tres días a partir de la fecha actual
(haz uso de datetime.datetime.today() para obtener la fecha actual).

Pista: investiga acerca de datetime.timedelta()
'''
import datetime

def reto19Avanzado():

  base = datetime.datetime.today()

  for x in range(0, 3):
      print(base + datetime.timedelta(days=x))