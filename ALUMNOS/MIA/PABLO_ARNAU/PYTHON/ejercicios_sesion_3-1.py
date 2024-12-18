while True:

    print(''' \n Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?
       1. Calcular una inversión
       X. Salir\n
       ''')
    opcion = input ()


    if opcion == '1':
        
        inversion = float (input ('¿Cuánto quieres invertir?\n'))
        interes = int (input ('¿Cuál es le interés anual?\n'))
        tiempo = int (input ('¿Cuántos años vas a mantener la inversión?\n'))

        dinero_generado = (inversion * ((1 + interes/100)**tiempo))- inversion

        print (f'En {tiempo} años habrás recibido {dinero_generado:.3f}€ de interés')

    elif opcion == 'X':
        print ('¡Nos vemos!')
        exit ()
    else:
        print('\n Opción incorrecta, selecciona 1 o X')  

