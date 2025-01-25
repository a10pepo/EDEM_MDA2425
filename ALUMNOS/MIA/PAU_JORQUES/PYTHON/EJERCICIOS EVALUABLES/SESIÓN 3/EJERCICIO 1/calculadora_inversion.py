def calcular_inversion(cantidad_ini, interes, años) -> float:
    return float(cantidad_ini) * (1 + float(interes))**float(años)

def opciones() -> str:
    print("[1] Calcular una inversión")
    print("[X] Salir")
    return input()

def datos() -> tuple[int, int, int]: 
    print("¿Cuánto quieres invertir?")
    cantidad: int =  int(input())
    print("¿Cuál es el interés anual?")
    interes: float = float(input())
    while(interes < 0 or interes >1):
        print("El interes tiene que ir entre 0 y 1")
        interes: float = float(input("Introduce otro valor: "))
    print("¿Cuántos años vas a mantener la inversión?")
    años: int = int(input())
    return (cantidad, interes, años)

print("Hola. Bienvenido al sistema de cálculo de inversiones.")

aux: str  = opciones()

while(aux != "X" and aux != "1"):
    print("Valor introducido incorrecto.")
    aux: str = opciones()

if(aux == "X"):
    print("¡Nos vemos!")
    exit()

while True:
    try:
        cantidad, interes, años = datos()
        print(f"En {años} años habrás recibido {calcular_inversion(cantidad,interes,años)}€ de interés")
        break
    except ValueError:
        print("Valor introducido incorrecto. Tiene que ser números.")
    except OverflowError:
        print("No puedo calcular ese valor tan grande.")

aux: str = opciones()

while(aux != "X"):
    if(aux == "1"):
        while True:
            try:
                cantidad, interes, años = datos()
                print(f"En {años} años habrás recibido {calcular_inversion(float(cantidad),float(interes),float(años))}€ de interés")
                break
            except ValueError:
                print("Valor introducido incorrecto. Tiene que ser números.")
            except OverflowError:
                print("No puedo calcular ese valor tan grande.")
            
        aux: str = opciones()   
    else:
        print("Valor introducido incorrecto.")
        aux: str = opciones()

if(aux == "X"):
    print("¡Nos vemos!")
    exit()
