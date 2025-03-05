def continuar():
    prueba = input("Pulsa '1' para seguir o 'X' para salir: ")
    if prueba == "1":
        return True
    elif prueba.lower() == "x":
        print("Gracias por usar la aplicación.")
        exit()
    else:
        print("Opción no válida.")
        return continuar()

d = input("Hola! Pulsa '1' para entrar o 'X' para salir: ")
if d.lower() == "x":
    print("Gracias por usar la aplicación.")
    exit()
if d == "1":
    print("¡Hola! ¿Cuánto quieres invertir? o pulsa 'X' para salir de la calculadora")
    if continuar():
        a = float(input("Invertirás: "))
        print(f"Invertirás {a} €")
        print("¿Cuál es el interés anual? o pulsa 'X' para salir de la calculadora")
        if continuar():
            b = float(input("El interés anual es: "))
            print(f"El interés anual es {b}")
            print("¿Cuántos años quieres mantener la inversión? o pulsa 'X' para salir de la calculadora")
            if continuar():
                c = int(input("¿Cuántos años?: "))
                print(f"Mantendrás la inversión de {a}€ con un interés anual de {b} durante {c} años")
                dinero_final = a * b**c
                print(f"Tras esos {c} años, tendrás una cantidad de {dinero_final} €")
else:
    print("Opción no válida.")