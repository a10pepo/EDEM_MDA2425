""""
Crea una aplicación de consola que calcule los resultados de una inversión. Debe
Pedir por consola una cantidad (numérica) de Inversión
Pedir el % de interés anual
Pedir el número de años que se va a mantener la inversión
Finalmente, calcular la cantidad generada en los años especificados por el usuario

"""

# Paso 1: Mensaje de bienvenida

bienvenida = "Hola. Bienvenido al sistema de cálculo de inversiones"
print (bienvenida)

# Paso 2: Pedir la cantidad de inversión

inversion_inicial = float ( input ("¿Cuánto quieres invertir? (en tu moneda local):"))

# Paso 3: Pedir el porcentaje de interés anual

interes_anual = float ( input ("¿Cuál es el interés anual? (en %)"))

# Paso 4; Pedir el número de años

años = int (input ("¿Cuántos años vas a mantener la inversión?"))



# Cálculo de la cantidad final final utilizando la fórmula de interés compuesto

cantidad_final = inversion_inicial * (1 + interes_anual/100) ** años

interes_generado = cantidad_final - inversion_inicial

# Paso 5: Mostrar el resultado 

print (f"\n En {años} años habrás recibido {interes_generado:.2f}€ de intereses.")