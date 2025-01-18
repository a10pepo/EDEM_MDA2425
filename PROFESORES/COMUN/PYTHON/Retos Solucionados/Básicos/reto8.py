'''
    ---------- RETO 8 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa que pueda decirte si un número (número entero) es primo o no
'''

'''
Número Primo: Aquellos números que son
únicamente divisibles entre sí mismos y 1
Son mayores que 1: 
[2, 3, 5, 7, 11, 13, 17, 19, 23, etc. ]
'''

def reto8Basico():
  numero: int = int(input('Introduce un número entero: '))

  if numero > 1:
      # Buscamos los factores de número
      for i in range(2,int(numero)):
          if (int(numero) % i) == 0:
              print(f"Lo siento, el número {numero} NO ES PRIMO. Es divisible entre {i}")
              break
      else:
          print(f"¡ENHORABUENA!, el número {numero} ES PRIMO")
  else:
      print(f"Lo siento, el número {numero} NO ES PRIMO. Los números primos son mayores que 1")