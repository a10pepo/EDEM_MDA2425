from ejercicio5_parte2 import Automovil


class Automovil:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.velocidad = 0

    def arrancar(self):
        self.encendido = True
        print(f"El automóvil {self.marca} {self.modelo} ha arrancado.")

    def acelerar(self, incremento: float):
        if self.encendido:
            self.velocidad += incremento
            print(f"{self.marca} {self.modelo} ha acelerado. Velocidad actual: {self.velocidad} km/h.")
        else:
            print(f"El automóvil {self.marca} {self.modelo} está apagado. No puede acelerar.")

    def detener(self):
        self.velocidad = 0
        print(f"{self.marca} {self.modelo} se ha detenido.")

    def apagar(self):
        self.encendido = False
        print(f"El automóvil {self.marca} {self.modelo} se ha apagado.")

# Definición de las clases derivadas
class Coche(Automovil):
    def __init__(self, marca: str, modelo: str, n_puertas: int):
        super().__init__(marca, modelo)
        self.n_puertas = n_puertas

    def acelerar(self, incremento):
        if self.encendido:
            if self.n_puertas <= 3:
                super().acelerar(incremento * 1.5)
            else:
                super().acelerar(incremento)
        else:
            print(f"El coche {self.marca} {self.modelo} está apagado. Arráncalo primero.")

class Moto(Automovil):
    def __init__(self, marca: str, modelo: str, cilindros: int):
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
        else:
            print(f"La moto {self.marca} {self.modelo} está apagada. Arráncala primero.")

class Camion(Automovil):
    def __init__(self, marca: str, modelo: str, remolque: bool):
        super().__init__(marca, modelo)
        self.remolque = remolque

    def acelerar(self, incremento):
        if self.encendido:
            if self.remolque:
                super().acelerar(incremento / 2)
            else:
                super().acelerar(incremento)
        else:
            print(f"El camión {self.marca} {self.modelo} está apagado. Arráncalo primero.")

mi_coche = Coche("Ferrari", "F40", 2)
mi_moto = Moto("Yamaha", "MT-07", 100)
mi_camion = Camion("Volvo", "FH", True)

mi_coche.arrancar()
mi_coche.acelerar(100)

mi_moto.arrancar()
mi_moto.acelerar(100)

mi_camion.arrancar()
mi_camion.acelerar(100)
