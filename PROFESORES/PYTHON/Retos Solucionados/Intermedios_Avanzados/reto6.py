'''
    ---------- RETO 6 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Reto 6
Escribe un programa que pida al usuario una palabra por consola y devuelva si se trata de un palíndormo*

* Palíndromo: Palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda
'''

def reto6Avanzado():
  palabra = input("Ingrese una palabra: ")
  inversa = palabra[::-1]

  if palabra == inversa:
      print("Palindromo")
  else:
      print("No palindromo")