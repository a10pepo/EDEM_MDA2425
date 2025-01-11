inversion = float(input(
'''Hola. Bienvenido al sistema de cálculo de inversiones. 
¿Cuánto quieres invertir?
'''               
))
interes = float(input('¿Cuál es el interés anual (en %)? ')) / 100
years = int(input('¿Cuántos años vas a mantener la inversión? '))

def calculo_inversion(inversion, interes, years):
    return inversion * (1+interes) ** years

ganancias = calculo_inversion(inversion, interes, years)

print(f'En {years} habrás recibido {ganancias}€')
