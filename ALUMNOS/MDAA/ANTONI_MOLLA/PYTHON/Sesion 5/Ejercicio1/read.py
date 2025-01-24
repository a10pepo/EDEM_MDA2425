import pandas as pd

df=pd.read_csv('prueba.csv')

#Filtramos
df_filtrado=df[df['Edad']>30]

print(df.head())  # Primeras 5 filas
print(df.tail())  # Últimas 5 filas

# Nombres de las columnas
print(df.columns)


df_filtrado2 = df[(df['Edad'] > 30) & (df['Correo'] == 'luis@example.com')]
print(df_filtrado2)