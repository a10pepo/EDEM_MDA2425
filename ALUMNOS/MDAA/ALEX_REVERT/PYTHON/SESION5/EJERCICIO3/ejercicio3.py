class Automovil:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False
        self.velocidad = 0

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.articulo()} {self.marca} {self.modelo} ha arrancado.")
        else:
            print(f"{self.articulo()} {self.marca} {self.modelo} ya está encendido.")

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f"{self.articulo()} {self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h.")
        else:
            print(f"{self.articulo()} {self.marca} {self.modelo} está apagado. No se puede acelerar.")

    def frenar(self, decremento):
        if self.encendido and self.velocidad > 0:
            self.velocidad -= decremento
            if self.velocidad < 0:
                self.velocidad = 0
            print(f"{self.articulo()} {self.marca} {self.modelo} ha frenado a {self.velocidad} km/h.")
        else:
            print(f"{self.articulo()} {self.marca} {self.modelo} está apagado o ya está detenido.")

    def parar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            print(f"{self.articulo()} {self.marca} {self.modelo} se ha detenido.")
        else:
            print(f"{self.articulo()} {self.marca} {self.modelo} ya está apagado.")

    def articulo(self):
        return "El automóvil"

class Coche(Automovil):
    def acelerar(self, incremento=10):
        super().acelerar(incremento)

    def frenar(self, decremento=10):
        super().frenar(decremento)

    def articulo(self):
        return "El coche"

class Moto(Automovil):
    def acelerar(self, incremento=15):
        super().acelerar(incremento)

    def frenar(self, decremento=15):
        super().frenar(decremento)

    def articulo(self):
        return "La moto"

class Camion(Automovil):
    def acelerar(self, incremento=5):
        super().acelerar(incremento)

    def frenar(self, decremento=5):
        super().frenar(decremento)

    def articulo(self):
        return "El camión"

# Ejemplo de uso
coche = Coche("Toyota", "Corolla", 2020)
moto = Moto("Yamaha", "MT-07", 2021)
camion = Camion("Volvo", "FH16", 2019)

coche.arrancar()
coche.acelerar()
coche.frenar()
coche.parar()

moto.arrancar()
moto.acelerar()
moto.frenar()
moto.parar()

camion.arrancar()
camion.acelerar()
camion.frenar()
camion.parar()