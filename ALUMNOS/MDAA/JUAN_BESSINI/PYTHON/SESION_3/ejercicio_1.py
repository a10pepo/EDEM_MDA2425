#by Juan Bessini
import sys

def calcular_inversion():
    while True:
        print("\n¿Qué quieres hacer?")
        print("[1] Calcular una inversión")
        print("[X] Salir")
        opcion = input("Selecciona una opción: ").strip().upper()
        
        if opcion == "1":
            print("\n¡Bienvenido al simulador de inversiones!")
            
            while True:
                try:
                    capital_inicial = float(input("Introduce el monto inicial de inversión (por ejemplo, 1000) o [X] para salir: "))
                except ValueError:
                    if input("¿Quieres salir? [X] para salir o Enter para continuar: ").strip().upper() == "X":
                        print("¡Nos vemos!")
                        sys.exit()
                    print("Entrada no válida. Introduce un número válido.")
                    continue
                if capital_inicial < 0:
                    print("El monto no puede ser negativo. Inténtalo de nuevo.")
                    continue
                break
            
            while True:
                try:
                    tasa_interes = float(input("Introduce el porcentaje de interés anual (por ejemplo, 5 para 5%) o [X] para salir: ")) / 100
                except ValueError:
                    if input("¿Quieres salir? [X] para salir o Enter para continuar: ").strip().upper() == "X":
                        print("¡Nos vemos!")
                        sys.exit()
                    print("Entrada no válida. Introduce un número válido.")
                    continue
                if tasa_interes < 0:
                    print("El interés no puede ser negativo. Inténtalo de nuevo.")
                    continue
                break
            
            while True:
                try:
                    duracion = int(input("¿Durante cuántos años planeas invertir? (por ejemplo, 10) o [X] para salir: "))
                except ValueError:
                    if input("¿Quieres salir? [X] para salir o Enter para continuar: ").strip().upper() == "X":
                        print("¡Nos vemos!")
                        sys.exit()
                    print("Entrada no válida. Introduce un número entero válido.")
                    continue
                if duracion < 0:
                    print("El número de años no puede ser negativo. Inténtalo de nuevo.")
                    continue
                break
            
            monto_final = capital_inicial * (1 + tasa_interes) ** duracion
            beneficio = monto_final - capital_inicial
            
            print(f"\nDespués de {duracion} años, tu inversión inicial de {capital_inicial:.2f}€ habrá crecido hasta {monto_final:.2f}€, generando un beneficio de {beneficio:.2f}€.")
            
        elif opcion == "X":
            print("¡Nos vemos!")
            sys.exit()
        
        else:
            print("Opción no válida. Por favor, introduce 1 para calcular o X para salir.")

# Ejecutar la aplicación
calcular_inversion()
