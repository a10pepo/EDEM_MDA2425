import pandas as pd

df = pd.read_csv('pokemon_data.csv')


#IMPRIMIR TODOS LOS VALORES

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(df)


#IMPRIMIR LOS 5 PRIMEROS
print(df.head(5))

#IMPRIMIR LOS ÚLTIMOS
print(df.tail(5))

#IMPRIMIR EL NOMBRE DE LAS COLUMNAS
print(df.columns)

#IMPRIMIR TODOS LOS NOMBRES
pd.set_option('display.max_rows', None)
print(df['Name'])

#IMPRIMIR TODOS LOS NOMBRES Y VELOCIDADES
pd.set_option('display.max_rows', None)
print(df[['Name', 'Speed']])

#IMPRIMIR LOS 5 PRIMEROS NOMBRES UTILIZANDO [:]

print(df['Name'][:5])

#IMPRIMIR TODAS LAS FILAS
pd.set_option('display.max_rows', None)
print(df)

#IMPRIME EL NOMBRE DE LA FILA 10
print(df['Name'][10])

#ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA

for index, row in df.iterrows():
    print(f'Índice: {index}, Nombre: {row["Name"]}')

#POKEMONS DE TIPO 1 == WATER

print(df[df['Type 1'] == 'Water'])

#ESTADÍSTICAS (usando Describe del DafaFrame)
print(df.describe())

#ORDENACIÓN POR NOMBRE ASCENDENTE
Ascendente = df.sort_values('Name', ascending=True)
print(Ascendente)

#CREAR UNA COLUMNA EXTRA CALCULADA
df['Total'] = (df['HP']+ df['Attack'] + df['Defense'] + df['Speed'])
print(df['Total'])


#ELIMINAR LA COLUMNA
df = df.drop('Total', axis=1)
print(df)

#FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"

grass_poison= df[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
print(grass_poison)

#FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON

fire_poison = df[(df['Type 1'] == 'Poison') | (df['Type 1'] == 'Fire')]
print(fire_poison)

#FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
tipo_hp = df[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] >= 70)]
print(tipo_hp)

#FILTRAR POKEMONS CON NOMBRE "MEGA"

MEGA = df[df['Name'].str.contains('Mega')]
print(MEGA)

#FILTRAR POKEMONS SIN NOMBRE "MEGA"

NO_MEGA = df[~df['Name'].str.contains('Mega')]
print(NO_MEGA)

#FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
PI = df[df['Name'].str.startswith('Pi')]
# print(PI)

#RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
df['Type 1'] = df['Type 1'].replace('Fire' , 'Flame')

print(df)

#RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA

df['Type 1'] = df['Type 1'].replace('Flame', 'Fire')
print(df)

#CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
df.loc[df['Legendary'] == True, 'Type 1'] = 'Fire'
print(df)

#Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA

media_tipo_pokemon = df.groupby('Type 1')['Sp. Def'].mean()
print(media_tipo_pokemon)

#ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
media_tipo_ataque = df.groupby('Type 1')['Sp. Atk'].mean()
media_ataque_ordenada = media_tipo_ataque.sort_values(ascending=False)
print(media_ataque_ordenada)

#ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
media_hp = df.groupby('Type 1')['HP'].mean()
media_hp_ordenada = media_hp.sort_values(ascending=False)
print(media_hp_ordenada)

#ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
columnas_deseadas= ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary']
sumatotal_tipo = df.groupby('Type 1')[columnas_deseadas].sum()
sumatotal_tipo['Total'] = sumatotal_tipo.sum(axis=1)
print(sumatotal_tipo)


#ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON

numero_de_pokemon1 = df.groupby('Type 1').size()
print(numero_de_pokemon1)

#ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON

numero_pokemon1 = df.groupby('Type 1').size()
numero_pokemon2 = df.groupby('Type 2').size()

print(numero_pokemon1)
print(numero_pokemon2)


#EJERCICIO 2 
#Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
#Arrancar
#Acelerar
#Frenar
#Parar

class Automovil():
    marca : str
    modelo : str
    matricula : int
    velocidad : int
    arrancado : bool

    def __init__(self, marca: str, modelo: str, matricula: int):
            self.marca = marca
            self.modelo = modelo 
            self.matricula = matricula
            self.arrancado = False
            self.velocidad = 0

    def arrancar(self):
        if not self.arrancado:
             self.arrancado = True
             print(f'El {self.marca} se ha arrancado')
    
    def acelerar(self, incremento: int):
         if self.arrancado:
              self.velocidad += incremento
              print(f'El {self.marca} lleva una velocidad de {self.velocidad}')
    def frenar(self, decremento: int):
         if self.arrancado:
              self.velocidad -= decremento
              if self.velocidad < 0:
                   self.velocidad = 0
                   print(f'ahora va a {self.velocidad} por hora')
    def parar(self):
            if self.arrancado:
              self.arrancado = False
              self.velocidad = 0
              print(f'el {self.marca} se ha parado')
            else:
                 print(f'el {self.marca} ya estaba parado')
    def informacion(self):
         estado = 'arrancado' if self.arrancado else 'parado'
         print(f"Marca: {self.marca}, Modelo: {self.modelo}, Matrícula: {self.matricula}, Velocidad: {self.velocidad} km/h, Estado: {estado}")

mi_vehiculo = Automovil('Ferrari', 'Roma', 44456)
mi_vehiculo.informacion()
mi_vehiculo.arrancar()
mi_vehiculo.acelerar(100)
mi_vehiculo.informacion()


#EJERCICIO 3 
#Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:
#Coche
#Moto
#Camión

class Coche(Automovil):
     numero_puertas = int
     caballos = int
     carburante = str

     def __init__(self, marca : str, modelo: str, matricula:int, numero_puertas: int, caballos: int, carburante: str):
          super(). __init__(marca, modelo, matricula)
          self.numero_puertas= numero_puertas
          self.caballos = caballos
          self.carburante = carburante
     def informacion(self):
          super().informacion()
          print(f"Número de puertas: {self.numero_puertas}, Caballos de fuerza: {self.caballos}, Carburante: {self.carburante}")

mi_coche = Coche('Ferrari', 'estrella', 444, 3, 150, 'Diesel')
mi_coche.informacion()

class Moto(Automovil):
     tipo: str
     color: str

     def __init__(self, marca: str, modelo: str, matricula: int, tipo: str, color:str):
          super().__init__(marca, modelo, matricula)
          self.tipo = tipo
          self.color = color
     def informacion(self):
          super().informacion()
          print(f'La moto es {self.tipo} y es de color {self.color}')

mi_moto = Moto('KTM', 'Cross', 775, 'Enduro', 'Verde')
mi_moto.informacion()

class Camion(Automovil):
     num_trailer: int
     carga: str

     def __init__(self, marca:str, modelo: str, matricula: int, num_trailer: int, carga:str):
          super().__init__(marca, modelo, matricula)
          self.num_trailer = num_trailer
          self.carga= carga
     def informacion(self):
          super().informacion()
          print(f'El camion tiene {self.num_trailer} trailers y el tipo de carga es de {self.carga}')

mi_camion = Camion('Tesla', 'CXXC', 77777, 5, 'Liquidos peligrosos')
mi_camion.informacion()
mi_camion.arrancar()
mi_camion.acelerar(80)
mi_camion.informacion()
