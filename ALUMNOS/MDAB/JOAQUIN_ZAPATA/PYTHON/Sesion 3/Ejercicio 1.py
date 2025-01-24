def calcular_inversion():
    while True:
        print("\nHola. Bienvenido al sistema de cálculo de inversiones.")
        print("[1] Calcular una inversión")
        print("[X] Salir")

        opcion = input("¿Qué quieres hacer? ").strip().upper()

        if opcion == "1":

            try:
                print("\nSistema de cálculo de inversión. Escribe 'X' en cualquier paso para salir.")
                
                cantidad_input = input("¿Cuánto quieres invertir? ")
                if cantidad_input.strip().upper() == "X":
                    print("¡Nos vemos!")
                    exit()
                cantidad = float(cantidad_input)

                interes_input = input("¿Cuál es el interés anual? ")
                if interes_input.strip().upper() == "X":
                    print("¡Nos vemos!")
                    exit()
                interes_anual = float(interes_input)

                años_input = input("¿Cuántos años vas a mantener la inversión? ")
                if años_input.strip().upper() == "X":
                    print("¡Nos vemos!")
                    exit()
                años = int(años_input)

                cantidad_generada = cantidad * (1 + (interes_anual / 100)) ** años
                intereses = cantidad_generada - cantidad

                print(f"\nEn {años} años habrás recibido {intereses:.2f}€ de interés.")
                print(f"El total de la inversión será de {cantidad_generada:.2f}€.")

                print("\n¿Qué quieres hacer ahora?")
                print("[1] Calcular una nueva inversión")
                print("[X] Salir")

                nueva_opcion = input("Elige una opción: ").strip().upper()
                if nueva_opcion == "X":
                    print("¡Nos vemos!")
                    exit()

            except ValueError:
                print("\nPor favor, introduce valores numéricos válidos.")
                continue

        elif opcion == "X":
            print("¡Nos vemos!")
            exit()
        else:
            print("\nPor favor, elige una opción válida (1 o X).")
            
calcular_inversion()
