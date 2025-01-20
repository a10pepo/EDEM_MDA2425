def calcular_inversion():
    while True:
        # 
        print("¡Bienvenido al sistema de cálculo de inversiones ")
        cantidad = float(input(" ¿Cuánto deseas invertir hoy? Escribe la cantidad aquí: "))
        interes = float(input(" ¿Cuál es el porcentaje de interés anual? "))
        tiempo = int(input(" ¿Cuántos años planeas mantener esta inversión? "))
        Recibiriamos = cantidad * (1 + (interes / 100)) ** tiempo
        intereses_generados = Recibiriamos - cantidad

        print(f"Con los datos que me has proporcionado, podemos decir que en {tiempo} años, habrás generado un interés total de:  {intereses_generados}€. Por lo que tu inversión final sera de {Recibiriamos}€ ")

        opcion = input('''¿Quiere que le ayude con una nueva inversión o prefiere salir?
                       [1] Calcular una nueva inversión
                       [X] Salir>''').strip().upper()
        if opcion == "X":
            print("¡Nos vemos! ")
            exit()  
        elif opcion != "1":
            print("Opción no válida. Volviendo al menú principal...")
        else:
            continue

def main():
    while True:
        print("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer? ")
        print("[1] Calcular una inversión")
        print("[X] Salir")
        opcion = input("> ")

        if opcion == "1":
            calcular_inversion()
        elif opcion == "X":
            print("¡Nos vemos! ")
            exit() 
        else:
            print("Opción no válida. Por favor, introduce 1 o X.")
main()