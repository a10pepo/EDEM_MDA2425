

# 1. A la aplicación de la calculadora de inversión, deberás añadirle una opción para salir de la consola.

def calcular_inversion () :

    # Solicitar datos

    inversion_inicial = float (input ("¿Cuánto quieres invertir? (en €):"))

    interes_anual = float (input ("¿Cuál es el interés anual? (en %):"))

    años = int (input ("¿Cuántos años vas a mantener la inversión?:"))

    # Calcular y mostrar el resultado

    cantidad_final = inversion_inicial * (1+ interes_anual/100) ** años

    interes_generado = cantidad_final - inversion_inicial

    print (f"\nEn {años} años, habrás recibido {interes_generado:.2f}€ de intereses.")


def menu () :
    
    print("Hola. Bienvenido al sistema de cálculo de inversiones.")  # Saludo inicial.

    while True:
        
        # Menú principal.
        
        opcion = input("\n¿Qué quieres hacer?\n[1] Calcular una inversión.\n[X] Salir.\nElige una opción: ").upper()

        if opcion == "1":
           
            # Si elige calcular, ejecutamos la función de inversión.
            
            while True:
                calcular_inversion()  # Realizar el cálculo.

                # Preguntar después de calcular si desea hacer otra inversión o salir.
                
                siguiente_opcion = input("\n¿Qué quieres hacer ahora?\n[1] Calcular una nueva inversión\n[X] Salir\nElige una opción: ").upper()

                if siguiente_opcion == "1":
                    
                    # Si elige 1, volvemos a preguntar por los datos de la inversión.
                    
                    continue  # Vuelve al bucle de cálculo de inversión.
                
                elif siguiente_opcion == "X":
                    
                    print("¡Nos vemos!")  # Mensaje de despedida.
                    
                    return  # Termina la ejecución del programa.
                
                else:
                    
                    print("Opción no válida. Elige 1 para calcular o X para salir.")
                    
                    break  # Si no es válida, rompemos el ciclo y regresamos al menú inicial.
        elif opcion == "X":
            
            print("¡Nos vemos!")  # Mensaje de despedida
            
            break  # Salir del bucle y terminar el programa
        
        else:
            
            print("Opción no válida. Elige 1 para calcular o X para salir.")


        

# Llamada inicial a la función menu para comenzar el programa

menu()





# 2. Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100.

for num in range(2, 101):  # Recorre los números del 2 al 100.
    
    es_primo = True  # Asumimos que el número es primo.

    for i in range(2, num):  # Comprobamos si num es divisible por algún número entre 2 y num-1.
       
        if num % i == 0:  # Si es divisible, no es primo.
            
            es_primo = False
            
            break  # Salimos del bucle si encontramos un divisor.

    if es_primo:  # Si es primo, lo mostramos.
        
        print(num)





# 3. Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no.

def es_bisiesto(año):
    
    return (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0))

años = [2000, 2001, 2004, 1900, 2020, 2100]

for año in años:
    
    print(f"{año}: {'Bisiesto' if es_bisiesto(año) else 'No bisiesto'}")




