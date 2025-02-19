'''
    ---------- RETO 29 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    -------------------------------------------------
'''

'''

Crea una función capaz de devolver el segundo valor numérico más pequeño de una lista de números.

'''

def segundoPeque(numeros):

    if (len(numeros)<2):
        return
    if ((len(numeros)==2)  and (numeros[0] == numeros[1]) ):
        return

    elementosDuplicados = set()
    elementosUnicos = []

    for x in numeros:
        if x not in elementosDuplicados:
            elementosUnicos.append(x)
            elementosDuplicados.add(x)
    elementosUnicos.sort()  
    return  elementosUnicos[1]   

def reto29Avanzado():
  print(segundoPeque([1, 2, -8, -2, 0, -3])) #3
  print(segundoPeque([1, 1, 0, 0, 2, -2, -2])) #0
  print(segundoPeque([1, 1, 1, 0, 0, 0, 2, -2, -4])) #-2
  print(segundoPeque([2,2])) #None
  print(segundoPeque([2])) #None