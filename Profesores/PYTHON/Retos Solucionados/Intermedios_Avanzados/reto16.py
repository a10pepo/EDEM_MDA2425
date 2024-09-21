'''
    ---------- RETO 16 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Partiendo de la siguiente lista de tuplas:

miLista = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

Actualiza la lista sin aquellas tuplas que estén vacías.
'''

def reto16Avanzado():
  miLista = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

  miLista = [tupla for tupla in miLista if tupla]

  print(miLista)