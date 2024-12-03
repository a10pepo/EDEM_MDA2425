def calcular_inversion():
    while True:
        # Paso 1
        print("\n ¡Bienvenido al sistema de cálculo de inversiones ")
        print("===========================================================")
        cantidad = float(input(" ¿Cuánto deseas invertir hoy? Escribe la cantidad aquí: "))

        # Paso 2
        print("\n ¡Perfecto! Ahora vamos a establecer el interés que recibirás ")
        interes_anual = float(input(" ¿Cuál es el porcentaje de interés anual? (escribe solo el número): "))

        # Paso 3
        print("\n ¡Casi terminamos! Ahora, solo necesitamos saber el tiempo ")
        anos = int(input(" ¿Cuántos años planeas mantener esta inversión? "))
        cantidad_final = cantidad * (1 + (interes_anual / 100)) ** anos
        intereses_generados = cantidad_final - cantidad

        # Paso 4 - Final
        print("\n ¡Listo! ")
        print("===========================================================")
        print(f"Después de {anos} años, habrás generado un interés total de:  {intereses_generados:.2f}€ ")
        print(f"Tu inversión inicial de {cantidad:.2f}€ se convertirá en:  {cantidad_final:.2f}€ ")
        print("===========================================================")

        opcion = input("\n¿Qué quieres hacer ahora?\n[1] Calcular una nueva inversión\n[X] Salir\n> ").upper()
        if opcion == "X":
            print("¡Nos vemos! ")
            exit()  
        elif opcion != "1":
            print("Opción no válida. Volviendo al menú principal...")
        else:
            continue

def main():
    while True:
        print("\n Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer? ")
        print("[1] Calcular una inversión")
        print("[X] Salir")
        opcion = input("> ").upper()

        if opcion == "1":
            calcular_inversion()
        elif opcion == "X":
            print("¡Nos vemos! ")
            exit() 
        else:
            print("Opción no válida. Por favor, introduce 1 o X.")
main()
