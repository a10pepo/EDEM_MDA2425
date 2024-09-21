'''
    ---------- RETO 30 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    -------------------------------------------------
'''

'''

Investiga acerca de ast y convierte un String en una lista. Es decir, un string que representa una lista literalmente. 

Puedes usar este ejemplo:
colores ="['Rojo', 'Verde', 'Blanco']"


Se trata de una cadena de texto que dentro contiene una lista. La idea es que a través de ast lo conviertas en una lista como tal.
'''

import ast


def reto30Avanzado():
  colores ="['Rojo', 'Verde', 'Blanco']"

  print(ast.literal_eval(colores))
