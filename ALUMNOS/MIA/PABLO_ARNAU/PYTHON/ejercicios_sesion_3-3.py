def esBisiesto(anyo: int) -> None: 
    if  (anyo%400 == 0 and anyo%100 == 0) or (anyo%4 == 0 and anyo%100 != 0):
        print (f'El año {anyo} es bisiesto')
    else:
        print (f'{anyo} no es bisiesto')


a = int(input ('Dame una año de inicio:'))
b = int(input ('Dame un año de fin:'))

lista_anyos2 = range (a,b)

for anyo in lista_anyos2:
    esBisiesto (anyo)