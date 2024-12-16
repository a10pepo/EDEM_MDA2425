#Función para saber si un año es bisiesto

def esBisiesto(anyo: int) -> None:
    if(anyo % 4 == 0 and anyo%100!=0 or anyo%400==0):
        print(f"{anyo} es bisiesto")
    else:
        print(f"{anyo} no es bisiesto")


lista_anyos=range(2000,2025)

for anyo in lista_anyos:
    esBisiesto(anyo)
