#4. Ejercicios Sesión 4
#   1.A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
#       1.Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos

def primosenrango(inicio,fin):
    primo=[2,3,5]
    entrega=[]
    rango1=range(6,fin)
    rango2=range(inicio,fin)
    for i in rango1:
        for x in primo:
            if i % x == 0:
                break
            elif x==primo[-1]:
                primo.append(i)
    for x in primo:
        if x in rango2:
            entrega.append(x)

    print(f"Aqui tiene una lista de todos los números primos del {inicio} al {fin}:")
    print(entrega)


#       2.Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no

def isprimo(num):
    primo=[2,3,5]
    
    rango=range(6,num+1)
    for i in rango:
        for x in primo:
            if i % x == 0:
                if i==num:
                    return False
                break
            elif x==primo[-1]:
                if i==num:
                    return True
                else:
                    primo.append(i)

#       3.Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.

def es_bisiesto(year):
    if year % 4 != 0: 
        return False
    elif year % 4 == 0 and year % 100 != 0: #divisible entre 4 y no entre 100 o 400
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 10 y no entre 400
        return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400
        return True
    
