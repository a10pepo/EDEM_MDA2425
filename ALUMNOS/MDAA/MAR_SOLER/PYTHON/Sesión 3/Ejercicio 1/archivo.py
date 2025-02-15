"""
A la aplicación de la calculadora de inversión, deberás añadirle una opción para salir de la consola.
"""

print("Hola. Bienvenido al sistema de cálculo de inversiones.")

def preguntas(pregunta):
    while True:
        try:
            respuesta = input(pregunta)
            if respuesta.lower() == 'x':
                print("¡Nos vemos!")
                exit()
            return float(respuesta)
        except ValueError:
            print("Debes introducir un número válido o 'X' para salir.")

while True:
    print("¿Qué quieres hacer?")
    print("[1] Calcular una inversión")
    print("[X] Salir")
    opcion = input("Selecciona una opción: ")

    if opcion.lower() == 'x':
        print("¡Nos vemos!")
        break
    
    elif opcion == '1':
        cantidad_inicial = preguntas("¿Cuánto quieres invertir?: ")
        interes = preguntas("¿Cuál es el interés anual? En puntos porcentuales: ")
        tiempo = preguntas("¿Cuántos años vas a mantener la inversión?: ")

        cantidad_final = round((cantidad_inicial * (1 + interes / 100) ** tiempo), 2)
        print(f"En {tiempo} años habrás recibido {cantidad_final}€ de interés")

    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")