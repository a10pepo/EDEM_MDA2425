from ..Ejercicio_2.Automovil import Automovil

class Coche(Automovil):
    def __init__(self, marca: str, modelo: str) -> None:
        super().__init__(marca, modelo)
        self.potencia = 120
        self.ruedas = 4

class Moto(Automovil):
    def __init__(self, marca: str, modelo: str) -> None:
        super().__init__(marca, modelo)
        self.potencia = 80
        self.ruedas = 2

class Camion(Automovil):        
    def __init__(self, marca: str, modelo: str) -> None:
        super().__init__(marca, modelo)
        self.potencia = 180
        self.ruedas = 6