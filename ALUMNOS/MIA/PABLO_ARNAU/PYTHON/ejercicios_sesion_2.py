print (' Hola. Bienvenido al sistema de cálculo de inversiones.')

inversion = int (input ('¿Cuánto quieres invertir?\n'))
interes = int (input ('¿Cuál es le interés anual?\n'))
tiempo = int (input ('¿Cuántos años vas a mantener la inversión?\n'))

dinero_generado = (inversion * ((1 + interes/100)**tiempo))- inversion

print (f'En {tiempo} años habrás recibido {dinero_generado:.3f}€ de interés')