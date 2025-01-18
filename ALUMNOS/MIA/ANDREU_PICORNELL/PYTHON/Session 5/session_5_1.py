import pandas as pd

df = pd.read_csv("pokemon_data.csv")

# IMPRIMIR TODOS LOS VALORES
def imprimir_valores(df):
    print(df)

# IMPRIMIR LOS PRIMEROS 5
def imprimir_5_primeros_valores(df):
    print(df.head())

# IMPRIMIR LOS ÚLTIMOS 5
def imprimir_5_ultimos_valores(df):
    print(df.tail())

# OBTENER NOMBRES DE LAS COLUMNAS
def obtener_nombre_columnas(df):
    print(df.columns)
    return df.columns

# OBTENER TODOS LOS NOMBRES
def obtener_nombres(df):
    print(df['Name'])
    return df['Name']

# OBTENER TODOS LOS NOMBRES Y VELOCIDADES
def obtener_nombres_y_velocidades(df):
    print(df[['Name','Speed']])
    return df[['Name','Speed']]

# LOS PRIMEROS 5 NOMBRES USANDO [::]
def obtener_5_primeros_nombres(df):
    print(df['Name'][:5])
    return df['Name'][:5]

# OBTENER TODAS LAS FILAS
def obtener_todas_las_filas(df):
    print(df)
    return df

# OBTENER UN RANGO DE FILAS
def obtener_rango_filas(df, inicio, fin):
    print(df.iloc[inicio:fin])
    return(df.iloc[inicio:fin])

# OBTENER EL NOMBRE DE LA FILA 10
def obtener_nombre_fila(df, fila):
    print(df.iloc[fila]['Name'])
    return(df.iloc[fila]['Name'])

# ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
def iterar_y_mostrar_indice_nombre(df):
    for index, row in df.iterrows():
        print(f"Índice: {index}, Nombre: {row['Name']}")

# POKEMONS DE TIPO 1 == WATER
def filtrar_pokemons_tipo_1_agua(df):
    print(df[df['Type 1'] == 'Water'])

# ESTADÍSTICAS (usando Describe del DataFrame)
def estadisticas_describe(df):
    print(df.describe())

# ORDENACIÓN POR NOMBRE ASCENDENTE
def ordenar_por_nombre(df):
    print(df.sort_values(by='Name'))

# CREAR UNA COLUMNA EXTRA CALCULADA
# La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
# La columna debe llamarse TOTAL
def crear_columna_total(df):
    df['TOTAL'] = df['HP'] + df['Attack'] + df['Defense'] + df['Speed']
    print(df)

# ELIMINAR LA COLUMNA TOTAL
def eliminar_columna_total(df):
    df.drop(columns=['TOTAL'], inplace=True)
    print(df)

# FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
def filtrar_pokemons_grass_poison(df):
    print(df[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])

# FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON"
def filtrar_pokemons_tipo_fire_poison(df):
    print(df[(df['Type 1'] == 'Fire') | (df['Type 2'] == 'Poison')])

# FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
def filtrar_grass_poison_hp(df):
    print(df[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] >= 70)])

# FILTRAR POKEMONS CON NOMBRE "MEGA"
def filtrar_pokemons_mega(df):
    print(df[df['Name'].str.contains('Mega')])

# FILTRAR POKEMONS SIN NOMBRE "MEGA"
def filtrar_pokemons_sin_mega(df):
    print(df[~df['Name'].str.contains('Mega')])

# FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
def filtrar_pokemons_pi(df):
    print(df[df['Name'].str.startswith('Pi')])

# RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
def renombrar_fire_a_flame(df):
    df['Type 1'] = df['Type 1'].replace('Fire', 'Flame')
    print(df)

# RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
def renombrar_flame_a_fire(df):
    df['Type 1'] = df['Type 1'].replace('Flame', 'Fire')
    print(df)

# CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
def cambiar_tipos_legendarios_a_fire(df):
    df.loc[df['Legendary'] == True, 'Type 1'] = 'Fire'
    print(df)

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
def estadisticas_media_por_tipo_ordenado_defensa(df):
    # Seleccionar solo las columnas numéricas
    columnas_numericas = df.select_dtypes(include=['number']).columns
    # Agrupar por 'Type 1' y calcular la media solo para las columnas numéricas
    resultado = df.groupby('Type 1')[columnas_numericas].mean().sort_values(by='Defense')
    print(resultado)

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
def estadisticas_media_por_tipo_ordenado_ataque(df):
    columnas_numericas = df.select_dtypes(include=['number']).columns
    resultado = df.groupby('Type 1')[columnas_numericas].mean().sort_values(by='Attack')
    print(resultado)

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
def estadisticas_media_por_tipo_ordenado_hp(df):
    columnas_numericas = df.select_dtypes(include=['number']).columns
    resultado = df.groupby('Type 1')[columnas_numericas].mean().sort_values(by='HP')
    print(resultado)

# (Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
def estadisticas_suma_por_tipo(df):
    columnas_numericas = df.select_dtypes(include=['number']).columns
    print(df.groupby('Type 1')[columnas_numericas].sum())

# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 DE POKEMON
def estadisticas_numero_por_tipo(df):
    print(df.groupby('Type 1').size())

# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
def estadisticas_numero_por_tipo_1_y_2(df):
    print(df.groupby(['Type 1', 'Type 2']).size())

# Nota: SI TENEMOS ARCHIVOS ENORMES (1TB) PODEMOS LEERLOS POR PARTES Cada fila podría estar acumulando cerca de 20 bytes, por lo que podríamos estar trabajando con cantidades enormes
# LEE EL ARCHIVO CSV SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5)
# ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA
def leer_csv_por_chunks(filepath, chunksize=5):
    for chunk in pd.read_csv(filepath, chunksize=chunksize):
        print(chunk)


# Llamando a todas las funciones

#imprimir_valores(df)
#imprimir_5_primeros_valores(df)
#imprimir_5_ultimos_valores(df)
#obtener_nombre_columnas(df)
#obtener_nombres(df)
#obtener_nombres_y_velocidades(df)
#obtener_5_primeros_nombres(df)
#obtener_todas_las_filas(df)
#obtener_rango_filas(df, 5, 15)
#obtener_nombre_fila(df, 10)
#iterar_y_mostrar_indice_nombre(df)
#filtrar_pokemons_tipo_1_agua(df)
#estadisticas_describe(df)
#ordenar_por_nombre(df)
#crear_columna_total(df)
#eliminar_columna_total(df)
#filtrar_pokemons_grass_poison(df)
#filtrar_pokemons_tipo_fire_poison(df)
#filtrar_grass_poison_hp(df)
#filtrar_pokemons_mega(df)
#filtrar_pokemons_sin_mega(df)
#filtrar_pokemons_pi(df)
#renombrar_fire_a_flame(df)
#renombrar_flame_a_fire(df)
#cambiar_tipos_legendarios_a_fire(df)
#estadisticas_media_por_tipo_ordenado_defensa(df)
#estadisticas_media_por_tipo_ordenado_ataque(df)
#estadisticas_media_por_tipo_ordenado_hp(df)
#estadisticas_suma_por_tipo(df)
#estadisticas_numero_por_tipo(df)
#estadisticas_numero_por_tipo_1_y_2(df)
leer_csv_por_chunks('pokemon_data.csv', chunksize=5)