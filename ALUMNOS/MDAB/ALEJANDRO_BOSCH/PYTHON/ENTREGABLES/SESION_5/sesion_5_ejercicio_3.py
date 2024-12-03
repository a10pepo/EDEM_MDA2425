from sesion_5_ejercicio_2 import Automovil


class Coche(Automovil):
    def __init__(self, marca:str, modelo:str, n_puertas:int):
        super().__init__(marca, modelo)
        self.n_puertas = n_puertas

    def acelerar(self, incremento):
        if self.encendido:
            if self.n_puertas <= 3:
                super().acelerar(incremento * 1.5)
            else: 
                super().acelerar(incremento)
        else:
            print(F"El coche {self.marca} {self.modelo} esta apagado, arrancalo primero ")

class Moto(Automovil):
    def __init__(self, marca:str, modelo:str, cilindros:int):
        super().__init__(marca, modelo)
        self.cilindros = cilindros

    def acelerar(self, incremento):
        if self.encendido:
            if self.cilindros <= 49:
                super().acelerar(incremento * 1.1)
            elif self.cilindros <= 100:
                super().acelerar(incremento * 1.3)
            elif self.cilindros <= 125:
                super().acelerar(incremento * 1.5)
        


class Camion(Automovil):
    def __init__(self, marca:str, modelo:str, remolque:bool):
        super().__init__(marca, modelo)
        self.remolque = True

    def acelerar(self, incremento):
        if self.encendido:
            if self.remolque:
                super().acelerar(incremento / 2)
            else:
                super().acelerar(incremento)
        else:
            print(f"El camion {self.marca} {self.modelo} está apagado")



mi_coche = Coche("Ferrari", "LaFerrari", 2)
mi_moto = Moto("Yamaha", "MT-07", 100)
mi_camion = Camion("Volvo", "FH", True)

mi_coche.arrancar()
mi_coche.acelerar(100)

mi_moto.arrancar()
mi_moto.acelerar(100)

mi_camion.arrancar()
mi_camion.acelerar(100)