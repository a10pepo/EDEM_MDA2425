import pandas as pd

# Leer el archivo CSV
pokemon_data = pd.read_csv('PYTHON/Sesion5/Ejercicio1/Data/pokemon_data.csv')
columnas_numericas = pokemon_data.select_dtypes(include=['number'])
data_pokemon = pokemon_data[['Type 1']].join(columnas_numericas)

# IMPRIMIR TODOS LOS VALORES
print("Todos los valores:")
print(pokemon_data)

# IMPRIMIR LOS PRIMEROS 5
print("\nPrimeros 5:")
print(pokemon_data.head(5))

# IMPRIMIR LOS ÚLTIMOS 5
print("\nÚltimos 5:")
print(pokemon_data.tail(5))

# OBTENER NOMBRES DE LAS COLUMNAS
print("\nNombres de las columnas:")
print(pokemon_data.columns)

# OBTENER TODOS LOS NOMBRES
print("\nTodos los nombres de los Pokémon:")
print(pokemon_data['Name'])

# OBTENER TODOS LOS NOMBRES Y VELOCIDADES
print("\nTodos los nombres y velocidades de los Pokémon:")
print(pokemon_data[['Name', 'Speed']])

# LOS PRIMEROS 5 NOMBRES USANDO [::]
print("\nPrimeros 5 nombres:")
print(pokemon_data['Name'][:5])

# OBTENER TODAS LAS FILAS
print("\nTodas las filas:")
print(pokemon_data)

# OBTENER UN RANGO DE FILAS (ejemplo de fila 10 a 15)
print("\nRango de filas de la 10 a la 15:")
print(pokemon_data[10:16])

# OBTENER EL NOMBRE DE LA FILA 10
print("\nNombre del Pokémon en la fila 10:")
print(pokemon_data.iloc[9]['Name'])

# ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
print("\nIterar y mostrar índice y nombre:")
for indice, fila in pokemon_data.iterrows():
    print(f"Índice: {indice}, Nombre: {fila['Name']}")

# POKEMONS DE TIPO 1 == WATER
print("\nPokémon de tipo 1 == Water:")
print(pokemon_data[pokemon_data['Type 1'] == 'Water'])

# ESTADÍSTICAS (usando Describe del DataFrame)
print("\nEstadísticas descriptivas:")
print(pokemon_data.describe())

# ORDENACIÓN POR NOMBRE ASCENDENTE
print("\nOrdenar por nombre (ascendente):")
print(pokemon_data.sort_values('Name'))

# CREAR UNA COLUMNA EXTRA CALCULADA (suma de HP + Ataque + Defensa + Velocidad)
pokemon_data['Total'] = pokemon_data['HP'] + pokemon_data['Attack'] + pokemon_data['Defense'] + pokemon_data['Speed']
print("\nDataFrame con columna Total:")
print(pokemon_data[['Name', 'Total']])

# ELIMINAR LA COLUMNA TOTAL
pokemon_data = pokemon_data.drop(columns=['Total'])
print("\nColumna 'Total' eliminada:")

# FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
print("\nPokémon de tipo Grass y Poison:")
print(pokemon_data[(pokemon_data['Type 1'] == 'Grass') & (pokemon_data['Type 2'] == 'Poison')])

# FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON"
print("\nPokémon de tipo Fire o Poison:")
print(pokemon_data[(pokemon_data['Type 1'] == 'Fire') | (pokemon_data['Type 1'] == 'Poison')])

# FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
print("\nPokémon de tipo Grass y Poison con HP >= 70:")
print(pokemon_data[(pokemon_data['Type 1'] == 'Grass') & (pokemon_data['Type 2'] == 'Poison') & (pokemon_data['HP'] >= 70)])

# FILTRAR POKEMONS CON NOMBRE "MEGA"
print("\nPokémon con 'Mega' en el nombre:")
print(pokemon_data[pokemon_data['Name'].str.contains('Mega')])

# FILTRAR POKEMONS SIN NOMBRE "MEGA"
print("\nPokémon sin 'Mega' en el nombre:")
print(pokemon_data[~pokemon_data['Name'].str.contains('Mega')])

# FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
print("\nPokémon cuyos nombres comienzan con 'Pi':")
print(pokemon_data[pokemon_data['Name'].str.startswith('Pi')])

# Cambiar todos los valores 'Fire' a 'Flame' en la columna 'Type 1'
pokemon_data['Type 1'].replace('Fire', 'Flame', inplace=True)
print("\nValores 'Fire' en la columna 'Type 1' cambiados a 'Flame':")
print(pokemon_data.head())

# Cambiar los valores 'Flame' de vuelta a 'Fire' en la columna 'Type 1'
pokemon_data['Type 1'].replace('Flame', 'Fire', inplace=True)
print("\nValores 'Flame' en la columna 'Type 1' cambiados de vuelta a 'Fire':")
print(pokemon_data.head())

# CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
pokemon_data.loc[pokemon_data['Legendary'] == True, 'Type 1'] = 'Fire'
print("\nPokémon legendarios cambiados a tipo 'Fire':")
print(pokemon_data[pokemon_data['Legendary'] == True])

# AGRUPACIÓN - groupBy ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON Y ORDENADOS POR DEFENSA
print("\nEstadísticas de media por tipo de Pokémon ordenadas por Defensa:")
print(data_pokemon.groupby('Type 1').mean().sort_values('Defense'))

# AGRUPACIÓN - groupBy ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON Y ORDENADOS POR ATAQUE
print("\nEstadísticas de media por tipo de Pokémon ordenadas por Ataque:")
print(data_pokemon.groupby('Type 1').mean().sort_values('Attack'))

# AGRUPACIÓN - groupBy ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON Y ORDENADOS POR HP
print("\nEstadísticas de media por tipo de Pokémon ordenadas por HP:")
print(data_pokemon.groupby('Type 1').mean().sort_values('HP'))

# AGRUPACIÓN - groupBy ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
print("\nEstadísticas de suma por tipo de Pokémon:")
print(data_pokemon.groupby('Type 1').sum())

# AGRUPACIÓN - groupBy ESTADÍSTICAS DEL NÚMERO DE POKEMONS POR TIPO 1
print("\nNúmero de Pokémon por tipo 1:")
print(pokemon_data.groupby('Type 1').count()['Name'])

# AGRUPACIÓN - groupBy ESTADÍSTICAS DEL NÚMERO DE POKEMONS POR TIPO 1 y 2
print("\nNúmero de Pokémon por tipo 1 y tipo 2:")
print(pokemon_data.groupby(['Type 1', 'Type 2']).count()['Name'])

pokemon_chunk = pd.read_csv('PYTHON/Sesion5/Ejercicio1/Data/pokemon_data.csv', chunksize=5)
for chunk in pokemon_chunk:
    print(chunk)
