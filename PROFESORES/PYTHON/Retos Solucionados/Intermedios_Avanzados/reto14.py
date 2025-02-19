'''
    ---------- RETO 14 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Partiendo de las siguientes cadenas de texto:

miCodigo = 'print("Hola Mundo")'
otroCodigo = 
"""

def multiplicar(x,y):   
  return x*y

print('Multiplica: 2 * 4: ',multiplicar(2,4))
"""

Haz uso de exec() para ejecutar ambas operaciones

'''

def reto14Avanzado():
  miCodigo = 'print("Hola Mundo")'
  otroCodigo = """
  def multiplicar(x,y):
      return x*y

  print('Multiplica: 2 * 4: ',multiplicar(2,4))
  """
  exec(miCodigo)
  exec(otroCodigo)