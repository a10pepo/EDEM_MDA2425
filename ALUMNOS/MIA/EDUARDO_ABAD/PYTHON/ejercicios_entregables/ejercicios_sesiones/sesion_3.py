user_selection=input('Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer? \n [1] Calcular una inversión \n [X] Salir')
if user_selection  =='X' or user_selection == 'x':
    print('¡Nos vemos!')
    exit()
elif user_selection == '1':
    cantidad_inicial=float(input('¿Cuánto dinero quieres invertir? '))
    interés_anual=float(input('¿Cuál es el interés anual? '))/100
    años=int(input('¿Cuántos años vas a mantener la inversión? '))
    dinero_acumulado=cantidad_inicial*(1+interés_anual)

    for i in range(años):
        dinero_acumulado=dinero_acumulado*(1+interés_anual)
    
    print(f'En {años} años habrás recibido {dinero_acumulado:.2f}€ de interés. ¿Qué quieres hacer ahora? \n\n [1] Calcular una nueva inversión \n [X] Salir')
else:
    ValueError
    print('Escribe un valor que sea correcto (1 o X)')