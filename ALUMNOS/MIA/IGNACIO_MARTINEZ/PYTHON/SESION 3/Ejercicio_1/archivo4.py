#Opción para salir de consola
while True:

    print('Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?\n'
       '1. Calcular una inversión\n'
       'X. Salir\n')
    
    opcion= input()

    if opcion == '1':
        inversion= float(input('Cuanto quieres invertir?\n'))
        interes= float(input('Cual es la tasa de interes anual?\n'))
        anios= float(input('Cuantos años vas a invertir?\n'))

        ingresos_netos= inversion * (1 + interes/100) ** anios - inversion
        print(f'Los ingresos netos son: {ingresos_netos}')

    elif opcion == 'X':
        print('Nos vemos!')
        exit()

    else:
        print('Opción no válida. Selecciona 1 o X.')
