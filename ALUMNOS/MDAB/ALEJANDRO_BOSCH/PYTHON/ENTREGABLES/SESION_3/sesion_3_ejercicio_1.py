#ejercicio 1

print("Hola. Bienvenido al sistema de cálculo de inversiones.")

    
def calcular_inversion():
    
    cantidad_inv = float(input("¿Cuánto quieres invertir?: "))

    int_anual = float(input("¿Cuál es el interés anual (en porcentaje)?: "))

    int_anual = int_anual / 100

    cantidad_años = int(input("¿Cuántos años vas a mantener la inversión?: "))

    cantidad_generada = (cantidad_inv * (1 + int_anual) ** cantidad_años)

    cantidad_generada = round(cantidad_generada, 2)
    
    print(f"En {cantidad_años} años, habrás recibido {cantidad_generada}€.")


while True: 
    opcion = input('''¿Qué quieres hacer?
[1] Calcular una nueva inversión
[X] Salir: ''').strip().upper()
    
    if opcion == "1":
        calcular_inversion()  
    elif opcion == "X":  
        print("¡Nos vemos!")
        exit()
    else:
        print("Opción incorrecta, elija [1] o [X] para continuar.")


'''
Con el While True: se realiza un bucle infinito donde mientras la opcion sea "1"
 se calcula la funcion llamada, una vez se acaba, empieza de nuevo preguntando que se quiere hacer,
 en caso de pulsar "X" esta vez se terminaria el bucle ya que le hemos dicho que "exit()"
 '''


