# #EJERCICIO 1 
while (True): 
    respuesta = input('Hola. Bienvenido al sistema de calculo de inversiones. ¿Que quieres hacer?:\n'
        '[1] : Calcular una inversion\n'
        '[X] : Salir\n'                 
).strip().upper()

    if respuesta == '1':
        try:
            inversion= int(input('Introduce tu inversion inicial:'))
            interes_anual = int(input('Introduce el interes anual :'))
            años = int(input ('Introduce el numero de años que dura la inversion :'))

            retorno_total = inversion * (1 + interes_anual/100)**años
            beneficio = retorno_total - inversion
            print(f'En {años} años habras recibido {beneficio} € de interes')
        except ValueError :
            print ('Error : Por favor introduce datos validos.')

    elif respuesta == 'X':
        print('Hasta luego!!')
        break

    
    else :
        print (input('No has introducido un dato valido. Vuelve a intentarlo:'))