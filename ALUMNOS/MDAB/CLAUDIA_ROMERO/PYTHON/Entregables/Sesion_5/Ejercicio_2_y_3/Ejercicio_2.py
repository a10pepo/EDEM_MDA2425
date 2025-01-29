# Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
# Arrancar
# Acelerar
# Frenar
# Parar

class Automovil:
    marca: str
    modelo: str
    velocidad: float
    estado: bool

    def __init__(self, marca: str, modelo: str, velocidad: float = 0, estado: bool = False):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.estado = estado

# Arrancar
    def arrancar(self):
        if not self.estado:
            self.estado = True
            print(f"El coche {self.marca} {self.modelo} se está arrancando.")
        else:
            print(f"El coche {self.marca} {self.modelo} ya está arrancado.")

# Acelerar
    def acelerar(self):
        if self.estado:
            self.velocidad += 10  
            print(f"El coche {self.marca} {self.modelo} está acelerando a {self.velocidad} km/h.")
        else:
            print(f"El coche {self.marca} {self.modelo} no está arrancado.")

# Frenar
    def frenar(self):
        if self.estado: 
            self.velocidad = 0
            print(f"El coche {self.marca} {self.modelo} está frenando a {self.velocidad} km/h.")
        else:
            print(f"El coche {self.marca} {self.modelo} no está arrancado.")

# Parar
    def parar(self):
        if self.estado:
            self.estado = False
            self.velocidad = 0 
            print(f"El coche {self.marca} {self.modelo} se ha parado.")
        else:
            print(f"El coche {self.marca} {self.modelo} ya estaba parado.")


coche = Automovil("Toyota", "Corolla")
coche.arrancar()
coche.acelerar()
coche.frenar()
coche.parar()
