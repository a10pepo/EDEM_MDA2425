'''
    ---------- RETO 4 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa que sea capaz de mostrar los elementos de una lista en orden inverso al original.
Por ejemplo: teniendo [1,2,3,4,5] el programa debe mostrar por pantalla [5,4,3,2,1]
'''

def reto4Basico():
  lista: [int] = [1,2,3,4,5]
  lista_inversa: [int] = reversed(lista)

  print(lista_inversa)

  for i in lista_inversa:
      print(f"- {i}")