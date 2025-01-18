class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.arrancado = False

    def arrancar(self):
        if not self.arrancado:
            self.arrancado = True
            print(f"El automóvil {self.marca} {self.modelo} ha arrancado.")
        else:
            print(f"El automóvil {self.marca} {self.modelo} ya está arrancado.")

    def acelerar(self, incremento):
        if self.arrancado:
            self.velocidad += incremento
            print(f"El automóvil {self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h.")
        else:
            print(f"No puedes acelerar, el automóvil {self.marca} {self.modelo} está apagado.")

    def frenar(self, decremento):
        if self.arrancado:
            self.velocidad -= decremento
            if self.velocidad < 0:
                self.velocidad = 0
            print(f"El automóvil {self.marca} {self.modelo} ha frenado a {self.velocidad} km/h.")
        else:
            print(f"No puedes frenar, el automóvil {self.marca} {self.modelo} está apagado.")

    def parar(self):
        if self.arrancado:
            self.arrancado = False
            self.velocidad = 0
            print(f"El automóvil {self.marca} {self.modelo} se ha detenido.")
        else:
            print(f"El automóvil {self.marca} {self.modelo} ya está apagado.")

# Ejemplo de uso
mi_coche = Automovil("Maseratti", "Gran Turismo")
mi_coche.arrancar()
mi_coche.acelerar(200)
mi_coche.frenar(90)
mi_coche.parar()
