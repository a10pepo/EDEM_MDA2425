'''
    ---------- RETO 10 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa que guarde en una variable el siguiente contenido:
{'titulo':'El Más Allá','aka':'E tu vivrai nel terrore - Laldilà','director':'Lucio Fulci', 'año':1981, 'país':'Italia'}
'''

def reto10Basico():
  pelicula: dict = dict({
    'título': 'El Más Allá',
    'aka': 'E tu vivrai nel terrore - L\'aldilà',
    'director': 'Lucio Fulci',
    'año': 1981,
    'país': 'Italia'
  })

  print(f"- Nombre de la película {pelicula.get('título')}")
  print(f"- AKA de la película {pelicula.get('aka')}")
  print(f"- Director de la película {pelicula.get('director')}")
  print(f"- Año de la película {pelicula.get('año')}")
  print(f"- País de la película {pelicula.get('país')}")
