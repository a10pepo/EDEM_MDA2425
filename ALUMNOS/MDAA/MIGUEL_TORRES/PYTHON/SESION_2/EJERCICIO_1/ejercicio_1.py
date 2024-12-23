# Ejercicio Sesión 2
#   1. Crea una aplicación de consola que calcule los resultados de una inversión. Debe:
#   2. Pedir por consola una cantidad (numérica) de Inversión
#   3. Pedir el % de interés anual
#   4. Pedir el número de años que se va a mantener la inversión
#   5. Finalmente, calcular la cantidad generada en los años especificados por el usuario


print("Hola. Bienvenido al sistema de cálculo de inversiones")

# Pedir el capital inicial con un bucle que captura el error de valor
while True:
    try:
        capital_inicial = int(input("¿Cuánto quieres invertir? (Introduce un número entero sin símbolos ni puntos, como por ejemplo 1000): "))
        break
    except ValueError:
        print("Por favor, introduce un número entero válido sin símbolos ni puntos, como por ejemplo 1000.")

# Pedir el interés anual con un bucle que captura el error de valor
while True:
    try:
        interes_anual = float(input("¿Cuál es el interés anual? (Introduce un número decimal, por ejemplo: 0.05 para 5%): "))
        break
    except ValueError:
        print("Por favor, introduce un número decimal válido usando el punto como separador, por ejemplo: 0.05 para 5%.")

# Pedir el número de años con un bucle que captura el error de valor
while True:
    try:
        años = int(input("¿Cuántos años vas a mantener la inversión? (Introduce un número entero como 5): "))
        break
    except ValueError:
        print("Por favor, introduce un número entero válido.")

# Cálculo de la inversión
capital_final = capital_inicial * (1 + interes_anual) ** años
interes_generado = capital_final - capital_inicial

# Resultado final
print(f"En {años} años habrás generado {interes_generado:.2f}€ de interés.")
