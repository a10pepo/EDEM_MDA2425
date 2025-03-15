#Programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no.

anios= [1997, 2016, 2020, 2024, 2028]

for anio in anios:
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        print(f'{anio} es un año bisiesto')
    else:
        print(f'{anio} no es un año bisiesto')

