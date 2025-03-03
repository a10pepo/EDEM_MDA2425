#Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:Coche,Moto,Camión
from ..Ejercicio_2.archivo11 import Automovil

def acelerar(self):
    self.velocidad += 10
    print(f"El {self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h.")   

class Coche(Automovil):
    def __init__(self, marca, modelo, color, velocidad=0, puertas=4):
        super().__init__(marca, modelo, color, velocidad)
        self.puertas = puertas

    def acelerar(self):
        self.velocidad += 20
        print(f"El {self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h.")

class Moto(Automovil):
    def __init__(self, marca, modelo, color, velocidad=0, cilindrada=500):
        super().__init__(marca, modelo, color, velocidad)
        self.cilindrada = cilindrada

    def acelerar(self):
        self.velocidad += 30
        print(f"La {self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h.")   

class Camion(Automovil):
    def __init__(self, marca, modelo, color, velocidad=0, carga=1000):
        super().__init__(marca, modelo, color, velocidad)
        self.carga = carga

    def acelerar(self): 
        self.velocidad += 40
        print(f"El {self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h.")   


