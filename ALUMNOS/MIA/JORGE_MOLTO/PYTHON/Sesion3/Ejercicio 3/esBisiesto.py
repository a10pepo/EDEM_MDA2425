def esBisiesto(anyo: int):
    if((anyo % 4 == 0 and anyo % 100 != 0) or anyo % 400 == 0):
        print(f'- {anyo} es bisiesto.')
    else:
        print(f'- {anyo} no es bisiesto.')

lista_anyos_bisiestos = [2012, 2016, 2020, 2021, 2022, 2024, 2025, 2026]

for anyo in lista_anyos_bisiestos:
    esBisiesto(anyo)        