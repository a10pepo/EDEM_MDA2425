'''
    ---------- RETO 9 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no
'''

def reto9Basico():
  anio: int = int(input("Introduce un año y vamos a ver si es bisiesto... "))

  if(anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
      print(f"¡El año {anio} es bisiesto!")
  else:
      print(f"Lo sentimos. El año {anio} NO es bisiesto!")