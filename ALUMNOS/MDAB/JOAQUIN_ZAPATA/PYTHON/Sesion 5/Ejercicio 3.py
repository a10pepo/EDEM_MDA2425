class Automovil:
    def __init__(self, potencia):
        self.potencia = potencia
        self.estado = "Parado"
    
    def arrancar(self):
        if self.estado == "Parado":
            self.estado = "Arrancado"
            print(f"El automóvil ha arrancado con {self.potencia} caballos de potencia.")
        else:
            print("El automóvil ya está arrancado.")
    
    def acelerar(self):
        if self.estado == "Arrancado":
            print(f"El automóvil está acelerando con {self.potencia} caballos de potencia.")
        else:
            print("El automóvil debe arrancar primero.")
    
    def frenar(self):
        if self.estado == "Arrancado":
            print("El automóvil está frenando.")
        else:
            print("El automóvil debe arrancar primero.")
    
    def parar(self):
        if self.estado == "Arrancado":
            self.estado = "Parado"
            print("El automóvil ha parado.")
        else:
            print("El automóvil ya está parado.")

class Coche(Automovil):
    def __init__(self, potencia):
        super().__init__(potencia)
    
    def acelerar(self):
        print(f"El coche está acelerando con {self.potencia} caballos de potencia. ¡Vroom!")
    
    def frenar(self):
        print("El coche está frenando con frenos de alto rendimiento.")
        
class Moto(Automovil):
    def __init__(self, potencia):
        super().__init__(potencia)
    
    def acelerar(self):
        print(f"La moto está acelerando con {self.potencia} caballos de potencia. ¡Rrrrr!")
    
    def frenar(self):
        print("La moto está frenando con frenos de disco.")
        
class Camion(Automovil):
    def __init__(self, potencia):
        super().__init__(potencia)
    
    def acelerar(self):
        print(f"El camión está acelerando con {self.potencia} caballos de potencia. ¡Grrrrr!")
    
    def frenar(self):
        print("El camión está frenando con frenos de aire.")

coche = Coche(200)
moto = Moto(100)
camion = Camion(400)

coche.arrancar()
coche.acelerar()
coche.frenar()
coche.parar()

moto.arrancar()
moto.acelerar()
moto.frenar()
moto.parar()

camion.arrancar()
camion.acelerar()
camion.frenar()
camion.parar()
