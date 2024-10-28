#3. Ejercicios Sesión 3
#   3.Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no.

def es_bisiesto(year):
    if year % 4 != 0: 
        print(f"{year} no es bisiesto")
    elif year % 4 == 0 and year % 100 != 0: #divisible entre 4 y no entre 100 o 400
        print(f"{year} es bisiesto")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 10 y no entre 400
        print(f"{year} no es bisiesto")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400
        print(f"{year} es bisiesto")

lista=[2000,2024,1246,46,67]
for x in lista:
    es_bisiesto(x)