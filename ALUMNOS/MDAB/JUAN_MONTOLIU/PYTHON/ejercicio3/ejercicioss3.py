#1
def intereses(inversion0, interes, periodo):
    cuota = (inversion0 * (interes/100) * periodo)
    return cuota


while True:
    print("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")
    print("> [1] Calcular una inversión")
    print("> [X] Salir")
    
    opcion = input("Elige una opción (1 o X): ").strip().upper()
    
    if opcion == '1':
        inversion0 = int(input("Introduzca la cantidad que desee invertir inicialmente: "))
        
        while True:
            interes = float(input("¿Qué tipo de interés desearía?: "))
            if 0 <= interes <= 100:
                break
            else:
                print("Error: El interés debe estar comprendido entre 0 y 100. Vuelva a intentarlo.")
        
        periodo = int(input("¿Cuántos años desearía invertir en el producto?: "))
        
        cuotapers = intereses(inversion0, interes, periodo)
        print(f"En {periodo} años habrás obtenido {cuotapers:.2f}€ en intereses.")
    
    elif opcion == 'X':
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, elige 1 o X.")





#2
for number_primo in range(0, 101):
    if number_primo < 2:
        print(f"{number_primo} no es un número primo.")
    else:
        es_primo = True

        for i in range(2, int(number_primo**0.5) + 1):
            if number_primo % i == 0:
                es_primo = False 
                break 

        if es_primo:
            print(f"{number_primo} es un número primo.")
        else:
            print(f"{number_primo} no es un número primo.")

#3
for x in range (0, 2050):
    if x % 4 == 0 and (x % 100 ==0 or not x %400 == 0):
        print(f"{x} es bisiesto")
    else:
        print(f"{x} no es bisiesto")
