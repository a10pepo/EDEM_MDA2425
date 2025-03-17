def esbisiesto(anyo:int) -> None:
    if (anyo %4 == 0 and anyo %100 != 0) or anyo %400 == 0:   
        print(f'-{anyo} es bisiesto')
    else:
        print(f'-{anyo} no es bisiesto')

lista_anyos = [2020, 2026, 2028]

for anyo in lista_anyos:
    esbisiesto(anyo)