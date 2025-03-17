# 3. Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:
# 	1. Coche
# 	2. Moto
# 	3. Camión

class Automovil:
    tipo: str #Tipo del vehiculo
    velocidad: float = 0
 
    def __init__(self, tipo, potencia, puertas):
        self.tipo = tipo
        self.potencia = potencia
        self.puertas = puertas
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
            self.velocidad += incremento * self.potencia
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


class Coche(Automovil):
    def __init__(self):
        super().__init__("Coche", potencia=1.2, puertas=4)  # Coche con potencia normal y 4 puertas


class Moto(Automovil):
    def __init__(self):
        super().__init__("Moto", potencia=1.5, puertas=0)  # Moto con más potencia y 0 puertas

class Camion(Automovil):
    def __init__(self):
        super().__init__("Camión", potencia=0.8, puertas=2)  # Camión con menos potencia y 2 puertas


#EJEMPLO

mi_coche = Coche()
print(f"{mi_coche.tipo} tiene {mi_coche.puertas} puertas.")
mi_coche.arrancar()
mi_coche.acelerar(30)
mi_coche.frenar(10)
mi_coche.parar()
print("")

mi_moto = Moto()
print(f"{mi_moto.tipo} tiene {mi_moto.puertas} puertas.")
mi_moto.arrancar()
mi_moto.acelerar(30)
mi_moto.frenar(10)
mi_moto.parar()
print("")

mi_camion = Camion()
print(f"{mi_camion.tipo} tiene {mi_camion.puertas} puertas.")
mi_camion.arrancar()
mi_camion.acelerar(30)
mi_camion.frenar(10)
mi_camion.parar()
print("")

#Cada uno llega a una velocidad dependiendo de la potencia de cada vehículo