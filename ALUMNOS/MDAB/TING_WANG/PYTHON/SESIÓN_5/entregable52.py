# 2

class Automovil:
    marca:str
    modelo:str
    color:str
    velocidad:float = 0

    def __init__(self, marca:str, modelo:str, color:str, velocidad:float):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad
    
    def arrancar(self):
        self.velocidad = 10
        print(f'El automóvil {self.marca} {self.modelo} {self.color} ha arrancado')
    
    def acelerar(self, presion:float):
        self.velocicdad += (presion + 10)
        print(f'El automóvil {self.marca} {self.modelo} {self.color} ha acelerado. Su velocidad ahora es {self.velocidad}km/h')
    
    def frenar(self, presion:float):
        self.velocidad -= (presion - 10)
        print(f'El automóvil {self.marca} {self.modelo} {self.color} ha frenado. Su velocidad ahora es {self.velocidad}km/h')
    
    def parar(self):
        self.velocidad = 0
        print(f'El automóvil {self.marca} {self.modelo} {self.color} está parado')

