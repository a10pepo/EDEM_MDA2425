
lista_Años= [1820,1950,1930,1955,1980,1992,2000,2010,2024,2050,2100]

#Realizamos un bucle que itere sobre los diversos años
for años in lista_Años:

#Realizamos una condicion para conocer si un año es bisiesto o no
    if( años % 4 == 0 and años % 100 != 0) or (años % 400 == 0):

        print(f'El año {años} es bisiesto')
    
    else:
        print(f' El año {años} no es bisiesto')