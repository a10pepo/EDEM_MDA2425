from session_5_2 import Automovil

class Coche(Automovil):
    def __init__(self, marca, modelo, distintivo_ambiental):
        super().__init__(marca, modelo)
        self.distintivo_ambiental = distintivo_ambiental   # Etiqueta polución: B, C, ECO, 0
        self.potencia = 20

    def acelerar(self, incremento):
        super().acelerar(incremento * self.potencia / 10)

class Moto(Automovil):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo                                   # Tipo de moto: Sport, Naked, Off-Road, Scooter...
        self.potencia = 30

    def acelerar(self, incremento):
        super().acelerar(incremento * self.potencia / 10)

class Camion(Automovil):
    def __init__(self, marca, modelo, capacidad):
        super().__init__(marca, modelo)
        self.capacidad = capacidad                         # Capacidad de carga
        self.potencia = 10

    def acelerar(self, incremento):
        super().acelerar(incremento * self.potencia / 10) 


coche = Coche("Volkswagen", "Polo", "C")
coche.arrancar()
coche.acelerar(50)
coche.frenar(-10)
coche.parar()

moto = Moto("Yamaha", "R1", "Sport")
moto.arrancar()
moto.acelerar(50)
moto.frenar(-20)
moto.parar()

camion = Camion("Mercedes", "Actros", 15000)
camion.arrancar()
camion.acelerar(50)
camion.frenar(-10)
camion.parar()
