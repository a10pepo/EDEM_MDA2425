'''
    ---------- RETO 9 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
'''

numero_decimal = 10
numero_binario = 0b1010

def dec_a_bin(decimal: float):
    return bin(decimal)
    
def bin_a_dec(binario):
    return float(binario)

def reto9Avanzado():
  print(f'El número {numero_decimal} en binario sería: {dec_a_bin(numero_decimal)}')

  print(f'El número binario {str(numero_binario)} es el número: {bin_a_dec(numero_binario)}')