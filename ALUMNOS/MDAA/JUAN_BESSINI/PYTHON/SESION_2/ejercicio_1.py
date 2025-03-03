#by Juan Bessini
# Solicitar el monto inicial con validación de entrada
while True:
    try:
        capital_inicial = float(input("Introduce el monto inicial de inversión (por ejemplo, 1000): "))
        if capital_inicial < 0:
            print("El monto no puede ser negativo. Inténtalo de nuevo.")
            continue
        break
    except ValueError:
        print("Entrada no válida. Introduce un número válido.")

# Solicitar el interés anual con validación
while True:
    try:
        tasa_interes = float(input("Introduce el porcentaje de interés anual (por ejemplo, 5 para 5%): ")) / 100
        if tasa_interes < 0:
            print("El interés no puede ser negativo. Inténtalo de nuevo.")
            continue
        break
    except ValueError:
        print("Entrada no válida. Introduce un número válido.")

# Solicitar el número de años con validación
while True:
    try:
        duracion = int(input("¿Durante cuántos años planeas invertir? (por ejemplo, 10): "))
        if duracion < 0:
            print("El número de años no puede ser negativo. Inténtalo de nuevo.")
            continue
        break
    except ValueError:
        print("Entrada no válida. Introduce un número entero válido.")

# Calcular el monto final usando interés compuesto
monto_final = capital_inicial * (1 + tasa_interes) ** duracion
beneficio = monto_final - capital_inicial

# Mostrar los resultados
print(f"Después de {duracion} años, tu inversión inicial de {capital_inicial:.2f}€ habrá crecido hasta {monto_final:.2f}€, generando un beneficio de {beneficio:.2f}€.")
