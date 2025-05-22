# Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de 
# Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que 
#otros:
# Coche
# Moto
# Camión

from Ejercicio_2 import Automovil

class Coche(Automovil):
    def __init__(self, marca:str, modelo:str, velocidad:float, estado:bool, caballos:int):
        super().__init__(marca, modelo, velocidad, estado)
        self.caballos = caballos

class Moto(Automovil):
    def __init__(self, marca:str, modelo:str, velocidad:float, estado:bool, cilindradas:int):
        super().__init__(marca, modelo, velocidad, estado)
        self.cilindradas = cilindradas

class Camion(Automovil):
    def __init__(self, marca: str, modelo: str, velocidad: float, estado: bool, carga:float):
        super().__init__(marca, modelo, velocidad, estado)
        self.carga = carga
