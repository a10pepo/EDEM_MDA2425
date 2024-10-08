print("Hola. Bienvenido al sistema de cálculo de inversiones.")
print("¿Cuánto quieres invertir?")
cantidad: int =  input()
print("¿Cuál es el interés anual?")
interes: int = input()
print("¿Cuántos años vas a mantener la inversión?")
años: int = input()
resultado: int = cantidad * (1 + interes)**años
print(f"En {años} años habrás recibido {resultado}€ de interés")