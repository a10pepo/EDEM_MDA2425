while True:
    print("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")
    print("[1] Calcular una inversión")
    print("[X] Salir")
    opcion = input("Elige una opción (1 o X): ").strip().upper()
    if opcion=='1':
        try: 
            monto_inversion= float(input('¿Cuanto quieres invertir? :' ))
            interes= float(input('¿Que porcentaje quieres invertir? Debe estar comprendido entre 0 y 1:' ))
            anios= int(input('¿Cuantos años lo quieres mantener?:' ))

            interes_simple= monto_inversion*interes*anios
            print('El interes en años es:', interes_simple)
        except ValueError:
            print("Por favor, introduce números válidos")
    
    elif opcion=='X' :
        print('Nos vemos')
        break