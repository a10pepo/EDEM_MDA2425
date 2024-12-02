class Automovil:
    def __init__(self, marca, modelo, potencia):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia  # Representa la potencia del motor (en caballos de fuerza, por ejemplo)
        self.velocidad_actual = 0
        self.arrancado = False

    def arrancar(self):
        if not self.arrancado:
            self.arrancado = True
            print(f"{self.marca} {self.modelo} ha arrancado.")
        else:
            print(f"{self.marca} {self.modelo} ya está arrancado.")

    def acelerar(self):
        if self.arrancado:
            self.velocidad_actual += self.potencia * 0.1  # Aceleración basada en la potencia
            print(f"{self.marca} {self.modelo} está acelerando. Velocidad actual: {self.velocidad_actual:.2f} km/h.")
        else:
            print(f"No puedes acelerar, {self.marca} {self.modelo} no está arrancado.")

    def frenar(self):
        if self.arrancado and self.velocidad_actual > 0:
            self.velocidad_actual -= self.potencia * 0.05  # La potencia también afecta la frenada
            if self.velocidad_actual < 0:
                self.velocidad_actual = 0
            print(f"{self.marca} {self.modelo} está frenando. Velocidad actual: {self.velocidad_actual:.2f} km/h.")
        elif self.velocidad_actual == 0:
            print(f"{self.marca} {self.modelo} ya está detenido.")
        else:
            print(f"No puedes frenar, {self.marca} {self.modelo} no está arrancado.")

    def parar(self):
        if self.arrancado:
            self.arrancado = False
            self.velocidad_actual = 0
            print(f"{self.marca} {self.modelo} se ha detenido y apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

# Clase Coche
class Coche(Automovil):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, potencia=150)  # Un coche tiene una potencia media de 150 hp

# Clase Moto
class Moto(Automovil):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, potencia=100)  # Una moto tiene menos potencia, digamos 100 hp

    def acelerar(self):
        if self.arrancado:
            self.velocidad_actual += self.potencia * 0.2  # Las motos aceleran más rápido
            print(f"{self.marca} {self.modelo} está acelerando rápidamente. Velocidad actual: {self.velocidad_actual:.2f} km/h.")
        else:
            print(f"No puedes acelerar, {self.marca} {self.modelo} no está arrancado.")

# Clase Camión
class Camion(Automovil):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, potencia=300)  # Un camión tiene mucha más potencia, digamos 300 hp

    def frenar(self):
        if self.arrancado and self.velocidad_actual > 0:
            self.velocidad_actual -= self.potencia * 0.02  # Los camiones frenan más lentamente
            if self.velocidad_actual < 0:
                self.velocidad_actual = 0
            print(f"{self.marca} {self.modelo} está frenando lentamente. Velocidad actual: {self.velocidad_actual:.2f} km/h.")
        elif self.velocidad_actual == 0:
            print(f"{self.marca} {self.modelo} ya está detenido.")
        else:
            print(f"No puedes frenar, {self.marca} {self.modelo} no está arrancado.")

# Pruebas
coche = Coche("Toyota", "Corolla")
moto = Moto("Yamaha", "R1")
camion = Camion("Mercedes", "Actros")

print("\n--- PRUEBA CON EL COCHE ---")
coche.arrancar()
coche.acelerar()
coche.frenar()
coche.parar()

print("\n--- PRUEBA CON LA MOTO ---")
moto.arrancar()
moto.acelerar()
moto.frenar()
moto.parar()

print("\n--- PRUEBA CON EL CAMIÓN ---")
camion.arrancar()
camion.acelerar()
camion.frenar()
camion.parar()
