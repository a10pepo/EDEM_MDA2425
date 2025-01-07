'''Lee el archivo CSV con Pandas de 'pokemon_data.csv' alojado en la carpeta de datos de este repositorio y realizar las siguientes operaciones'''

import pandas as pd 
df = pd.read_csv('pokemon_data.csv')

tamano_chunck = 5
for chunck in pd.read_csv('pokemon_data.csv', chunksize=tamano_chunck):

    '''IMPRIMIR TODOS LOS VALORES'''
    print(df)

    '''IMPRIMIR LOS PRIMEROS 5'''
    print(df.head(5))

    '''IMPRIMIR LOS ÚLTIMOS 5'''
    print(df.tail(5))

    '''OBTENER NOMBRES DE LAS COLUMNAS'''
    print(df.columns)

    '''OBTENER TODOS LOS NOMBRES'''
    nombre = df['Name']
    print(nombre)

    '''OBTENER TODOS LOS NOMBRES Y VELOCIDADES'''
    lista_columnas = df[['Name', 'Speed']]
    print(lista_columnas)

    '''LOS PRIMEROS 5 NOMBRES USANDO [::]'''
    nombre = df['Name'][0:5]
    print(nombre)

    '''OBTENER TODAS LAS FILAS'''
    filas = df.iloc[0:]
    print(filas)

    '''OBTENER UN RANGO DE FILAS'''
    filas = df.iloc[0:20]
    print(filas)

    '''OBTENER EL NOMBRE DE LA FILA 10'''
    fila = df.iloc[10]
    print(fila)

    '''ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA'''
    for indice, nombre in df.iterrows(): 
        print(indice, nombre['Name'])

    '''POKEMONS DE TIPO 1 == WATER'''
    condicion_tipo_1_agua = df['Type 1'] == 'Water'
    pokemon_de_tipo_agua = df.loc[ condicion_tipo_1_agua ] 
    print(pokemon_de_tipo_agua)

    '''ESTADÍSTICAS (usando Describe del DafaFrame)'''
    print(df.describe())

    '''ORDENACIÓN POR NOMBRE ASCENDENTE'''
    nombre = df.sort_values('Name',ascending = True )
    print(nombre)

    '''CREAR UNA COLUMNA EXTRA CALCULADA
    La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
    La columna debe llamarse TOTAL'''

    df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Speed']
    print(df['Total'])

    '''ELIMINAR LA COLUMNA TOTAL'''
    df = df.drop(columns=['Total'])
    print(df.columns)

    '''FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"'''
    condicion_tipo_1_poisson = df['Type 1'] == 'Poison'
    condicion_tipo_1_grass = df['Type 1'] == 'Grass'
    pokemon_de_tipo_poisson_grass = df.loc[ condicion_tipo_1_poisson | condicion_tipo_1_grass ] #localizar por una condicion
    print(pokemon_de_tipo_poisson_grass)

    '''FILTRAR POKEMONS DE TIPOS "FIRE" Y "POISON"'''
    condicion_tipo_1_poisson = df['Type 1'] == 'Poison'
    condicion_tipo_1_fire = df['Type 1'] == 'Fire'
    pokemon_de_tipo_poisson_fire = df.loc[ condicion_tipo_1_poisson | condicion_tipo_1_fire ] #localizar por una condicion
    print(pokemon_de_tipo_poisson_fire)

    '''FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70'''
    condicion_tipo_1_poisson = df['Type 1'] == 'Poison'
    condicion_tipo_1_grass = df['Type 1'] == 'Grass'
    hp = df['HP'] >= 70
    pokemon_de_tipo_poisson_grass = df.loc[ (condicion_tipo_1_poisson | condicion_tipo_1_grass) & hp] #localizar por una condicion
    print(pokemon_de_tipo_poisson_grass )

    '''FILTRAR POKEMONS CON NOMBRE "MEGA"'''
    resultado_filtrado = df[df['Name'].str.contains('Mega')]
    print(resultado_filtrado)

    '''FILTRAR POKEMONS SIN NOMBRE "MEGA"'''
    resultado_filtrado = df[~df['Name'].str.contains('Mega')]
    print(resultado_filtrado)

    '''FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"'''
    resultado_filtrado = df[df['Name'].str.contains('^PI', case=False, regex=True)]
    print(resultado_filtrado)

    '''RENOMBRADO DE COLUMNA "FIRE" a "FLAME"'''
    df['Type 1'] = df['Type 1'].replace({'Fire': 'Flame'})
    print(df)

    '''RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA'''
    df['Type 1'] = df['Type 1'].replace({'Flame': 'Fire'})
    print(df)

    '''CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"'''
    cambio = df.loc[df['Legendary'], 'Type 1'] = 'Fire'
    print(df)

    '''(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA'''
    estadisticas_defensa = df.groupby('Type 1')['Defense'].mean().reset_index()
    estadisticas_defensa = estadisticas_defensa.sort_values(by='Defense', ascending=False)
    print(estadisticas_defensa)

    '''(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE'''
    estadisticas_ataque = df.groupby('Type 1')['Attack'].mean().reset_index()
    estadisticas_ataque = estadisticas_ataque.sort_values(by='Attack', ascending=False)
    print(estadisticas_ataque)

    '''(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP'''
    estadisticas_hp = df.groupby('Type 1')['HP'].mean().reset_index()
    estadisticas_hp = estadisticas_hp.sort_values(by='HP', ascending=False)
    print(estadisticas_hp)

    '''(Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON'''
    suma= df.groupby('Type 1').sum()
    print(suma)

    '''(Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON'''
    estadisticas_contar = df.groupby('Type 1')['Name'].count().reset_index()
    print(estadisticas_contar)

    '''(Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON'''
    estadisticas_contar = df.groupby(['Type 1', 'Type 2'])['Name'].count().reset_index()
    print(estadisticas_contar)