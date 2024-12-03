# # A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:

# # Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos

def es_primo (n):
    if n < 2 :
        return False  # el 1 no es PRIMO

    if n ==2 :
        return True  
    
    for i in range(2,n):
        if n % i == 0 :
            return False  # si el numero se puede divir por algun numero y el modulo es 0, NO ES PRIMO
    return True

def mostrar_primos(inicio, fin):
    for num in range(inicio, fin + 1):
        if es_primo(num):
            print(num)

mostrar_primos(2,24)



# Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no

def es_primo (n):
    if n < 2 :
        return False  # el 1 no es PRIMO

    if n ==2 :
        return True  
    
    for i in range(2,n):
        if n % i == 0 :
            return False  # si el numero se puede divir por algun numero y el modulo es 0, NO ES PRIMO
    return True

numero = int(input('Introduce un numero aleatorio para verificar si es primo o no :'))

if es_primo(numero) == True :
    print(f'El numero {numero} es primo')

else :
    print(f'Elnumero {numero} no es primo')  


# Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.

def es_bisiesto (n):
    if ( n % 4 == 0 and n % 100 != 0 ) or (n % 400 == 0):
        return True
    else :
        return False
    
año = int(input('Introduce un año aleatorio para ver si es bisiesto o no :'))

if es_bisiesto(año)== True :
    print(f'El año {año} es bisiesto')
else :
    print(f'El año {año} no es bisiesto')