def calcular_inversion(inversion, interes, años):
    inversion_final = inversion * (1 + interes / 100) ** años
    return inversion_final

def main():
    while True:
        try:
            print("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")
            print("[1] Calcular una inversión")
            print("[X] Salir")
            opcion = input("Elige una opción: ").strip().upper()

            if opcion == '1':
                while True:
                    try:
                        inversion = float(input("¿Cuánto quieres invertir?: "))
                        interes = float(input("¿Cuál es el interés anual?: "))
                        años = int(input("¿Cuántos años vas a mantener la inversión?: "))
                        
                        inversion_final = calcular_inversion(inversion, interes, años)
                        interes_ganado = inversion_final - inversion
                        
                        print(f"En {años} años habrás recibido {interes_ganado:.2f}€ de interés.")
                        print("¿Qué quieres hacer ahora?")
                        print("[1] Calcular una nueva inversión")
                        print("[X] Salir")
                        opcion = input("Elige una opción: ").strip().upper()
                        
                        if opcion == 'X':
                            print("¡Nos vemos!")
                            exit()
                        elif opcion != '1':
                            print("Opción no válida. Por favor, elige una opción válida.")
                    except ValueError:
                        print("Error: Introduce un número válido")
            elif opcion == 'X':
                print("¡Nos vemos!")
                exit()
            else:
                print("Opción no válida. Por favor, elige una opción válida.")
        
        except ValueError:
            print("Error: Introduce un número válido")

if __name__ == "__main__":
    main()