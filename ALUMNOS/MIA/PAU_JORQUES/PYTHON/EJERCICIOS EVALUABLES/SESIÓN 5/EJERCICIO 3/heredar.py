from EJERCICIO2.automovil import Automovil

class Coche(Automovil):
    def __init__(self, velocidad, ruedas, marca, peso, año, potencia):
        super().__init__(velocidad, ruedas, marca, peso, año, potencia) 


class Moto(Automovil):
    def __init__(self, velocidad, ruedas, marca, peso, año, potencia):
        super().__init__(velocidad, ruedas, marca, peso, año, potencia) 


class Camion(Automovil):
    def __init__(self, velocidad, ruedas, marca, peso, año, potencia):
        super().__init__(velocidad, ruedas, marca, peso, año, potencia) 


