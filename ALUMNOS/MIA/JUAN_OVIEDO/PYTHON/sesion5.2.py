class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.velocidad = 0

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            print(f'{self.marca} {self.modelo} ha arrancado')
        else:
            print(f'{self.marca} {self.modelo} ya está encendido')

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f'{self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h.')
        else:
            print(f'No puedes acelerar. {self.marca} {self.modelo} está apagado.')

    def frenar(self, decremento):
        if self.encendido and self.velocidad > 0:
            self.velocidad = max(0, self.velocidad - decremento)
            print(f'{self.marca} {self.modelo} ha frenado a velocidad {self.velocidad} km/h')
        elif self.velocidad == 0:
            print(f'{self.marca} {self.modelo} ya está detenido')
        else:
            print(f'No puedes frenar. {self.marca} {self.modelo} está apagado.')

    def parar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            print(f'{self.marca} {self.modelo} se ha detenido y apagado')
        else:
            print(f'{self.marca} {self.modelo} ya está apagado')

mi_auto = Automovil("Mini", "Cooper")
mi_auto.arrancar()
mi_auto.acelerar(150)
mi_auto.frenar(20)