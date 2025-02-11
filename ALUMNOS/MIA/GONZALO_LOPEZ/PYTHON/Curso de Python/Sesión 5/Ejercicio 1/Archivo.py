# Lee un archivo CSV con Pandas y realizar las siguientes operaciones
import pandas as pd
df = pd.read_csv("C:\\Users\\Usuario\\Documents\\Master IA\\MIA 24-25\\PYTHON\\PYTHON\\Curso de Python\\Sesión 5\\Ejercicio 1\\pokemon_data.csv")  # LEER EL ARCHIVO CSV

#print(df)  # Mostrar todos los valores
#print(df.head(5)) # Mostrar los 5 primeros valores
#print(df.tail(5)) # Mostrar los 5 últimos valores
# print(df.columns) # Obtener el nombre de las columnas
#print(df['Name']) # Obtener todos los nombres
#print(df[['Name','Speed']]) # Obtener los nombres y velocidades
#print(df['Name'][0:6:1]) # Obtener los 5 primeros nombres usando [::]
#print(df) # Obtener todas las filas
#print(df.iloc[0:21]) # Obtener un rango de filas
#print(df.iloc[0:21,0:5]) # Obtener un rango de filas y de columnas a la vez
#print("El nombre del pokemon de la fila 10 es :", df.iloc[11]['Name']) # Obtener el nombre de la fila 10

#ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
# for index, row in df.iterrows():
#   print(f'Indice: {index}, Nombre: {row['Name']}')

#POKEMONS DE TIPO 1 == WATER
# print(df[df['Type 1']=='Water']['Name'])

#ESTADÍSTICAS (usando Describe del DafaFrame)
# print(df.describe)

# ORDENACIÓN POR NOMBRE ASCENDENTE
# print(df.sort_values(by='Name',ascending=True))  # ascending=True (de la A  a la Z)

#CREAR UNA COLUMNA EXTRA CALCULADA
# La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
# La columna debe llamarse TOTAL
# df['TOTAL']=df['HP']+df['Attack']+df['Defense']+df['Speed']
# print(df)

#ELIMINAR LA COLUMNA TOTAL
# df=df.drop(columns=['TOTAL'])
# print(df)

# Selecciona todas las filas y algunas columnas
#df.iloc[0:20](excluye el final), df.loc[0:20](incluye el final)
#df.iloc utiliza INDICES de las columnas, df.loc solo utiliza NOMBRES/ETIQUETAS de las columnas
# print(df.iloc[:,[1,2,5]])

# FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
# print(df)
# print(df[df['Type 1']=='Grass'][df['Type 2']=='Poison']) # Así primero aplica 1 filtro , y después el otro filtro sobre el primero

#QUEREMOS APLICAR LOS DOS FILTROS A LA VEZ 
# filtered_df = df[(df['Type 1']=='Grass')&(df['Type 2']=='Poison')]
# print(filtered_df)

# FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON
# df_filtrado=df[(df['Type 1']=='Fire') | (df['Type 2']=='Poison')]
# print(df_filtrado)

# FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
# filtred_df=df[(df['Type 1']=='Grass')&(df['Type 2']=='Poison')&(df['HP']>=70)]
# print(filtred_df)


# FILTRAR POKEMONS CON NOMBRE "MEGA"
# filtred_pokemons= df[df['Name'].str.contains('Mega',case=False, na=False)]
# print(filtred_pokemons)

# print(df)

# FILTRAR POKEMONS SIN NOMBRE "MEGA"
# filtered_pokemons=df[~df['Name'].str.contains('Mega', case=False,na=False)]
# print(filtered_pokemons)




# FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
# filtered_pokemon=df[df['Name'].str.lower().str.startswith('pi',na=False)]
# print(filtered_pokemon)

# RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
# df.rename(columns={'FIRE':'FLAME'},inplace=True)
# print(df)

# df= df.rename(columns={'Fire': ' Flame'})
# print(df)


# RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
# df=df.rename(columns={'Flame':'Fire'})
# print(df)


# CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"

# df.loc[df['Legendary'],'Type 1']='Fire'
# print(df[df['Legendary']])

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA

# stats_by_type= df.groupby('Type 1').mean(numeric_only=True).sort_values(by='Defense',ascending=False)
# print(stats_by_type)


# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE

# stats_by_type= df.groupby('Type 1').mean(numeric_only=True).sort_values(by='Attack',ascending=False)
# print(stats_by_type)

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
# stats_by_type=df.groupby('Type 1').mean(numeric_only=True).sort_values(by='HP', ascending=False)
# print(stats_by_type)



# (Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
# stats_by_type=df.groupby('Type 1').sum(numeric_only=True)
# print(stats_by_type)



# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON
# stats_by_type=df.groupby('Type 1').size()
# print(stats_by_type)


# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
# stats_by_type=df.groupby(['Type 1','Type 2']).size()
# print(stats_by_type)








