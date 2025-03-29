'''
Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no.
'''
import math
def bisiesto (lista):
    bis = list(filter(lambda x: x % 4 == 0, lista))
    print(f'los años bisiestos son {bis}')
        

mi_lista=[2019,2018,1988,1954]

bisiesto(mi_lista)

