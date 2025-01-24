#Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos

def mostrar_primos_en_rango(inicio, fin):
    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            print(numero)

mostrar_primos_en_rango(1, 100)


#Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

print(es_primo(7))  

#Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.
def es_año_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    return False

print(es_año_bisiesto(2024))  # True
print(es_año_bisiesto(1900))  # False
print(es_año_bisiesto(2000))  # True
