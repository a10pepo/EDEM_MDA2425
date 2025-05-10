import pandas as pd
import numpy as np

data = pd.read_csv('pokemon_data.csv')

# IMPRIMIR TODOS LOS DATOS
#print(data)

# IMPRIMIR LOS 5 PRIMEROS
#print(data.head(5))

# IMPRIMIR LOS ÚLTIMOS 5
#print(data.tail(5))

# OBTENER EL NOMBRE DE LAS COLUMNAS
#print(data.columns)

# OBTENER TODOS LOS NOMBRES Y VELOCIDADES
#print(data[['Name','Speed']])

# OBTENER LOS 5 PRIMEROS NOMBRES USANDO [:]
#print(data['Name'][:5])

# OBTENER TODAS LAS FILAS
#print(data)

#OBTENER UN RANGO DE FILAS
# print(data[3:9])

# OBTENER EL NOMBRE DE LA FILA 10
#print(data['Name'][10])

# ITERAR POR TODOS Y MOSTRAR EL INDICE Y NOMBRE DE CADA FILA
#print(data.index, data['Name'])

# OBTENER LOS POKEMOS DE TIPO 1
#print(data[data['Type 1'] == 'Water'])

# OBTENER ESTADÍSTICAS
#print(data.describe())

# ORDENAR POR NOMBRE ASCENDENTE
#print(data.sort_values('Name', ascending= True))

# CREAR COLUMNA EXTRA CALCULADA
#data['TOTAL'] = data['HP'] + data['Attack'] + data['Defense'] + data['Speed']
# print(data)

# ELIMINAR COLUMNA TOTAL
# data.drop(columns='TOTAL')
# print(data)

# FILTRAR POKEMONS DE TIPO GRASS Y POISON
#print(data[(data['Type 1'] == 'Grass') & (data['Type 2'] == 'Poison')])

# FILTRAR POKEMONS DE TIPO FIRE O POISON
#print(data[(data['Type 1'] == 'Grass') | (data['Type 2'] == 'Poison')])

#FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
#print(data[(data['Type 1'] == 'Grass') & (data['Type 2'] == 'Poison') & (data['HP'] >= 70)])

# FILTRAR POKEMONS CON NOMBRE "MEGA"
#print(data[data['Name'].str.contains('Mega')])

# FILTRAR POKEMONS SIN NOMBRE "MEGA"
#print(data[~data['Name'].str.contains('Mega')])

# FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
#print(data[data['Name'].str.startswith('Pi')])

# RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
# data.loc[data['Type 1']== 'Fire', 'Type 1'] = 'Flame'
# print(data)

# RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
# data.loc[data['Type 1']== 'Flame', 'Type 1'] = 'Fire'
# print(data)

# CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
# data.loc[data['Legendary']== True, 'Type 1'] = 'Fire'
# print(data)

# ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
# ordenado_tipo= data.groupby('Type 1')['Defense'].mean().sort_values(ascending= False)
# print(ordenado_tipo)

# ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
# ordenado_tipo= data.groupby('Type 1')['Ataque'].mean().sort_values(ascending= False)
# print(ordenado_tipo)

# ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
# ordenado_tipo= data.groupby('Type 1')['HP'].mean().sort_values(ascending= False)
# print(ordenado_tipo)

#  ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
# ordenado_tipo= data.groupby('Type 1')['Type 1'].sum()
# print(ordenado_tipo)

# ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 DE POKEMON
# ordenado_tipo= data.groupby('Type 1')['Type 1'].sum()
# print(ordenado_tipo)

# ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
# ordenado_tipo= data.groupby(['Type 1', 'Type 2']).size()
# print(ordenado_tipo)

# LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5) // ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA
# data = pd.read_csv('pokemon_data.csv',chunksize=5)
# for chunk in data:
#     print(chunk)






