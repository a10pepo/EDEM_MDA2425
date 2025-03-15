class Automovil:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
        self.velocidad = 0

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} ha arrancado.")
        else:
            print(f"El {self.marca} {self.modelo} ya está encendido.")

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f"El {self.marca} {self.modelo} está acelerando a {self.velocidad} km/h.")
        else:
            print("No puedes acelerar un automóvil que está apagado.")

    def frenar(self, decremento):
        if self.encendido:
            self.velocidad -= decremento
            if self.velocidad < 0:
                self.velocidad = 0
            print(f"El {self.marca} {self.modelo} ha frenado a {self.velocidad} km/h.")
        else:
            print("No puedes frenar un automóvil que está apagado.")

    def parar(self):
        if self.encendido:
            self.velocidad = 0
            self.encendido = False
            print(f"El {self.marca} {self.modelo} se ha detenido y apagado.")
        else:
            print(f"El {self.marca} {self.modelo} ya está apagado.")

auto = Automovil("Toyota", "Corolla", "Rojo")
auto.arrancar()
auto.acelerar(50)
auto.frenar(20)
auto.parar()
