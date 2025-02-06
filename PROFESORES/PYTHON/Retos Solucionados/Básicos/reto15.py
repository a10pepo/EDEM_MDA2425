'''
    ---------- RETO 15 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
'''

def doble (lista:[int]) -> [int]:
    for i, numero in enumerate(lista):
        lista[i] *=2

def reto15Basico():
  miLista = [10,50,100]
  # Lo pasaremos por referencia
  doble(miLista)
  print(f"Lista Original Modificada: {miLista}") #[20, 100, 200]