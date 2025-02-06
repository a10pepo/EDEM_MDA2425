'''
    ---------- RETO 3 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
El nuevo gobierno ha decidido replantear el sistema de 
    pago de impuestos. Ha pensado que a partir de ahora:

    - si una persona es mayor de 16 años y menor de 70 ésta debe pagar impuestos.

    - En caso de no tener ingresos iguales o superiores a 800€ se
    acumulará una deuda mensual del 10%.

    - Si supera los 800€, pero no llega a los 2000€,
    deberá pagar un impuesto del 30% mensual

    - Si supera los 2000€ esta persona deberá pagar el 50%
    en concepto de impuestos

    - si la persona es menor de 16 años,
    no tiene que pagar impuestos

Escribe un programa capaz de calcular la cantidad de impuestos, o endeudamiento,
de una lista de personas durante un año entero (12 meses).

'''




def reto3Avanzado():
    edad = int(input('Introduce tu edad: '))
    sueldo_mensual: int = 0
    deuda_mensual: int = 0
    impuestos_mensual: int = 0
    
    if(edad < 16 or edad > 70):
        print('No tienes que pagar impuestos.')
    else:
        sueldo_mensual = int(input('Inroduce tu salario: '))
        if(sueldo_mensual <= 800):
            deuda_mensual = sueldo_mensual * 0.10
            print(f"Con una edad de {edad} y unos ingresos de {sueldo_mensual},acumularás una deuda con el Estado de{deuda_mensual*12}€ este año")
        elif(sueldo_mensual > 800 and sueldo_mensual < 2000):
            impuestos_mensual = sueldo_mensual * 0.30
            print(f"Con una edad de {edad} y unos ingresos de {sueldo_mensual}, debes pagar {impuestos_mensual*12}€ en impuestos este año")
        else:
            impuestos_mensual = sueldo_mensual * 0.50
            print(f"Con una edad de {edad} y unos ingresos de {sueldo_mensual}, debes pagar {impuestos_mensual*12}€ en impuestos este año")