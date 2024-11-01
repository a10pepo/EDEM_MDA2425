## 3
def esBisiesto(year:int) -> None:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
        print(f'{year} es bisiesto')
    else :
        print(f' - {year} no es bisiesto')


if __name__== "entregable3bisiesto.py":
    lista_year = [2020, 2021, 2022, 2023, 2024, 2025]
    for year in lista_year:
        esBisiesto(year)
    
