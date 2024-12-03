
def es_bisiesto(anyo):
    return anyo % 4 == 0 and (anyo % 100 != 0 or anyo % 400 == 0)

anyos = range(2000, 2100)
for anyo in anyos:
    if es_bisiesto(anyo):
        print(f"{anyo} es bisiesto")
    else:
        print(f"{anyo} no es bisiesto")