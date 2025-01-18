# Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
def evalua_primo_en_array(array_nums: int)-> None:
    for num in array_nums:
       if es_primo(num) == True:
           print(num)

# Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no
def es_primo(num: int) -> bool:
    if num < 2:
        return False

    for i in range(2,num):
        if (num % i) == 0:
            return False
    return True

# Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.
def es_bisiesto(anyo: int) -> None:
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
