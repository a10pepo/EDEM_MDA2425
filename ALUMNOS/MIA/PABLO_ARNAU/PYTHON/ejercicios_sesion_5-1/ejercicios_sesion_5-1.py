import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#    IMPRIMIR TODOS LOS VALORES

# print(df)

#     IMPRIMIR LOS PRIMEROS 5
# print(df.head())

#     IMPRIMIR LOS ÚLTIMOS 5
# print(df.tail())

#     OBTENER NOMBRES DE LAS COLUMNAS
# print(df.columns.tolist())

#     OBTENER TODOS LOS NOMBRES
# print(df['Name'].tolist())

#     OBTENER TODOS LOS NOMBRES Y VELOCIDADES
# print(df[['Name','Speed']])

#     LOS PRIMEROS 5 NOMBRES USANDO [::]
# print(df['Name'][:5])

#     OBTENER TODAS LAS FILAS
# print(df)

#     OBTENER UN RANGO DE FILAS
# print(df[4:16])

#     OBTENER EL NOMBRE DE LA FILA 10
# print(df['Name'][10:11])

#     ITERAR POR TODOS MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
'''for index, row in df.iterrows():
    print(row['#'],row['Name'])'''

#     POKEMONS DE TIPO 1 == WATER

# print(df[df['Type 1'] == 'Water'])

#     ESTADÍSTICAS (usando Describe del DafaFrame)
'''estadisticas = df.describe ()
print (estadisticas)'''

#     ORDENACIÓN POR NOMBRE ASCENDENTE
# print (df.sort_values ('Name'))

#     CREAR UNA COLUMNA EXTRA CALCULADA
#         La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
#         La columna debe llamarse TOTAL

'''df['Total'] = df['HP']+ df['Attack']+df['Defense']+df['Speed']
print(df['Total'])'''

#     ELIMINAR LA COLUMNA TOTAL

# df = df.drop(columns=['Total'])

#     FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"

# print (df[(df['Type 1'].isin(['Grass', 'Poison'])) | (df['Type 2'].isin(['Grass', 'Posion']))])

#     FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON

# print (df[(df['Type 1'].isin(['Fire', 'Poison'])) | (df['Type 2'].isin(['Fire', 'Posion']))])

#     FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70

#print (df[((df['Type 1'] == 'GRASS') | (df['Type 2'] == 'GRASS')) & ((df['Type 1'] == 'POISON') | (df['Type 2'] == 'POISON')) & (df['HP'] >= 70)])

#     FILTRAR POKEMONS CON NOMBRE "MEGA" habría que poner 'Mega' y 'mega'

# print (df[df['Name'].str.contains("mega")])

#     FILTRAR POKEMONS SIN NOMBRE "MEGA" habría que poner 'Mega' y 'mega'

# print (df[~df['Name'].str.contains("mega")])

#     FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"

# (df[df['Name'].str.startswith("Pi")])

#     RENOMBRADO DE COLUMNA "FIRE" a "FLAME"

# df.rename(columns={'Fire': 'Flame'}, inplace=True)

#     RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA

# df.rename(columns={'Flame': 'Fire'}, inplace=True)

#     CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"

# df.loc[df['Legendary'], 'Type 1'] = 'Fire'
# print(df)

#     (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA

# print(df.groupby('Type 1')['Defense'].mean())

#     (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
# print(df.groupby('Type 1')['Attack'].mean())

#     (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
# print(df.groupby('Type 1')['HP'].mean())

#     (Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
# print(df.groupby('Type 1').sum())

#     (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON

# print(df.groupby('Type 1').size().reset_index(name='Cantidad'))

#     (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON

# print (df.groupby(['Type 1', 'Type 2']).size().reset_index(name='Cantidad'))

#LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5)
#ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA

for chunk in pd.read_csv('pokemon_data.csv', chunksize=5):
    print(chunk)



