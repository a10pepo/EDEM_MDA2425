'''
    ---------- RETO 21 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''

Haciendo uso de:
colores = ["Negro", "Rojo", "Marrón", "Amarillo"]representacion = ["#000000", "#FF0000", "#800000", "#FFFF00"]

e investigando acerca de zip() deberás entrelazar ambas listas para obtener un diccionario que tenga la clave color cuyos valores son los de la lista colores y otra clave code que tendrá como valor los datos de la lista representación
'''

def reto21Avanzado():
  colores = ["Negro", "Rojo", "Marrón", "Amarillo"]
  representacion = ["#000000", "#FF0000", "#800000", "#FFFF00"]

  print([{'color': f, 'codigo': c} for f, c in zip(colores, representacion)])