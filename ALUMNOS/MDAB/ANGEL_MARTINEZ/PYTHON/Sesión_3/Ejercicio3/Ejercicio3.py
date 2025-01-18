
inicio = int(input("¿Desde que año quiere usted comprobar si es bisiesto?"))
final = int(input("¿Hasta que año quiere comprobar si es bisiesto?"))

def esBisiesto(anyo: int) -> None:
    if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 400 == 0):
        return True
    return False

print(f"\nAños bisiestos entre {inicio} y {final}:")
for anyo in range(inicio, final + 1):  
    if esBisiesto(anyo):
        print(f"{anyo} es bisiesto")
    else:
        print(f"{anyo} no es bisiesto")
