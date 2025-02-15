class Automovil():

    def __init__(self, velocidad_maxima):  #estructura importante && __int__: es la funcion constructura que nos permite contruir el objeto coche 
        self.velocidad_maxima= velocidad_maxima
        self.velocidad_actual=0
        self.encendido=False

    def arrancar(self):
        if not self.encendido:
            self.encendido=True
            print(f'El automovil se ha encendido')
        else:
            print('el automovil ya estaba arrancado')
    
    def acelerar(self, incremento):
        if self.encendido:
            nueva_velo= self.velocidad_actual + incremento
            if nueva_velo>self.velocidad_maxima:
                print(f'el automovil va a su velocidad máxima {self.velocidad_maxima}')
            else:
                self.velocidad_actual=nueva_velo
                print(f'el automovil va a una velocidad de {self.velocidad_actual}')
        else: 
            print('el automovil esta apagado, enciendelo primero anda')
    
    def frenar(self, decremento):
        if self.encendido:
            nueva_velo=self.velocidad_actual - decremento
            if nueva_velo<0:
                self.velocidad_actual=0
            else:
                self.velocidad_actual=nueva_velo
            print(f'la velocidad actual del automovil es de {self.velocidad_actual} km/h')
        else:
            print('el automovil esta apagado melon como vas a frenar... Arrancalo anda.')
    
    def parar(self):
        if self.encendido:
            self.velocidad_actual=0
            self.encendido=False
            print('el automovil se ha detenido y parado el motor')
        else:
            print('el automovil ya estaba  detenido y apagado')

mi_auto=Automovil(200)

