# Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no.
import random

random_years = random.sample(range(1800, 2101), 10)

for year in random_years:
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f'El año {year} es bisiesto')
    else:
        print(f'El año {year} no es bisiesto')