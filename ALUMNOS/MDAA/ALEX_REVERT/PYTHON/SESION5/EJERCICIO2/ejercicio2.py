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
            print(f"El automóvil {self.marca} {self.modelo} ha arrancado.")
        else:
            print(f"El automóvil {self.marca} {self.modelo} ya está encendido.")

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f"El automóvil {self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h.")
        else:
            print(f"El automóvil {self.marca} {self.modelo} está apagado. No se puede acelerar.")

    def frenar(self, decremento):
        if self.encendido and self.velocidad > 0:
            self.velocidad -= decremento
            if self.velocidad < 0:
                self.velocidad = 0
            print(f"El automóvil {self.marca} {self.modelo} ha frenado a {self.velocidad} km/h.")
        else:
            print(f"El automóvil {self.marca} {self.modelo} está apagado o ya está detenido.")

    def parar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            print(f"El automóvil {self.marca} {self.modelo} se ha detenido.")
        else:
            print(f"El automóvil {self.marca} {self.modelo} ya está apagado.")


auto = Automovil("Toyota", "Corolla", 2020)
auto.arrancar()
auto.acelerar(50)
auto.frenar(20)
auto.parar()