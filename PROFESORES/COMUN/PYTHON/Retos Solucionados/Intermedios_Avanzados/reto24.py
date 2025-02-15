'''
    ---------- RETO 24 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    -------------------------------------------------
'''

'''
Haciendo uso de {:.2%}

Muestra por consola los valores 0.2564 y -0.253 como porcentajes de dos cifras.
'''

def reto24Avanzado():
  x = 0.2564
  y = -0.253

  print("\nNúmero Original: ", x)
  print("Porcentaje: " + "{:.2%}".format(x));

  print("Número Original: ", y)
  print("Porcentaje: " + "{:.2%}".format(y));

  print()