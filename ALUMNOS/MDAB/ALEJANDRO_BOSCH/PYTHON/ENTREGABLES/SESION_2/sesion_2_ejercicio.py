#Crea una aplicación de consola que calcule los resultados de una inversión.


print("Hola. Bienvenido al sistema de cálculo de inversiones.")

def calcular_inversion():
    
    cantidad_inv = float(input("¿Cuánto quieres invertir?: "))

    int_anual = float(input("¿Cuál es el interés anual (en porcentaje)?: "))

    int_anual = int_anual / 100

    cantidad_años = int(input("¿Cuántos años vas a mantener la inversión?: "))

    cantidad_generada = (cantidad_inv * (1 + int_anual) ** cantidad_años)

    cantidad_generada = round(cantidad_generada, 2)
    
    print(f"En {cantidad_años} años, habrás recibido {cantidad_generada}€.")

calcular_inversion()