def año_bisiesto():
    año = int(input('¿Qué año quieres probar?:'))
    bisiesto = False
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        bisiesto= True

    if bisiesto:
        print(f'El año {año} es bisiesto')
    else:
        print(f'El año {año} no es bisiesto')

año_bisiesto()