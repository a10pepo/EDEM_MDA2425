'''
    ---------- RETO 23 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    -------------------------------------------------
'''

'''
Investiga acerca de Counter del módulo collections y haciendo uso del siguiente diccionario, encuentra la moda en las puntuaciones de películas:

misPeliculas = {'PeliculaA':81, 'PeliculaB':83, 'PeliculaC':87}
'''
from collections import Counter

def reto23Avanzado():

  puntuacion = Counter({'PeliculaA':81, 'PeliculaB':83, 'PeliculaC':87})
  print(puntuacion.most_common())