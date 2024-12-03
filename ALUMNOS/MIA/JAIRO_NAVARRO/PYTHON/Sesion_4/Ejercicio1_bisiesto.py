def esbisiesto(anyo:int):
    if (anyo %4 == 0 and anyo %100 != 0) or anyo %400 == 0: 
        return True
    else: 
        return False

lista_anyos = range (2020, 2026)

for anyo in lista_anyos:
    if esbisiesto(anyo) == True:
        print(f'{anyo} es bisiesto')
    else:
        print(f'{anyo} no es bisiesto')