
lista_Años= [1820,1950, 1930, 1955, 1980,1992, 2000, 2010, 2024, 2050, 2100]


for años in lista_Años:
    if( años % 4 == 0 and años % 100 != 0) or (años % 400 == 0):
        print(f'El año {años} es bisiesto')
    
    else:
        print(f' El año {años} no es bisiesto')