print("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")

while True:
    print("[1] Calcular una inversión")
    print("[X] Salir")

    choice = input("Elige la opción (1 o X): ")

    if choice == "1":
        principal = float(input("¿Cuánto quieres invertir?"))
        interest_rate = float(input("¿Cuál es el interés anual?"))
        years = int(input("¿Cuántos años vas a mantener la inversión?"))

        final_amount = principal * (1 + interest_rate / 100) ** years

        print(f"En {years} años habrás recibido {final_amount:.2f}€ de interés. ¿Qué quieres hacer ahora?")

    elif choice == "X":
        print("¡Nos vemos!")
        break  # Exit the loop and end the program
