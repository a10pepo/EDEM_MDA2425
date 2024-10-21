def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    return False

def mostrar_bisiestos(inicio,fin):
    for año in range(inicio,fin+1):
        if es_bisiesto(año):
            print(f"El año {año} es bisiesto")

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def mostrar_primos(inf, sup):
    for numero in range(inf,sup+1):
        if es_primo(numero):
            print(f"El número {numero} es primo")


if __name__=="__main__":
    print("Dime un intervalo de valores.")

    while True:
        try: 
            num1: int = int(input("Num 1: "))
            num2: int = int(input("Num 2: "))
            break
        except ValueError:
            print("Introduce numeros.")

    if(num1>num2):
        sup: int = num1
        inf: int = num2
    else:
        sup: int = num2
        inf: int = num1
    
    mostrar_primos(inf,sup)

    print("Dime un intervalo de años.")

    while True:
        try:
            año1: int = int(input("Dime un año: "))
            año2: int = int(input("Dime otro año: "))
            break
        except ValueError:
            print("Introduce números.")

    if(año1>año2):
        sup: int = año1
        inf: int = año2
    else:
        sup: int = año2
        inf: int = año1
    
    mostrar_bisiestos(inf,sup)