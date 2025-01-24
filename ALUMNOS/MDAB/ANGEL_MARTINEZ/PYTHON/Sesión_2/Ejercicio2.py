print("Hola. Bienvenido al sistema de cálculo de inversiones.") 
cantidad = int(input("¿Cuánto quieres invertir? "))
tipo_interes = float(input("¿A que tipo de interes anual se encontrara esa cantidad Sujeta?"))
años = int(input("¿Cuántos años vas a mantener la inversión?"))

interes_a_recibir = (cantidad * (tipo_interes * 0.01) * años) 


print (f"En {años} años habrás recibido {interes_a_recibir}€ de interés")

