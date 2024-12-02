def esBisiesto(anyo: int):
    if((anyo % 4 == 0 and anyo % 100 != 0) or anyo % 400 == 0):
        print(True)
    else:
        print(False)

anio = int(input('Introduce un año para saber si es bisiesto: '))

esBisiesto(anio)