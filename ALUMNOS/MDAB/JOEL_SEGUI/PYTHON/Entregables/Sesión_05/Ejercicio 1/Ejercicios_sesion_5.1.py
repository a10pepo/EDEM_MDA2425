import pandas as pd

datos = "pokemon_data.csv"

df = pd.read_csv(datos)

# - IMPRIMIR TODOS LOS VALORES
print(df)

# - IMPRIMIR LOS PRIMEROS 5
print(df.head())

# - IMPRIMIR LOS ÚLTIMOS 5
print(df.tail())
# - OBTENER NOMBRES DE LAS COLUMNAS
print(df.columns)

# - OBTENER TODOS LOS NOMBRES
print(df['Name'])

# - OBTENER TODOS LOS NOMBRES Y VELOCIDADES
print(df[['Name', 'Speed']])

# - LOS PRIMEROS 5 NOMBRES USANDO [::]
print(df['Name'][::5])

# - OBTENER TODAS LAS FILAS
print(df.iloc[:, :])

# - OBTENER UN RANGO DE FILAS
print(df[10:15])

# - OBTENER EL NOMBRE DE LA FILA 10
print(df.iloc[10]['Name'])

# - ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
for index, row in df.iterrows():
    print(index, row['Name'])

# - POKEMONS DE TIPO 1 == WATER
print(df[df['Type 1'] == 'Water'])

# - ESTADÍSTICAS (usando Describe del DafaFrame)
print(df.describe())

# - ORDENACIÓN POR NOMBRE ASCENDENTE
print(df.sort_values(by = 'Name'))

# - CREAR UNA COLUMNA EXTRA CALCULADA
        # - La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
        # - La columna debe llamarse TOTAL
df['TOTAL'] = df['HP'] + df['Attack'] + df['Defense'] + df['Speed'] #Creo que no se ha creado
print(df.columns) #Si que existe pero no se llega a ver por el tamaño o algo

# - ELIMINAR LA COLUMNA TOTAL
df.drop(columns=['TOTAL'], inplace=True)

# - FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
print(df[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])

# - FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON
print(df[(df['Type 1'] == 'Fire') | (df['Type 2'] == 'Poison')])

# - FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
print(df[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] >= 70)])

# - FILTRAR POKEMONS CON NOMBRE "MEGA"
print(df[df['Name'].str.contains('Mega')])

# - FILTRAR POKEMONS SIN NOMBRE "MEGA"
print(df[~df['Name'].str.contains('Mega')])

# - FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
print(df[df['Name'].str.startswith('Pi')])

# - RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flame'
print(df.head(10)) #Funciona

# - RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
df.loc[df['Type 1'] == 'Flame', 'Type 1'] = 'Fire'
print(df.head(10)) #Funciona

# - CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
df.loc[df['Legendary'] == True, 'Type 1'] = 'Fire'
print(df.tail(10)) #Se ha hecho correctamente

# - (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA

        # Agrupar por "Type 1" y calcular la media, seleccionando solo las columnas numéricas
mean_stats_by_type = df.groupby('Type 1').mean(numeric_only=True).sort_values(by='Defense')

        # Imprimir los resultados
print(mean_stats_by_type)

# - (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE

        # Agrupar por "Type 1" y calcular la media, seleccionando solo las columnas numéricas y ordenando por "Attack"
mean_stats_by_attack = df.groupby('Type 1').mean(numeric_only=True).sort_values(by='Attack')

        # Imprimir los resultados
print(mean_stats_by_attack)

# - (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP

        # Agrupar por "Type 1" y calcular la media, seleccionando solo las columnas numéricas y ordenando por "Attack"
mean_stats_by_attack = df.groupby('Type 1').mean(numeric_only=True).sort_values(by='HP')

        # Imprimir los resultados
print(mean_stats_by_attack)

# - (Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
                
                # Agrupar por "Type 1" y calcular la media, seleccionando solo las columnas numéricas y ordenando por "Attack"
mean_stats_by_attack = df.groupby('Type 1').mean(numeric_only=True).sort_values(by='HP')

        # Imprimir los resultados
print(mean_stats_by_attack)

# - (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON
                
                # Agrupar por "Type 1" y calcular la suma, seleccionando solo las columnas numéricas
sum_stats_by_type = df.groupby('Type 1').sum(numeric_only=True)

                # Imprimir los resultados
print(sum_stats_by_type)

# - (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
                #Contar el número de Pokémon por "Type 1" y "Type 2"
count_by_types = df.groupby(['Type 1', 'Type 2']).size()

                # Imprimir los resultados
print(count_by_types)

# -----EXTRA-------

#- LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE  (chunksize=5)
chunks = pd.read_csv('pokemon_data.csv', chunksize=5)

# Procesar cada chunk
for chunk in chunks:
    # Aquí puedes realizar operaciones con cada chunk
    print(chunk)



#- ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}:")
    print(chunk)
    print("\n")  # Añadir una línea en blanco para mayor legibilidad