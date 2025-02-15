print("Hola. Bienvenido al sistema de cálculo de inversiones")
inversion = float(input("¿Cuanto quieres invertir?\n"))
print(f"Esta es tu inversión -> {inversion}")

interes_anual = float(input("¿Cuál es el interés anual?\n"))
print(f"Este es el interés anual -> {interes_anual}")

anos_de_inversion = int(input("¿Cuantos años vas a mantener la inversión?\n"))
print(f"En {anos_de_inversion} años recibirás {(anos_de_inversion * interes_anual)/100}")

