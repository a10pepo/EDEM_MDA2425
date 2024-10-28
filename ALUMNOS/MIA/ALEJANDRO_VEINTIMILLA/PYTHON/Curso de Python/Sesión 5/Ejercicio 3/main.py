#5. Ejercicios Sesión 5
    #3.Crea clases de automóvil distintas como y que dispongan de distintos atributos, 
        #pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, 
        #salvo que algunos deben tener más potencia que otros:
class Automovil():
    velocidad:float=0
    nombre:str

    def __init__(self,nombre):
        self.nombre=nombre

    def arrancar(self):
        self.velocidad_actual = 10
        print('El automóvil ha arrancado')
    
    def frenar(self, presion: float):
        self.velocidad_actual -= (presion - 10)
        print(f'El automóvil ha frenado. Su velocidad ahora es de {self.velocidad_actual}')
    
    def acelerar(self, presion: float):
        self.velocidad_actual += (presion + 10)
        print(f'El automóvil ha acelerado. Su velocidad ahora es de {self.velocidad_actual}')

    def Parar(self, presion: float):
        self.velocidad_actual = 0
        print(f'El automóvil se ha detenido. Su velocidad ahora es de {self.velocidad_actual}')

        #Coche
class Coche(Automovil):
    n_puertas:int

    def __init__(self,nombre,n_puertas):
        self.n_puertas=n_puertas
        super(Coche, self).__init__(nombre)

        #Moto
class Moto(Automovil):
    marca:bool

    def __init__(self,nombre,marca):
        self.marca=marca
        super(Moto, self).__init__(nombre)

        #Camión
class Camion(Automovil):
    cargado:bool

    def __init__(self,nombre,cargado):
        self.cargado=cargado
        super(Camion, self).__init__(nombre)



# class Coche:
#     velocidad:int=0
#     nombre:str

#     def __init__(self,nombre) -> None:
#         self.nombre=nombre

#     def mostrar_velocidad(self):
#         print(f"El veiculo, {self.nombre}, se desplaza a {self.velocidad}KM/H")

#     def arrancar(self):
#         if self.velocidad > 0:
#             print(f"El veiculo, {self.nombre}, ya esta en marcha" )
#         else:
#             self.velocidad=10

#         #2.Acelerar

#     def acelerar(self):
#         if self.velocidad > 0:
#             self.velocidad=self.velocidad+10
#         else:
#             print(f"El veiculo, {self.nombre}, no ha arrancado. No puede acelerar si estar en marcha" )
            
#         #3.Frenar

#     def frenar(self):
#         if self.velocidad > 0:
#             self.velocidad=self.velocidad-10
#         else:
#             print(f"El veiculo, {self.nombre}, ya esta detenido y, por tanto, no puede frenar más" )

#         #4.Parar

#     def parar(self):
#         if self.velocidad > 0:
#             self.velocidad=0
#         else:
#             print(f"El veiculo, {self.nombre}, ya esta detenido." )

# mi_carro: Coche = Coche("panda")

# mi_carro.mostrar_velocidad()
# mi_carro.frenar()
# mi_carro.arrancar()
# mi_carro.mostrar_velocidad()
# mi_carro.acelerar()
# mi_carro.mostrar_velocidad()
# mi_carro.frenar()
# mi_carro.mostrar_velocidad()
# mi_carro.parar()
# mi_carro.mostrar_velocidad()
