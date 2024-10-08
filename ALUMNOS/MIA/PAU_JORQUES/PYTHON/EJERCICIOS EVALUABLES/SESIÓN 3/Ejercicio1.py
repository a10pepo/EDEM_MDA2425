def calcular_inversion(cantidad_ini, interes, años):
    return float(cantidad_ini) * (1 + float(interes))**float(años)


print("Hola. Bienvenido al sistema de cálculo de inversiones.")
print("[1] Calcular una inversión")
print("[X] Salir")

aux: str  = input()

while(aux != "X" and aux != "1"):
    print("[1] Calcular una inversión")
    print("[X] Salir")
    aux: str = input()

if(aux == "X"):
    print("¡Nos vemos!")
    exit()

print("¿Cuánto quieres invertir?")
cantidad: int =  input()
print("¿Cuál es el interés anual?")
interes: float = float(input())
print("¿Cuántos años vas a mantener la inversión?")
años: int = input()

print(f"En {años} años habrás recibido {calcular_inversion(cantidad,interes,años)}€ de interés")

print("[1] Calcular una nueva inversión")
print("[X] Salir")
aux: str = input()

while(aux != "X"):
    if(aux == "1"):
        print("¿Cuánto quieres invertir?")
        cantidad: int =  input()
        print("¿Cuál es el interés anual?")
        interes: float = float(input())
        print("¿Cuántos años vas a mantener la inversión?")
        años: int = input()

        print(f"En {años} años habrás recibido {calcular_inversion(float(cantidad),float(interes),float(años))}€ de interés")

        print("[1] Calcular una nueva inversión")
        print("[X] Salir")
        aux: str = input()        
    else:
        print("[1] Calcular una nueva inversión")
        print("[X] Salir")
        aux: str = input()

if(aux == "X"):
    print("¡Nos vemos!")
    exit()
