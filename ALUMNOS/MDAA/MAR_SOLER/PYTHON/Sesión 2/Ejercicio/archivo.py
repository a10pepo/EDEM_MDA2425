"""
Crea una aplicación de consola que calcule los resultados de una inversión. Debe
Pedir por consola una cantidad (numérica) de Inversión
Pedir el % de interés anual
Pedir el número de años que se va a mantener la inversión
Finalmente, calcular la cantidad generada en los años especificados por el usuario
"""

print("Hola. Bienvenido al sistema de cálculo de inversiones.")

def preguntas(pregunta):
    while True:
        try:
            respuesta = float(input(pregunta))
            return respuesta
        except ValueError:
            print("Debes introducir un número")

cantidad_inicial = preguntas("¿Cuánto quieres invertir?: ")
interes = preguntas("¿Cuál es el interés anual? En puntos porcentuales: ")
tiempo = preguntas("¿Cuántos años vas a mantener la inversión?: ")

cantidad_final = round((cantidad_inicial * (1 + interes / 100) ** tiempo),2)
print(f"En {tiempo} años habrás recibido {cantidad_final}€ de interés")