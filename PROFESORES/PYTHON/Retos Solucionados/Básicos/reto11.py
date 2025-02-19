'''
    ---------- RETO 11 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa que pida al usuario los siguientes datos por consola:
Título de la películaDirectorAñoPaísE introduzca esos valores en una variable GLOBAL llamada "pelicula".
'''

global pelicula

def reto11Basico():
  pelicula: dict = dict()

  pelicula['Titulo'] = input('Introduzca el TÍTULO de la película: ')
  pelicula['Director'] = input('Introduzca el DIRECTOR de la película: ')
  pelicula['Año'] = int(input('Introduzca el AÑO de la película: '))
  pelicula['País'] = input('Introduzca el PAÍS de la película: ')


  print(pelicula)