import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('pokemon_data.csv')

# IMPRIMIR TODOS LOS VALORES
print("TODOS LOS VALORES:")
print(df)

# IMPRIMIR LOS PRIMEROS 5
print("\nPRIMEROS 5:")
print(df.head())

# IMPRIMIR LOS ÚLTIMOS 5
print("\nÚLTIMOS 5:")
print(df.tail())

# OBTENER NOMBRES DE LAS COLUMNAS
print("\nNOMBRES DE LAS COLUMNAS:")
print(df.columns)

# OBTENER TODOS LOS NOMBRES
print("\nTODOS LOS NOMBRES:")
print(df['Name'])

# OBTENER TODOS LOS NOMBRES Y VELOCIDADES
print("\nTODOS LOS NOMBRES Y VELOCIDADES:")
print(df[['Name', 'Speed']])

# LOS PRIMEROS 5 NOMBRES USANDO [::]
print("\nPRIMEROS 5 NOMBRES USANDO [::]:")
print(df['Name'][:5])

# OBTENER TODAS LAS FILAS
print("\nTODAS LAS FILAS:")
print(df.iloc[:])

# OBTENER UN RANGO DE FILAS
print("\nRANGO DE FILAS (5-10):")
print(df.iloc[5:10])

# OBTENER EL NOMBRE DE LA FILA 10
print("\nNOMBRE DE LA FILA 10:")
print(df.iloc[9]['Name'])

# ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
print("\nÍNDICE Y NOMBRE DE CADA FILA:")
for index, row in df.iterrows():
    print(index, row['Name'])

# POKEMONS DE TIPO 1 == WATER
print("\nPOKEMONS DE TIPO 1 == WATER:")
print(df[df['Type 1'] == 'Water'])

# ESTADÍSTICAS (usando Describe del DataFrame)
print("\nESTADÍSTICAS:")
print(df.describe())

# ORDENACIÓN POR NOMBRE ASCENDENTE
print("\nORDENACIÓN POR NOMBRE ASCENDENTE:")
print(df.sort_values('Name'))

# CREAR UNA COLUMNA EXTRA CALCULADA
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Speed']
print("\nCON COLUMNA TOTAL:")
print(df)

# ELIMINAR LA COLUMNA TOTAL
df = df.drop(columns=['Total'])
print("\nSIN COLUMNA TOTAL:")
print(df)

# FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
print("\nPOKEMONS DE TIPOS 'GRASS' Y 'POISON':")
print(df[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])

# FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON"
print("\nPOKEMONS DE TIPO 'FIRE' Ó 'POISON':")
print(df[(df['Type 1'] == 'Fire') | (df['Type 2'] == 'Poison')])

# FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
print("\nPOKEMONS DE TIPO 'GRASS' Y 'POISON' Y UN HP >= 70:")
print(df[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] >= 70)])

# FILTRAR POKEMONS CON NOMBRE "MEGA"
print("\nPOKEMONS CON NOMBRE 'MEGA':")
print(df[df['Name'].str.contains('Mega')])

# FILTRAR POKEMONS SIN NOMBRE "MEGA"
print("\nPOKEMONS SIN NOMBRE 'MEGA':")
print(df[~df['Name'].str.contains('Mega')])

# FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
print("\nPOKEMONS CUYOS NOMBRES COMIENCEN CON 'PI':")
print(df[df['Name'].str.startswith('Pi')])

# RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
df.rename(columns={'Type 1': 'Flame'}, inplace=True)
print("\nRENOMBRADO DE 'Type 1' A 'Flame':")
print(df)

# RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
df.rename(columns={'Flame': 'Type 1'}, inplace=True)
print("\nRENOMBRADO DE 'Flame' A 'Type 1':")
print(df)

# CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
df.loc[df['Legendary'] == True, 'Type 1'] = 'Fire'
print("\nCAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO 'FIRE':")
print(df)

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
print("\nESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON ORDENADOS POR DEFENSA:")
print(df.groupby('Type 1').mean(numeric_only=True).sort_values('Defense'))

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
print("\nESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON ORDENADOS POR ATAQUE:")
print(df.groupby('Type 1').mean(numeric_only=True).sort_values('Attack'))

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
print("\nESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON ORDENADOS POR HP:")
print(df.groupby('Type 1').mean(numeric_only=True).sort_values('HP'))

# (Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
print("\nESTADÍSTICAS DE SUMA POR TIPO DE POKEMON:")
print(df.groupby('Type 1').sum(numeric_only=True))

# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 DE POKEMON
print("\nESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 DE POKEMON:")
print(df.groupby('Type 1').count())

# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
print("\nESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON:")
print(df.groupby(['Type 1', 'Type 2']).count())

# LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5)
print("\nLEER EL ARCHIVO CSV POR CHUNKS (chunksize=5):")
chunk_size = 5
for chunk in pd.read_csv('pokemon_data.csv', chunksize=chunk_size):
    print(chunk)