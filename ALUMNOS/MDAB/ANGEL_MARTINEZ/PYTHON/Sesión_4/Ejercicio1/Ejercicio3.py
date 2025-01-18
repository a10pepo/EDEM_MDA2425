año = int(input("¿Que año quiere usted comprobar si es bisiesto?"))

def esBisiesto(anyo: int) -> None:
    if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 400 == 0):
        return True
    return False

print(f"\n¿El año {año} es bisiesto?:")
if esBisiesto(año):
        print(f"Verdadero")
else:
        print(f"Falso")
