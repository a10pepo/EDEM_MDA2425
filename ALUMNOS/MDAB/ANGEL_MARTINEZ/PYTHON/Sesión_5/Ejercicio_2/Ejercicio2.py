class Automovil:
    tipo: str 
    velocidad: float = 0
 
    def __init__(self, tipo):
        self.tipo = tipo
        self.arrancado = False 
        self.velocidad = 0 

    def arrancar(self):
        if not self.arrancado: 
            self.arrancado = True
            print(f'{self.tipo} ha arrancado.')
        else:
            print(f'{self.tipo} ya está arrancado.')
        
    def acelerar(self, incremento:float):
        if self.arrancado: 
            self.velocidad += incremento
            print(f'{self.tipo} ha acelerado a {self.velocidad} km/h.')
        else:
            print(f'No puedes acelerar, {self.tipo} no está en arrancado.')

    def frenar(self, decremento):
        if self.arrancado: 
            self.velocidad -= decremento
            if self.velocidad < 0:
                self.velocidad = 0 
            print(f'{self.tipo} ha reducido su velicidad a {self.velocidad} km/h. ')
        else:
            print(f'No puedes frenar, {self.tipo} no está en arrancado')

    def parar(self):
        if self.arrancado: 
            self.velocidad = 0
            self.arrancado = False
            print(f'{self.tipo} se ha detenido')
        else:
            print(f'{self.tipo} ya está detenido')

    def __repr__(self): 
        return f'Tipo: {self.tipo} Arrancado: {self.arrancado} Velocidad: {self.velocidad}'
    
    def mostrar_vehiculo(self):
        print(f'Tipo: {self.tipo} | Arrancado: {self.arrancado} | Velocidad: {self.velocidad}')



auto = Automovil("Moto")
