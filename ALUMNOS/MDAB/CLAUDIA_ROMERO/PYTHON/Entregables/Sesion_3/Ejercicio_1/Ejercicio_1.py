#A la aplicación de la calculadora de inversión, deberás añadirle una opción para salir de la consola.

print("Hola. Bienvenido al sistema de cálculo de inversiones.")

while True:
    print('''
¿Qué quieres hacer?
[1] Calcular una inversión
[X] Salir
''')
    
    opcion = input().upper()

    if opcion == "1":
        print("Has elegido calcular una inversión.")
        inversion = float(input("¿Cuánto quieres invertir? "))
        interes_anual = float(input("¿Cuál es el interés anual? "))
        años = int(input("¿Cuántos años vas a mantener la inversión? "))
        
        calculo = inversion * (1 + (interes_anual / 100)) ** años
        interes = calculo - inversion
        print(f"En {años} años habrás recibido {interes}€ de interés.")
        print(f"El valor total de tu inversión al cabo de {años} años será de {calculo}€.")

    elif opcion == "X": 
        print("¡Nos vemos!")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona [1] o [X].")
