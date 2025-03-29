'''
Crea una aplicación de consola que calcule los resultados de una inversión. Debe
Pedir por consola una cantidad (numérica) de Inversión
Pedir el % de interés anual
Pedir el número de años que se va a mantener la inversión
Finalmente, calcular la cantidad generada en los años especificados por el usuario
Debería resultar en algo así vía consola:

Paso 1

> Hola. Bienvenido al sistema de cálculo de inversiones.
> ¿Cuánto quieres invertir?
> (EL usuario escribe aquí la cantidad)
'''
try:
    print("Hola. Bienvenido al sistema de cálculo de inversiones.")
    montante=float(input("¿Cuánto quieres invertir? "))

    '''
    Paso 2

    > ¿Cuál es el interés anual?
    > (EL usuario escribe aquí el interés anual)
    '''

    interes=float(input("¿Cuál es el interés anual en %? "))/100

    '''
    Paso 3

    > ¿Cuántos años vas a mantener la inversión?
    > (EL usuario escribe aquí el nº de años)
    '''

    n=int(input("¿Cuántos años vas a mantener la inversión? "))

    '''
    Paso 4 - Final

    > En [N] años habrás recibido [X]€ de interés
    > (Donde [N] debes sustituirlo por el número de años y [X] por la cantidad generada)
    '''

    print(f'En {n} años habrás recibido {n*interes*montante}€ de interés ')

except ValueError: 
    print('Debes introducir un número') #Si hay un value error sacamos el mensaje, para que no se pare el programa