''' 
Hola Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?
> [1] Calcular una inversión
> [X] Salir
> (Aquí el usuario deberá escribir 1 o X. Ningón otro valor será considerado como válido. Saliendo el mismo mensaje si introduce algo distinto a 1 o X)
'''
print("Hola Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")
while True:
    print("> [1] Calcular una inversión")
    print("> [X] Salir")
    inicio=input(">")
    if inicio=='1':
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
    elif inicio=='X':
        print('¡Nos vemos!')
        exit()
    else:
        print('Introduce una de las dos opciones')

'''
En caso de escribir 1 --> Se deberá proceder al sistema de Cálculo de inversión. En todas las pantallas posteriores, se debe mostrar la opción de [X] Salir

> En [N] años habrás recibido [X]€ de interés. ¿Qué quieres hacer ahora?
> [1] Calcular una nueva inversión
> [X] Salir
En caso de escribir X --> La aplicación debe mostrar un mensaje de despedida y cerrarse:

> ¡Nos vemos!
> (aplicación cerrada con un exit())

'''





