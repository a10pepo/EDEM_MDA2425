
def Calculadora_Inversiones(): #Definimos una función
    while True: #Hacemos un bucle infinito
        print('Hola. Bienvenido al sistema de cálculo de inversiones')
        
        Cantidad = int(input(f'¿Cuanto quieres invertir?'))

        print('Ahora vamos a determinar el interes de la inversion')
        
        Porcentaje= float(input(f'¿Cual es el interes anual?(En decimal)'))

        Años= int(input(f'¿Cuantos años va a mantener la inversión?'))

        print('Procesando...')
        
        Total_compuesto = Cantidad * ((1 + Porcentaje / 100) ** Años)

        print(f'En {Años} años deberias recibir en intereses {Total_compuesto:.2f} €' )
        
        opcion = input("¿Qué quieres hacer ahora?\n[1] Calcular una nueva inversión\n[X] Salir\n> ").upper()
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
        opcion = input(">").upper()

        if opcion == "1":
            Calculadora_Inversiones()
        elif opcion == "X":
            print("¡Nos vemos! ")
            exit() 
        else:
            print("Opción no válida. Por favor, introduce 1 o X.")
main()