#Crea una clase Automóvil que disponga de los atributos necesarios y métodos para: Arrancar, Acelerar, Frenar y Parar.

class Automovil:
    def __init__(self, marca, modelo, color, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad
        self.arrancado = False

    def arrancar(self):
        if not self.arrancado:
            self.arrancado = True
            print(f"El {self.marca} {self.modelo} ha arrancado.")
        else:
            print(f"El {self.marca} {self.modelo} ya está arrancado.")

    def acelerar(self):
        if self.arrancado:
            self.velocidad += 10
            print(f"El {self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h.")
        else:
            print(f"El {self.marca} {self.modelo} no puede acelerar si no está arrancado.")

    def frenar(self):
        if self.arrancado:
            self.velocidad = max(0, self.velocidad - 10)
            print(f"El {self.marca} {self.modelo} ha frenado a {self.velocidad} km/h.")
        else:
            print(f"El {self.marca} {self.modelo} no puede frenar si no está arrancado.")

    def parar(self):
        if self.arrancado:
            self.arrancado = False
            self.velocidad = 0  # Reinicia la velocidad a 0 al parar
            print(f"El {self.marca} {self.modelo} ha parado.")
        else:
            print(f"El {self.marca} {self.modelo} no puede parar si no está arrancado.")


    

    
