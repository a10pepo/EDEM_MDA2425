class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.velocidad = 0

    def arrancar(self):
        self.encendido = True
        print(f"{self.marca} {self.modelo} está arrancado.")

    def acelerar(self, incremento):
        if self.encendido:
            if incremento > 0:
                self.velocidad = self.velocidad + incremento
                print(f"{self.marca} {self.modelo} ha acelerado, su nueva velocidad es {self.velocidad} km/h.")
            else:
                print("El incremento es negativo, por ello el coche no ha acelerado.")
        else:
            print(f"{self.marca} {self.modelo} no está arrancado.")

    def frenar(self, decremento):
        if self.encendido:
            if (decremento < 0) & (self.velocidad > 0):
                self.velocidad = max(0,self.velocidad + decremento)
                print(f"{self.marca} {self.modelo} ha frenado, su nueva velocidad es {self.velocidad} km/h.")
            else:
                print("Para frenar el decremento debe ser negativo y la velocidad mayor que 0.")
        else:
            print(f"{self.marca} {self.modelo} no está arrancado.")

    def parar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            print(f"{self.marca} {self.modelo} está apagado.")
        else:
            print(f"{self.marca} {self.modelo} no está arrancado.")
