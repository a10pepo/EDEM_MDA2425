from Ejercicio2 import Automovil

class Coche(Automovil):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas 

class Moto(Automovil):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada 

class Camion(Automovil):
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self.capacidad_carga = capacidad_carga

    def acelerar(self, incremento):
        if self.arrancado:
            super().acelerar(incremento * 2) 
        else:
            print(f"No puedes acelerar, el {self.marca} {self.modelo} está apagado.")
