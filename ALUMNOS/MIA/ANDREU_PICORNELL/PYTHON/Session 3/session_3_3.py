# Funcion para saber si un año es bisesto
def esBisiesto(anyo: int) -> None:
    if anyo % 4 == 0:
        if anyo % 100 == 0:
            if anyo % 400 == 0:
                print(f"{anyo} es bisiesto")
            else:
                print(f"{anyo} no es bisiesto")
        else:
            print(f"{anyo} es bisiesto")
    else:
        print(f"{anyo} no es bisiesto")

lista_anyos = [2001,2002,2003,2004,2005,2006,2007,2008,2009]

for anyo in lista_anyos:
    esBisiesto(anyo)