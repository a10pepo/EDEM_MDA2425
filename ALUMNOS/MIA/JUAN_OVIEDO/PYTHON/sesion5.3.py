class Automovil:
    def __init__(self, marca, modelo, potencia):
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




class Coche(Automovil):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, potencia=2)  

class Moto(Automovil):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, potencia=3)  

class Camion(Automovil):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, potencia=7)







mi_coche = Coche("Mini", "Cooper")
mi_moto = Moto("Yamaha", "R1")
mi_camion = Camion("Scania", "1500")


mi_coche.arrancar()
mi_coche.acelerar(130)
mi_coche.frenar(10)
mi_coche.parar()

mi_moto.arrancar()
mi_moto.acelerar(240)
mi_moto.frenar(0)
mi_moto.parar()

mi_camion.arrancar()
mi_camion.acelerar(90)
mi_camion.frenar(10)
mi_camion.parar()



