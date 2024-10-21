class Automovil:
    def __init__(self, velocidad, ruedas, marca, peso, año, potencia):
        self.velocidad = velocidad
        self.ruedas = ruedas
        self.marca = marca
        self.peso = peso
        self.año = año
        self.potencia = potencia

    def arrancar(self, velocidad):
        self.velocidad = velocidad

    def acelerar(self, velocidad):
        self.velocidad += velocidad
    
    def frenar(self, velocidad):
        self.velocidad -= velocidad
    
    def parar(self, velocidad):
        self.velocidad = 0
