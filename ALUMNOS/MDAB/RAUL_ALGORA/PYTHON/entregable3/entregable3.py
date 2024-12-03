
# CALCULADORA

def calcular_inversion():
    x= int(input('Hola. Bienvenido al sistema de cálculo de inversiones. ¿Cuánto quieres invertir?'))
    y= float(input('¿cual es el interes anual?'))
    z= int(input('¿cuantos años vas a mantener la inversión'))


    interes_generado = x * (1 + y) ** z
    print(f'En {z} años habras generado {interes_generado} euros')



def mostrar_menu():
    while True: 
        print('HOLA. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?')
        print('[1] Calcular una inversión')
        print('[X] Salir')

        opcion= input('selecciona una opcion: ') .strip() .upper()
        
        if opcion == '1':
            calcular_inversion()
        elif opcion == 'X':
            print('saliendo del sistema. Hasta luego!')
            break
        else: 
            print('opcion invalida')

mostrar_menu()

# PROGRAMA DE NUMEROS PRIMOS 

for i in range(2,101):
    es_primo= True
    for num in range(2, i):
        if i % num == 0:
            es_primo= False
            break
    if es_primo:
        print(i)

# PROGRAMA AÑOS BISISESTOS


def esbisiesto(anyo: int) -> None: 
     #condición de si el año es bisiesto
     if (anyo%400 == 0):
         print(f'{anyo} es bisiesto')
     elif (anyo%100 == 0):
         #condicion en la que no lo sea 
         print(f'- {anyo} no es bisiesto')
     elif (anyo % 4 == 0):
         print(f'- {anyo} es bisiesto')
     else: 
         print (f'- {anyo} no es bisiesto')

lista_anyos = range(2020, 2030)

for anyo in lista_anyos:
     esbisiesto(anyo)
