
# ## Ejercicio 2
# 2. Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
# 	1. Arrancar
# 	2. Acelerar
# 	3. Frenar
# 	4. Parar

class Automovil:
    tipo: str #Tipo del vehiculo
    velocidad: float = 0
 
    def __init__(self, tipo):
        self.tipo = tipo
        self.arrancado = False #Estado del vehículo
        self.velocidad = 0 #Velocidad actual del vehículo

    def arrancar(self):
        if not self.arrancado: # Si no es True (si no está arrancado)
            self.arrancado = True
            print(f'{self.tipo} ha arrancado.')
        else:
            print(f'{self.tipo} ya está arrancado.')
        
    def acelerar(self, incremento:float):
        if self.arrancado: #Si es true (si antes se ha encendido)
            self.velocidad += incremento
            print(f'{self.tipo} ha acelerado a {self.velocidad} km/h.')
        else:
            print(f'No puedes acelerar, {self.tipo} no está en arrancado.')

    def frenar(self, decremento):
        if self.arrancado: #Si es true (si antes se ha encendido)
            self.velocidad -= decremento
            if self.velocidad < 0:
                self.velocidad = 0 # No permitir velocidad negativa
            print(f'{self.tipo} ha reducido su velicidad a {self.velocidad} km/h. ')
        else:
            print(f'No puedes frenar, {self.tipo} no está en arrancado')

    def parar(self):
        if self.arrancado: #Si est´ta encendido
            self.velocidad = 0
            self.arrancado = False
            print(f'{self.tipo} se ha detenido')
        else:
            print(f'{self.tipo} ya está detenido')

    def __repr__(self): #Repr es per a representar de una manera determinada el objecte creat
        return f'Tipo: {self.tipo} Arrancado: {self.arrancado} Velocidad: {self.velocidad}'
    
    def mostrar_vehiculo(self):
        print(f'Tipo: {self.tipo} | Arrancado: {self.arrancado} | Velocidad: {self.velocidad}')



auto = Automovil("Moto")

auto.arrancar()
auto.acelerar(50)
auto.frenar(20)
auto.mostrar_vehiculo()
auto.parar()
auto.mostrar_vehiculo()
