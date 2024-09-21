'''
    ---------- RETO 26 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    -------------------------------------------------
'''

'''
Crea una función que reciba una palabra y sea capaz de devolver una palabra del revés.
'''

def reto26Avanzado():
  
  '''
  def reverso(palabra):
    if len(palabra) % 4 == 0:
        return ''.join(reversed(palabra))
    return palabra
  '''
  
  def reverso2(palabra):
    return ''.join(reversed(palabra))

  print(reverso2('Madrid'))
  print(reverso2('Valencia'))