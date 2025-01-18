# 2. Ejercicios Sesión 2
# Crea una aplicación de consola que calcule los resultados de una inversión. Debe
# Pedir por consola una cantidad (numérica) de Inversión
# Pedir el % de interés anual
# Pedir el número de años que se va a mantener la inversión
# Finalmente, calcular la cantidad generada en los años especificados por el usuario

inversion = float(input("Hola. Bienvenido al sistema de cálculo de inversiones. \n¿Cuánto quieres invertir? (€) ->"))
interes = float(input("¿Cuál es el interés anual? (%) ->"))
anyos = int(input("¿Cuántos años vas a mantener la inversión? ->"))
ganancia = float(((inversion*(interes / 100))*anyos))

print (f"En {anyos} años habrás recibido {ganancia}€ de interés")