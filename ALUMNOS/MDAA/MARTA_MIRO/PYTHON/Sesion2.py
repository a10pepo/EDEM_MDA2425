#1
print ("Hola. Bienvenido al sistema de cálculo de inversiones")
cantidad_inversion = float (input("¿Cuánto quieres invertir? "))
#2
print("Has indicado que deseas invertir:", cantidad_inversion, "€") 
interes_anual = float (input("¿Cuál es el interés anual? "))
print("Has indicado que el interés anual es de:", interes_anual) 
interes_decimal = interes_anual / 100
print("Con un interés anual del:", interes_anual, "% ,es decir,", interes_decimal, "en decimales)")
#3
años_inversion = int (input("¿Cuántos años vas a mantener la inversión? "))
print("Has indicado que la inversión durará:", años_inversion, "años")
#4
resultado_final = cantidad_inversion * (1 + interes_decimal) ** años_inversion
interes_generado = resultado_final - cantidad_inversion
print((f"En {años_inversion} años habrás recibido {interes_generado}€ de interés.")) 

.