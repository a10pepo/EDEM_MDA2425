'''
    ---------- RETO 7 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa que pida 5 precios al usuario y los almacene en una lista de precios.

Al finalizar, deberá mostrar por consola la media de los precios introducidos.
'''

def reto7Avanzado():
  lista_precios: [float] = []
  total: float = 0.0
  media_precios: float = 0.0

  while (lista_precios.__len__() < 5):
      precio: float = float(input("Introduce un precio: "))
      lista_precios.append(precio)

  for precio in lista_precios:
      total += precio

  media_precios = total / lista_precios.__len__()

  print(f"Precio Medio de la lista: {media_precios} €")