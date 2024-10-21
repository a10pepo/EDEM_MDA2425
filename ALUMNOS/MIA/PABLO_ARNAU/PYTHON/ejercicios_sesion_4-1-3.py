def esBisiesto(anyo: int): 
    if  (anyo%400 == 0 and anyo%100 == 0) or (anyo%4 == 0 and anyo%100 != 0):
        bisiesto = True
    else:
        bisiesto = False
    return bisiesto

anyo = int(input ('Dame una año para comprobar si es bisiesto o no:'))
resultado = esBisiesto(anyo)

print (f' El número {anyo} es bisiesto: {resultado}')
