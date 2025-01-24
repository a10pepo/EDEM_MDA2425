def calcular_inversion():
    print("Hola. Bienvenido al sistema de cálculo de inversiones.")

    cantidad = float(input("¿Cuánto quieres invertir? "))

    interes_anual = float(input("¿Cuál es el interés anual? "))
    
    años = int(input("¿Cuántos años vas a mantener la inversión? "))

    cantidad_generada = cantidad * (1 + (interes_anual / 100)) ** años
    intereses = cantidad_generada - cantidad

    print(f"\nEn {años} años habrás recibido {intereses:.2f}€ de interés")
    print(f"El total de la inversión será de {cantidad_generada:.2f}€")

calcular_inversion()
