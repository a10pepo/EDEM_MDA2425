def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    return False

def mostrar_bisiestos(inicio,fin):
    for año in range(inicio,fin+1):
        if es_bisiesto(año):
            print(f"El año {año} es bisiesto.")
        else:
            print(f"El año {año} no es bisiesto.")

if __name__=="__main__":
    print("Dime un intervalo de años.")

    while True:
        try:
            año1: int = int(input("Dime un año: "))
            año2: int = int(input("Dime otro año: "))
            break
        except ValueError:
            print("Hay que introducir un numero.")

    if(año1>año2):
        sup: int = año1
        inf: int = año2
    else:
        sup: int = año2
        inf: int = año1
    
    mostrar_bisiestos(inf,sup)