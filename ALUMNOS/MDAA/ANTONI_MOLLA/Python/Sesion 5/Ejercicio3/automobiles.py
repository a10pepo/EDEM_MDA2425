class Automovil:
    def __init__(self, marca, modelo, potencia):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia  
        self.velocidad = 0  # Velocidad inicial

    def arrancar(self):
        print(f"{self.marca} {self.modelo} ha arrancado.")

    def acelerar(self):
        self.velocidad += self.potencia * 0.1  # La aceleración depende de la potencia
        print(f"{self.marca} {self.modelo} ha acelerado. Velocidad actual: {self.velocidad:.2f} km/h.")

    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= self.potencia * 0.05  # Frenado depende de la potencia
            self.velocidad = max(self.velocidad, 0)  # Asegura que la velocidad no sea negativa
            print(f"{self.marca} {self.modelo} ha frenado. Velocidad actual: {self.velocidad:.2f} km/h.")
        else:
            print(f"{self.marca} {self.modelo} ya está detenido.")

    def parar(self):
        self.velocidad = 0
        print(f"{self.marca} {self.modelo} se ha detenido por completo.")

# Clase Coche
class Coche(Automovil):
    def __init__(self, marca, modelo, potencia):
        super().__init__(marca, modelo, potencia)

# Clase Moto
class Moto(Automovil):
    def __init__(self, marca, modelo, potencia):
        super().__init__(marca, modelo, potencia)

    def acelerar(self):
        self.velocidad += self.potencia * 0.15  # Las motos suelen ser más ágiles
        print(f"{self.marca} {self.modelo} (Moto) ha acelerado. Velocidad actual: {self.velocidad:.2f} km/h.")

# Clase Camión
class Camion(Automovil):
    def __init__(self, marca, modelo, potencia, capacidad_carga):
        super().__init__(marca, modelo, potencia)
        self.capacidad_carga = capacidad_carga  # Capacidad de carga en toneladas

    def acelerar(self):
        self.velocidad += self.potencia * 0.05  # Los camiones aceleran más lento
        print(f"{self.marca} {self.modelo} (Camión) ha acelerado. Velocidad actual: {self.velocidad:.2f} km/h.")

# Ejemplo de uso
if __name__ == "__main__":
    coche = Coche("Toyota", "Corolla", 120)
    moto = Moto("Yamaha", "YZF-R3", 42)
    camion = Camion("Volvo", "FH16", 540, 25)

    print("\n-- Coche --")
    coche.arrancar()
    coche.acelerar()
    coche.frenar()
    coche.parar()

    print("\n-- Moto --")
    moto.arrancar()
    moto.acelerar()
    moto.frenar()
    moto.parar()

    print("\n-- Camión --")
    camion.arrancar()
    camion.acelerar()
    camion.frenar()
    camion.parar()
