
# Paso 1
print("> Hola. Bienvenido al sistema de cálculo de inversiones.")
print("> ¿Cuánto quieres invertir?")
cantidad = float(input("> "))

# Paso 2
print("> ¿Cuál es el interés anual (%)?")
interes_anual = float(input("> "))

# Paso 3
print("> ¿Cuántos años vas a mantener la inversión?")
anyos = int(input("> "))

# Paso 4 - Final
monto_final = cantidad * (1 + interes_anual / 100) ** anyos
beneficio = monto_final - cantidad
print(f"> En {anyos} años habrás recibido {beneficio}€ de interés compuesto")