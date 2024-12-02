# EJERCICIO 1 
def calculadora_inversion():
    while True:
    
        print("\nHola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")
        print("[1] Calcular una inversión")
        print("[X] Salir")
        
        
        opcion = input("Ingresa tu elección: ").strip().lower()
        
        
        if opcion == '1':
            calcular_inversion()
        elif opcion == 'x':
            print("\n¡Nos vemos!")
            exit()
        else:
            print("\nOpción no válida. Por favor, introduce 1 o X.")


def calcular_inversion():
    while True:
        try:
            
            monto = float(input("\nIntroduce el monto de la inversión en euros: "))
            tasa_interes = float(input("Introduce la tasa de interés anual (en %): "))
            anios = int(input("Introduce el número de años: "))
            
            
            resultado_final = monto * (1 + tasa_interes / 100) ** anios
            interes_generado = resultado_final - monto
            
            
            print(f"\nEn {anios} años habrás recibido {interes_generado:.2f}€ de interés.")
        except ValueError:
            
            print("\nPor favor, introduce valores válidos.")
            continue
        
        
        print("\n¿Qué quieres hacer ahora?")
        print("[1] Calcular una nueva inversión")
        print("[X] Salir")
        
        
        opcion = input("Ingresa tu elección: ").strip().lower()
        
        
        if opcion == '1':
            continue
        elif opcion == 'x':
            print("\n¡Nos vemos!")
            exit()
        else:
            print("\nOpción no válida. Regresando al menú principal.")
            break


calculadora_inversion()

# EJERCICIO 2 

def mostrar_numeros_primos():
    print("Números primos del 1 al 100:")
    
    
    for num in range(2, 101):
        es_primo = True
        
        
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                es_primo = False
                break
        
        
        if es_primo:
            print(num, end=" ")  
    print()  

mostrar_numeros_primos()

# EJERCICIO 3 

def identificar_anios_bisiestos(anios):
    for anio in anios:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            print(f"El año {anio} es bisiesto.")
        else:
            print(f"El año {anio} no es bisiesto.")

entrada = input("Introduce una lista de años separados por comas (ejemplo: 2000,2001,2024): ")

try:
    lista_anios = [int(anio.strip()) for anio in entrada.split(",")]

    identificar_anios_bisiestos(lista_anios)
except ValueError:
    print("Por favor, introduce una lista de años válida.")


