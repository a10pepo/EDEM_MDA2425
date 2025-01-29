# Lee el archivo CSV con Pandas de 'pokemon_data.csv' alojado en la carpeta de datos de este repositorio y 
# realizar las siguientes operaciones

#Lee el archivo CSV con Pandas
import pandas as pd
pokemon = pd.read_csv("CLAUDIA_ROMERO/PYTHON/Entregables/Sesion_5/Ejercicio_1/pokemon_data.csv")

#IMPRIMIR TODOS LOS VALORES
print(pokemon)

#IMPRIMIR LOS PRIMEROS 5
print(pokemon.head())

#IMPRIMIR LOS ÚLTIMOS 5
print(pokemon.tail())

#OBTENER NOMBRES DE LAS COLUMNAS
print(pokemon.columns)

#OBTENER TODOS LOS NOMBRES
print(pokemon["Name"])

# OBTENER TODOS LOS NOMBRES Y VELOCIDADES
print(pokemon[["Name", "Speed"]])

# LOS PRIMEROS 5 NOMBRES USANDO [::]
print(pokemon["Name"][:5])

# OBTENER TODAS LAS FILAS
print(pokemon)

# OBTENER UN RANGO DE FILAS
print(pokemon.iloc[10:21])

# OBTENER EL NOMBRE DE LA FILA 10
print(pokemon.iloc[9]["Name"])

# ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
for indice, fila in pokemon.iterrows():
    print(f"Índice: {indice}, Pokemon: {fila["Name"]}")

# POKEMONS DE TIPO 1 == WATER
water = pokemon[pokemon["Type 1"] == "Water"]
print(water)

# ESTADÍSTICAS (usando Describe del DafaFrame)
print(pokemon.describe())

# ORDENACIÓN POR NOMBRE ASCENDENTE
print(pokemon["Name"].sort_values(ascending=True))

# CREAR UNA COLUMNA EXTRA CALCULADA
# La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
# La columna debe llamarse TOTAL
pokemon["TOTAL"] = pokemon["HP"] + pokemon["Attack"] + pokemon["Defense"] + pokemon["Speed"]
print(pokemon[["Name", "TOTAL"]])

# ELIMINAR LA COLUMNA TOTAL
pokemon = pokemon.drop("TOTAL", axis=1)

# FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
print(pokemon[(pokemon["Type 1"] == "Grass") | (pokemon["Type 1"] == "Poison")])

# FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON
print(pokemon[(pokemon["Type 1"] == "Fire") | (pokemon["Type 1"] == "Poison")])

# FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
print(pokemon[((pokemon["Type 1"] == "Grass") | (pokemon["Type 1"] == "Poison")) & (pokemon["HP"] >= 70)])

# FILTRAR POKEMONS CON NOMBRE "MEGA"
print(pokemon[pokemon["Name"].str.contains("Mega")])

# FILTRAR POKEMONS SIN NOMBRE "MEGA"
print(pokemon[~pokemon["Name"].str.contains("Mega")])

# FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
print(pokemon[pokemon["Name"].str.startswith("Pi")])

# RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
pokemon["Type 1"].replace("Fire", "Flame", inplace=True)
print(pokemon)

# RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
pokemon["Type 1"].replace("Flame", "Fire", inplace=True)
print(pokemon)

# CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
pokemon.loc[pokemon["Legendary"] == True, "Type 1"] = "Fire"
# Cambiar el tipo de todos los Pokémon legendarios a "Fire"
pokemon.loc[pokemon["Legendary"] == True, "Type 1"] = "Fire"

# Imprimir los Pokémon legendarios con tipo "Fire"
pokemon.loc[pokemon["Legendary"] == True, "Type 1"] = "Fire"
print(pokemon[pokemon["Legendary"] == True][["Name", "Type 1", "Legendary"]])

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
print(pokemon.groupby("Type 1").mean(numeric_only=True).sort_values("Defense"))

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
print(pokemon.groupby("Type 1").mean(numeric_only=True).sort_values("Attack"))

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
print(pokemon.groupby("Type 1").mean(numeric_only=True).sort_values("HP"))

# (Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
print(pokemon.groupby("Type 1").sum(numeric_only=True))

# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 DE POKEMON
print(pokemon.groupby("Type 1").size())

# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
print(pokemon.groupby(["Type 1", "Type 2"]).size())

# Nota: SI TENEMOS ARCHIVOS ENORMES (1TB) PODEMOS LEERLOS POR PARTES Cada fila podría estar acumulando cerca de 
# 20 bytes, por lo que podríamos estar trabajando con cantidades enormes
# LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5)
# ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA
for chunk in pd.read_csv("CLAUDIA_ROMERO/PYTHON/Entregables/Sesion_5/Ejercicio_1/pokemon_data.csv", chunksize=5):
    print(chunk)