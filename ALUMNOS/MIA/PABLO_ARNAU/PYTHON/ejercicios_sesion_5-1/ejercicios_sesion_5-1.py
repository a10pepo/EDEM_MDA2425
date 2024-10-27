import pandas as pd

df = pd.read_csv('Inventory_v2.csv')

#Voy a sumar todo el stock del inventario

stock= df['quantity'].sum()

print(f'El stock total del inventario es :{stock} unidades')

# Voy a imprimir las 5 primeras filas

print(df.head())

# Voy a sacar el valor medio del stock

valor_total=df['value'].sum()

valor_medio_unidades = float (valor_total/stock)

print (f'El valor medio del stock es: {valor_medio_unidades}')


