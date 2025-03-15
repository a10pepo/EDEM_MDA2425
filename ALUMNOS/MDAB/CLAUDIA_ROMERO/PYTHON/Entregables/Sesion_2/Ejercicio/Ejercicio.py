# Crea una aplicación de consola que calcule los resultados de una inversión. Debe
# Pedir por consola una cantidad (numérica) de Inversión
# Pedir el % de interés anual
# Pedir el número de años que se va a mantener la inversión
# Finalmente, calcular la cantidad generada en los años especificados por el usuario


print("Hola. Bienvenido al sistema de cálculo de inversiones.")

inversion = float(input("¿Cuánto quieres invertir? "))
interes_anual = float(input("¿Cuál es el interés anual? "))
años = int(input("¿Cuántos años vas a mantener la inversión? "))

calculo = inversion * (1+ (interes_anual/100)) ** años

# Mostrar el resultado final
print(f"En {años} años habrás recibido {calculo}€ de interés.")
