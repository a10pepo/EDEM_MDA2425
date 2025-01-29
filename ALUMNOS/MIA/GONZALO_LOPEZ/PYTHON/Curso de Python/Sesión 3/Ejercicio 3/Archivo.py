# Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no.
lista_anyos = [2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030]

def es_bisiesto (n):
    if ( n % 4 == 0 and n % 100 != 0 ) or (n % 400 == 0):
        return True
    else :
        return False

for año in lista_anyos :
    if es_bisiesto(año) :
        print (f'El año {año} es bisiesto')   
    else :
        print (f'El año {año } no es bisiesto')