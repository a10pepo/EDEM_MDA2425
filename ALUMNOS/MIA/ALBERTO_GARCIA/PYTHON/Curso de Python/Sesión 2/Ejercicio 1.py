print('Bienvenido al centro de control del cálculo de inversiones\n')
euros=int(input('Dame la cantidad de inversión inicial:\n'))
percentaje=int(input('Dame el % de interes anual \n'))
anyos=int(input('¿Durante cuantos años vas a mantener la inversión?\n'))
a=0
while(a<=anyos):
    euros=euros*(1+(percentaje/100))
    a=a+1
print(f'En {anyos}, habrás recibido {euros} de interes')