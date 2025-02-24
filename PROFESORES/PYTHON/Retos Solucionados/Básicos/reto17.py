'''
    ---------- RETO 17 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Partiendo de la siguiente tupla:
tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
Realiza las siguientes operaciones:

- Encontrar los elementos de 3 a 5
- Encontrar los 6 primeros elementos
- Muestra la tupla desde el 5 elemento hasta el final
- Muestra toda la tupla haciendo uso de [:]
- Muestra todos los elementos desde la posición 2 a la 9 de dos en dos
- Devuelve la tupla con un salto cada 4 elementos
- Usa un step negativo para mostrar la tupla desde la posición 9 a la 2
'''

def reto17Basico():
  tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

  # Elementos 3 a 5
  # tupla [start:stop]
  _slice = tupla[3:5]
  print('1-', _slice)

  # Primeros 6 elementos
  # Si no se define un start, se toma desde el principio
  _slice = tupla[:6]
  print('2-',_slice)

  # Desde 5 Hasta el final
  _slice = tupla[5:]
  print('3-',_slice)

  # Toda la Tupla
  _slice = tupla[:]
  print('4-',_slice)

  # Los índices se pueden definir con valores negativos
  _slice = tupla[-8:-4]
  print('5-',_slice)

  # Reformulando la tupla
  tupla = tuple("HELLO WORLD")
  print('6-',tupla)

  # tupla[start:stop:step]
  _slice = tupla[2:9:2]
  print('7-',_slice)

  # Devuelve una tupla con un salto cada 4 elementos
  _slice = tupla[::4]
  print('8-',_slice)

  # Cuando tenemos el Step negativo, va desde atrás
  _slice = tupla[9:2:-4]
  print('9-',_slice)