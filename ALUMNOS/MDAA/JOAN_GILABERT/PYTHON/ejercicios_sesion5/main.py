'''
Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
Arrancar
Acelerar
Frenar
Parar
Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:
Coche
Moto
Camión
'''

class Automovil:
    def __init__(self, marca, modelo, potencia, encendido=False):
        self.marca=marca
        self.modelo=modelo
        self.potencia=potencia
        self.encendido=encendido
        self.velocidad=0


    def Arrancar(self):
        if self.encendido:
            return "El coche ya está en marcha"
        else:
            self.encendido=True
            return "El coche ha arrancado"
        
    def Acelerar(self):
        if self.encendido:
            self.velocidad+=self.potencia*0.2
            return f"El coche ha acelerado a {self.velocidad} km/h"
        else:
            return "El coche no está en marcha"
        
    def Frenar(self):
        if self.encendido:
            self.velocidad-=self.velocidad*0.2
            return f"El coche ha frenado. Ahora va a {self.velocidad} km/h"
        else:
            return "El coche no está en marcha"
        
    def Parar(self):
        if self.encendido:
            self.encendido=False
            return "El coche se ha parado"
        else:
            return "El coche ya estaba parado"
        

class Coche(Automovil):
    def __init__(self, marca, modelo, potencia=120, encendido=False):
        super().__init__(marca, modelo, potencia, encendido)

class Moto(Automovil):
    def __init__(self, marca, modelo, potencia=80, encendido=False):
        super().__init__(marca, modelo, potencia, encendido)

class Camion(Automovil):
    def __init__(self, marca, modelo, potencia=300, encendido=False):
        super().__init__(marca, modelo, potencia, encendido)
        

Coche1=Coche("Seat", "Ibiza")
print(Coche1.Arrancar())
print(Coche1.Acelerar())
print(Coche1.Acelerar())
print(Coche1.Acelerar())
print(Coche1.Frenar())
print(Coche1.Parar())
print("\n")

Moto1=Moto("Yamaha", "FZ6")
print(Moto1.Arrancar())
print(Moto1.Acelerar())
print(Moto1.Acelerar())
print(Moto1.Acelerar())
print(Moto1.Frenar())
print(Moto1.Parar())
print("\n")

Camion1=Camion("Mercedes", "Actros")
print(Camion1.Arrancar())
print(Camion1.Acelerar())
print(Camion1.Acelerar())
print(Camion1.Acelerar())
print(Camion1.Frenar())
print(Camion1.Parar())
print("\n")