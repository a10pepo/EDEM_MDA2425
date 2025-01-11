"""
Crea una aplicación de consola que calcule los resultados de una inversión. 
Debe:
1. Pedir por consola una cantidad (numérica) de Inversión
2. Pedir el % de interés anual
3. Pedir el número de años que se va a mantener la inversión
4. Finalmente, calcular la cantidad generada en los años especificados por el usuario
"""

print("Hola. Bienvenido al sistema de cálculo de inversiones de interés compuesto.")

def obtener_input(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un valor válido.")

inversion_inicial = obtener_input("¿Cuánto quieres invertir? ")
interes_anual = obtener_input("¿Cuál es el interés anual? (en puntos porcentuales) ") / 100
duracion = obtener_input("¿Cuántos años vas a mantener la inversión? ")

inversion_final = inversion_inicial * ((1 + interes_anual) ** duracion)
interes_acumulado = round((inversion_final - inversion_inicial),2)

print(f"En {duracion} años habrás recibido {interes_acumulado}€ de interés.")