import pandas as pd


pokemon_data_df = pd.read_csv("ENTREGABLES\pokemon_data.csv",
                              dtype ={
                                  "Name": str,
                                  "Type 1": str,
                                  "Type 2": str,
                                  "HP": int,
                                  "Attack": int,
                                  "Defense": int,
                                  "Sp.Atk": int,
                                  "Sp.Def": int,
                                  "Speed": int,
                                  "Generation":int,
                                  "Legendary": bool


                              })

columnas_numericas = pokemon_data_df.select_dtypes(include=["number"])
pokemon_datos = pokemon_data_df[['Type 1']].join(columnas_numericas)

#Imprimir todos los valores
print(pokemon_data_df)

#Leer los primeros 5
print(pokemon_data_df.head(5))

#Leer los ultimos 5
print(pokemon_data_df.tail(5))

#Nombres columnas
print(pokemon_data_df.columns)

#Obtener todos los nombres
print(pokemon_data_df["Name"])

#Obtener todos los nombres y velocidades
lista_combinada = ["Name", "Speed"]
nombre_y_velocidades = pokemon_data_df[lista_combinada]
print(nombre_y_velocidades) 

#Obtener rango de los 5 primeros
print(pokemon_data_df["Name"][0:5])

# OBTENER TODAS LAS FILAS
print(pokemon_data_df.iloc[:])

# OBTENER UN RANGO DE FILAS
print(pokemon_data_df.iloc[0:5])

# OBTENER EL NOMBRE DE LA FILA 10
print(pokemon_data_df.iloc[10]["Name"]) #Wartotle

# ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA

for i, pokemon in pokemon_data_df.iterrows():
    print(f"{i} - {pokemon["Name"]}")

# POKEMONS DE TIPO 1 == WATER
tipo_agua = pokemon_data_df["Type 1"] == "Water"
pokemon_tipo_agua = pokemon_data_df[tipo_agua]
print(pokemon_tipo_agua) 

# ESTADÍSTICAS (usando Describe del DafaFrame)
print(pokemon_data_df.describe()) #resumen datos

# ORDENACIÓN POR NOMBRE ASCENDENTE
print(pokemon_data_df.sort_values("Name",  ascending = True))

# CREAR UNA COLUMNA EXTRA CALCULADA
# La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
# La columna debe llamarse TOTAL

pokemon_data_df["Total"] = pokemon_data_df["HP"] + pokemon_data_df["Attack"] + pokemon_data_df["Defense"] + pokemon_data_df["Speed"]
print(pokemon_data_df["Total"])
print(pokemon_data_df) #comprobar que 'Total' esta creada


# ELIMINAR LA COLUMNA TOTAL
pokemon_data_df = pokemon_data_df.drop("Total", axis = 1)
print(pokemon_data_df) #comprobar que 'Total' esta borrada

# FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"

pokemon_planta_y_veneno = pokemon_data_df[
    (pokemon_data_df["Type 1"] == "Grass") & (pokemon_data_df["Type 2"] == "Poison")
]

print(pokemon_planta_y_veneno)


# FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON
pokemon_fuego_o_veneno = pokemon_data_df[
    (pokemon_data_df["Type 1"].isin(["Fire", "Poison"])) |
    (pokemon_data_df["Type 2"].isin(["Fire", "Poison"]))
 ]

print(pokemon_fuego_o_veneno)

# FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70

pokemon_planta_y_veneno = pokemon_data_df[
    (pokemon_data_df["Type 1"] == "Grass") & (pokemon_data_df["Type 2"] == "Poison") & (pokemon_data_df["HP"] >= 70)
]

print(pokemon_planta_y_veneno)

# FILTRAR POKEMONS CON NOMBRE "MEGA"

pokemon_mega = pokemon_data_df[
    (pokemon_data_df["Name"].str.contains("Mega"))
]

print(pokemon_mega)

# FILTRAR POKEMONS SIN NOMBRE "MEGA"
pokemon_sin_mega = pokemon_data_df[
    (~pokemon_data_df["Name"].str.contains("Mega"))
]

print(pokemon_sin_mega)

# FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
pokemon_pi = pokemon_data_df[
    (pokemon_data_df["Name"].str.startswith("Pi"))
]

print(pokemon_pi)

# RENOMBRADO DE COLUMNA "FIRE" a "FLAME"


pokemon_data_df["Type 1"].replace("Fire" , "Flame", inplace= True)
print(pokemon_data_df)

# RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA

pokemon_data_df["Type 1"].replace("Flame" , "Fire", inplace= True)
print(pokemon_data_df)

# CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"

pokemon_data_df.loc[pokemon_data_df["Legendary"] == True, "Type 1"] = "Fire"
print(pokemon_data_df)


# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA


print(pokemon_datos.groupby("Type 1").mean().sort_values("Defense"))



# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE


print(pokemon_datos.groupby("Type 1").mean().sort_values("Attack"))


# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP

print(pokemon_datos.groupby("Type 1").mean().sort_values("HP"))


# (Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON

print(pokemon_datos.groupby("Type 1").sum())


# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON

print(pokemon_data_df.groupby("Type 1").count()["Name"])

# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON

print(pokemon_data_df.groupby(["Type 1", "Type 2"]).count()["Name"])


# LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5)
# ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA

chunks = pd.read_csv("ENTREGABLES\pokemon_data.csv", chunksize= 5)

for chunk in chunks:
    print(chunk)





