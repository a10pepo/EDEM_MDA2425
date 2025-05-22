import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# IMPRIMIR TODOS LOS VALORES
print(df)

# IMPRIMIR LOS PRIMEROS 5
print(df.head())

# IMPRIMIR LOS ÚLTIMOS 5
print(df.tail())

# OBTENER NOMBRES DE LAS COLUMNAS
print(df.columns)

# OBTENER TODOS LOS NOMBRES
print(df['Name'])

# OBTENER TODOS LOS NOMBRES Y VELOCIDADES
print(df[['Name', 'Speed']])

# LOS PRIMEROS 5 NOMBRES USANDO [::]
print(df['Name'][:5])

# OBTENER TODAS LAS FILAS
print(df)

# OBTENER UN RANGO DE FILAS
print(df[10:21])

# OBTENER EL NOMBRE DE LA FILA 10
print(df.iloc[9]['Name'])

# ITERAR POR TODOS Y MOSTRAR ÍNDICE Y NOMBRE
for index, row in df.iterrows():
    print(index, row['Name'])

# POKEMONS DE TIPO 1 == WATER
print(df[df['Type 1'] == 'Water'])

# ESTADÍSTICAS (DESCRIBE)
print(df.describe())

# ORDENACIÓN POR NOMBRE ASCENDENTE
print(df.sort_values('Name'))

# CREAR UNA COLUMNA EXTRA CALCULADA (TOTAL)
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Speed']
print(df)

# ELIMINAR LA COLUMNA TOTAL
df = df.drop(columns=['Total'])
print(df)

# FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
print(df[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])

# FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON"
print(df[(df['Type 1'] == 'Fire') | (df['Type 2'] == 'Poison')])

# FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
print(df[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] >= 70)])

# FILTRAR POKEMONS CON NOMBRE "MEGA"
print(df[df['Name'].str.contains('Mega')])

# FILTRAR POKEMONS SIN NOMBRE "MEGA"
print(df[~df['Name'].str.contains('Mega')])

# FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
print(df[df['Name'].str.startswith('Pi')])

# RENOMBRAR COLUMNA "TYPE 1" A "FLAME"
df.rename(columns={'Type 1': 'Flame'}, inplace=True)
print(df)

# RENOMBRAR DE NUEVO A "TYPE 1"
df.rename(columns={'Flame': 'Type 1'}, inplace=True)
print(df)

# CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
df.loc[df['Legendary'] == True, 'Type 1'] = 'Fire'
print(df[df['Legendary'] == True])

# ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON ORDENADOS POR DEFENSA
print(df.groupby('Type 1').mean().sort_values('Defense'))

# ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON ORDENADOS POR ATAQUE
print(df.groupby('Type 1').mean().sort_values('Attack'))

# ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON ORDENADOS POR HP
print(df.groupby('Type 1').mean().sort_values('HP'))

# ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
print(df.groupby('Type 1').sum())

# ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON
print(df['Type 1'].value_counts())

# ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 Y 2 DE POKEMON
print(df.groupby(['Type 1', 'Type 2']).size())

# LEE EL ARCHIVO CSV SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5)
file_path = 'pokemon_data.csv'  
chunk_size = 5
chunk_iter = pd.read_csv(file_path, chunksize=chunk_size)

# ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA
for chunk in chunk_iter:
    print("CHUNK:")
    print(chunk)
    print("-" * 50)