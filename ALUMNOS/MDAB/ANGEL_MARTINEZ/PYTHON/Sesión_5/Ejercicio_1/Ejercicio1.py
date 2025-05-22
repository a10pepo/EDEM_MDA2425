import pandas as pd

pokemons= pd.read_csv('pokemon_data.csv')

#IMPRIMIR TODOS LOS VALORES
print(pokemons)
#IMPRIMIR LOS PRIMEROS 5

print(pokemons.head(5))
#IMPRIMIR LOS ÚLTIMOS 5
print(pokemons.tail(5))

#OBTENER NOMBRES DE LAS COLUMNAS
print(pokemons.columns)

#OBTENER TODOS LOS NOMBRES
print(pokemons["Name"])


#OBTENER TODOS LOS NOMBRES Y VELOCIDADES
print(pokemons[["Name", "Speed"]])


#LOS PRIMEROS 5 NOMBRES USANDO [::]
print(pokemons["Name"][:5])


#OBTENER TODAS LAS FILAS
print(pokemons)


# OBTENER UN RANGO DE FILAS
print(pokemons[10:21])

# OBTENER EL NOMBRE DE LA FILA 10
print(pokemons.loc[9, "Name"])

# ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
for index, row in pokemons.iterrows():
    print(index, row["Name"])

# POKEMONS DE TIPO 1 == WATER
print(pokemons[pokemons["Type 1"] == "Water"])

# ESTADÍSTICAS (usando Describe del DataFrame)
print(pokemons.describe())

# ORDENACIÓN POR NOMBRE ASCENDENTE
print(pokemons.sort_values("Name"))

# CREAR UNA COLUMNA EXTRA CALCULADA
# La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
pokemons["Total"] = pokemons["HP"] + pokemons["Attack"] + pokemons["Defense"] + pokemons["Speed"]
print(pokemons)

# ELIMINAR LA COLUMNA TOTAL
pokemons = pokemons.drop(columns=["Total"])
print(pokemons)

# FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
print(pokemons[(pokemons["Type 1"] == "Grass") & (pokemons["Type 2"] == "Poison")])

# FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON"
print(pokemons[(pokemons["Type 1"] == "Fire") | (pokemons["Type 2"] == "Poison")])

# FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
print(pokemons[(pokemons["Type 1"] == "Grass") & (pokemons["Type 2"] == "Poison") & (pokemons["HP"] >= 70)])

# FILTRAR POKEMONS CON NOMBRE "MEGA"
print(pokemons[pokemons["Name"].str.contains("Mega")])

# FILTRAR POKEMONS SIN NOMBRE "MEGA"
print(pokemons[~pokemons["Name"].str.contains("Mega")])

# FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
print(pokemons[pokemons["Name"].str.startswith("Pi")])

# RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
pokemons = pokemons.rename(columns={"Type 1": "Flame"})
print(pokemons)

# RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
pokemons = pokemons.rename(columns={"Flame": "Type 1"})
print(pokemons)

# CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
pokemons.loc[pokemons["Legendary"] == True, "Type 1"] = "Fire"
print(pokemons)

# ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
print(pokemons.groupby("Type 1").mean().sort_values("Defense"))

# ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
print(pokemons.groupby("Type 1").mean().sort_values("Attack"))

# ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
print(pokemons.groupby("Type 1").mean().sort_values("HP"))

# ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
print(pokemons.groupby("Type 1").sum())

# ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 DE POKEMON
print(pokemons["Type 1"].value_counts())

# ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
print(pokemons.groupby(["Type 1", "Type 2"]).size())