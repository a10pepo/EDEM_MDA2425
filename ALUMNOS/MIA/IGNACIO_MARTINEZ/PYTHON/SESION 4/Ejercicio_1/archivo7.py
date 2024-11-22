#Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos

def mostrar_primos_en_rango(inicio, fin):
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            print(numero)

mostrar_primos_en_rango(1, 20)

#Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

print(es_primo(17))  
print(es_primo(4))   

#Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.

def es_bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

print(es_bisiesto(2000))  


