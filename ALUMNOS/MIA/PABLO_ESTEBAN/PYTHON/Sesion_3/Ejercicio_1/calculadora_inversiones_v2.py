def check_salir():
    print("> [X] Salir")
    valor = input("> ")
    if valor.lower() == "x":
        print("> ¡Nos vemos!")
        exit()
    return valor

primera = True
while True:
    print("> Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")
    print("> [1] Calcular una inversión" if primera else "> [1] Calcular una nueva inversión")
    opcion = check_salir()

    if opcion == "1":
        # Paso 1
        print()
        print("> Hola. Bienvenido al sistema de cálculo de inversiones.")
        print("> ¿Cuánto quieres invertir?")
        cantidad = float(check_salir())
        print()

        # Paso 2
        print("> ¿Cuál es el interés anual (%)?")
        interes_anual = float(check_salir())
        print()

        # Paso 3
        print("> ¿Cuántos años vas a mantener la inversión?")
        anyos = int(check_salir())
        print()

        # Paso 4 - Final
        monto_final = cantidad * (1 + interes_anual / 100) ** anyos
        beneficio = monto_final - cantidad
        print(f"> En {anyos} años habrás recibido {beneficio}€ de interés compuesto. ¿Que quieres hacer ahora?")

        primera = False
    print()