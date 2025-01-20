import sys  # Para usar sys.exit()

def calcular_inversion():
    # Pedir el capital inicial con un bucle que captura el error de valor
    while True:
        try:
            capital_inicial = int(input("¿Cuánto quieres invertir? (Introduce un número entero sin símbolos ni puntos, como por ejemplo 1000) [X para salir]: "))
            break
        except ValueError:
            entrada = input("Por favor, introduce un número entero válido o escribe X para salir: ").strip().upper()
            if entrada == "X":
                print("¡Nos vemos!")
                sys.exit()
    
    # Pedir el interés anual con un bucle que captura el error de valor
    while True:
        try:
            interes_anual = float(input("¿Cuál es el interés anual? (Introduce un número decimal, por ejemplo: 0.05 para 5%) [X para salir]: "))
            break
        except ValueError:
            entrada = input("Por favor, introduce un número decimal válido o escribe X para salir: ").strip().upper()
            if entrada == "X":
                print("¡Nos vemos!")
                sys.exit()
    
    # Pedir el número de años con un bucle que captura el error de valor
    while True:
        try:
            años = int(input("¿Cuántos años vas a mantener la inversión? (Introduce un número entero como 5) [X para salir]: "))
            break
        except ValueError:
            entrada = input("Por favor, introduce un número entero válido o escribe X para salir: ").strip().upper()
            if entrada == "X":
                print("¡Nos vemos!")
                sys.exit()

    # Cálculo de la inversión
    capital_final = capital_inicial * (1 + interes_anual) ** años
    interes_generado = capital_final - capital_inicial

    # Resultado final
    print(f"En {años} años habrás generado {interes_generado:.2f}€ de interés.")
    print("")

def menu_principal():
    while True:
        print("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")
        print("[1] Calcular una inversión")
        print("[X] Salir")
        opcion = input("Elige una opción (1 o X): ").strip().upper()

        if opcion == "1":
            calcular_inversion()
            while True:
                print("¿Qué quieres hacer ahora?")
                print("[1] Calcular una nueva inversión")
                print("[X] Salir")
                nueva_opcion = input("Elige una opción (1 o X): ").strip().upper()
                if nueva_opcion == "1":
                    calcular_inversion()
                elif nueva_opcion == "X":
                    print("¡Nos vemos!")
                    sys.exit()
                else:
                    print("Opción no válida. Por favor, elige 1 o X.")
        elif opcion == "X":
            print("¡Nos vemos!")
            sys.exit()
        else:
            print("Opción no válida. Por favor, elige 1 o X.")

# Ejecutar el programa
menu_principal()
