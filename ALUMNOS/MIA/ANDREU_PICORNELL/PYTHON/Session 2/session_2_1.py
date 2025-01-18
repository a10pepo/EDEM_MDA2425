print("Hola. Bienvenido al sistema de cálculo de inversiones.")

principal = float(input("¿Cuánto quieres invertir?"))
interest_rate = float(input("¿Cuál es el interés anual?"))
years = int(input("¿Cuántos años vas a mantener la inversión?"))

final_amount = principal * (1 + interest_rate / 100) ** years

print(f"En {years} años habrás recibido {final_amount:.2f}€ de interés")