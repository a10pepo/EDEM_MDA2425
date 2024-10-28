#2. Ejercicios Sesión 2
#   1.Crea una aplicación de consola que calcule los resultados de una inversión. Debe:
#   -1.Pedir por consola una cantidad (numérica) de Inversión
#   -2.Pedir el % de interés anual
#   -3.Pedir el número de años que se va a mantener la inversión
#   -4.Finalmente, calcular la cantidad generada en los años especificados por el usuario


print("Hola. Bienvenido al sistema de cálculo de inversiones.")
print("¿Cuanto dinero deseas invertir?")

money = int(input())

print("¿Cuál es el interés anual(escrive en decimal 25%=0.25)?")

interest = float(input())

print("¿Cuántos años vas a mantener la inversión?")

year = int(input())

profit= round((money*(1+interest)**year)-money, 2)

print(f"En {year} años habrás recibido {profit}€ de interés")