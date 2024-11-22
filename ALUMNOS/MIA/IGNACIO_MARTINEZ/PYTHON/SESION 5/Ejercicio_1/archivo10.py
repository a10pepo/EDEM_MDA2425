import pandas as pd

# Leer el archivo CSV

data = pd.read_csv('pokemon_data.csv')

#IMPRIMIR TODOS LOS VALORES

print(data.values)

#IMPRIMIR LOS PRIMEROS 5

print(data.head(5))

#IMPRIMIR LOS ÚLTIMOS 5

print(data.tail(5))

#OBTENER NOMBRES DE LAS COLUMNAS

print(data.columns)

#OBTENER TODOS LOS NOMBRES

print(data['Name'])

#OBTENER TODOS LOS NOMBRES Y VELOCIDADES

print("\nTodos los nombres y velocidades de los Pokémon:")
print(data[['Name', 'Speed']])

#LOS PRIMEROS 5 NOMBRES USANDO [::]

print(data['Name'][0:5])

#OBTENER TODAS LAS FILAS

print(data)

#OBTENER UN RANGO DE FILAS

print(data[2:6])

#OBTENER EL NOMBRE DE LA FILA 10

print(data.iloc[9]['Name'])

#ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA

for index, row in data.iterrows():
    print(index, row['Name'])

#POKEMONS DE TIPO 1 == WATER

water_pokemon = data[data['Type 1'] == 'Water']
print(water_pokemon)

#ESTADÍSTICAS (usando Describe del DafaFrame)

print(data.describe())

#ORDENACIÓN POR NOMBRE ASCENDENTE

print(data.sort_values('Name', ascending=True))

#CREAR UNA COLUMNA EXTRA CALCULADA
#La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
#La columna debe llamarse TOTAL

data['Total'] = data['HP'] + data['Attack'] + data['Defense'] + data['Speed']
print(data[['Name', 'Total']])

#ELIMINAR LA COLUMNA TOTAL

data = data.drop(columns=['Total'])

#FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"

grass_poison_pokemon = data[(data['Type 1'] == 'Grass') | (data['Type 2'] == 'Poison')]
print(grass_poison_pokemon)

#FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON

fire_poison_pokemon = data[(data['Type 1'] == 'Fire') | (data['Type 2'] == 'Poison')]
print(fire_poison_pokemon)

#FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70

grass_poison_hp_pokemon = data[(data['Type 1'] == 'Grass') | (data['Type 2'] == 'Poison') & (data['HP'] >= 70)]
print(grass_poison_hp_pokemon)

#FILTRAR POKEMONS CON NOMBRE "MEGA"

mega_pokemon = data[data['Name'].str.contains('Mega')]
print(mega_pokemon)

#FILTRAR POKEMONS SIN NOMBRE "MEGA"

no_mega_pokemon = data[~data['Name'].str.contains('Mega')]
print(no_mega_pokemon)

#FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"

pi_pokemon = data[data['Name'].str.startswith('Pi')]
print(pi_pokemon)

#RENOMBRADO DE COLUMNA "FIRE" a "FLAME"

data['Type 1'] = data['Type 1'].replace('Fire', 'Flame')
data['Type 2'] = data['Type 2'].replace('Fire', 'Flame')

print(data[['Name', 'Type 1', 'Type 2']])

#RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA

data['Type 1'] = data['Type 1'].replace('Flame', 'Fire')
data['Type 2'] = data['Type 2'].replace('Flame', 'Fire')

print(data[['Name', 'Type 1', 'Type 2']])

#CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"

legendary_pokemon = data[data['Legendary'] == True]
legendary_pokemon['Type 1'] = 'Fire'
legendary_pokemon['Type 2'] = 'Fire'
print(legendary_pokemon[['Name', 'Type 1', 'Type 2']])

#(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA

print(data.groupby('Type 1').mean(numeric_only=True).sort_values('Defense'))

#(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE

print(data.groupby('Type 1').mean(numeric_only=True).sort_values('Attack'))

#(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP

print(data.groupby('Type 1').mean(numeric_only=True).sort_values('HP'))

#(Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON

print(data.groupby('Type 1').sum(numeric_only=True))

#(Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 DE POKEMON

print(data.groupby('Type 1').count())

#(Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON

print(data.groupby(['Type 1', 'Type 2']).count())

#LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5)

chunksize = 5
chunks = pd.read_csv('pokemon_data.csv', chunksize=chunksize)

for chunk in chunks:
    print(chunk)




















