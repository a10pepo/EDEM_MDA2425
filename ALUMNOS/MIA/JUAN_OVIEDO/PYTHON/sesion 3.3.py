#Función para saber si un año es bisiesto
def esbisiesto(anyo: int,anyo2) -> None:
    y = range(anyo,anyo2)
    for anyo in y:
        if anyo % 4== 0 and anyo % 100 !=0 or (anyo % 400==0):
          print(f'{anyo} es bisiesto')
        else:
          print(f'-{anyo} no es bisiesto')



        




lista_anyos = [2020, 2021, 2022, 2023, 2024, 2025]
esbisiesto(1900,2000)