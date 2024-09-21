'''
    ---------- RETO 18 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Crea una función que sea capaz de eliminar un caracter concreto de una cadena de texto.
'''

def eliminar(str, n):
    inicio = str[:n] 
    final = str[n+1:]
    return inicio + final

def reto18Basico():
  print(eliminar('Madrid', 0)) #adrid
  print(eliminar('Madrid', 3)) #Madid
  print(eliminar('Madrid', 5)) #Madri
