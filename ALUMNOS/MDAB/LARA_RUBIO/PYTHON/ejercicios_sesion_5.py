# 1. Lee un archivo CSV con Pandas y realizar las siguientes operaciones. (Pendiente de establecer)

# 2. Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:

# 2.1 Arrancar
# 2.2 Acelerar
# 2.3 Frenar
# 2.4 Parar

class Automovil:
    def __init__(self, marca, modelo):
        
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False  
        self.velocidad = 0  # Velocidad inicial 

    def arrancar(self):
        if not self.arrancado:
            self.arrancado = True
            print(f"El {self.marca} {self.modelo} ha arrancado.")
        else:
            print(f"El {self.marca} {self.modelo} ya había arrancado.")

    def acelerar(self, incremento):
        if self.arrancado:
            self.velocidad += incremento
            print(f"El {self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h.")
        else:
            print(f"Primero debes arrancar el {self.marca} {self.modelo}.")

    def frenar(self, decremento):
        if self.arrancado:
            self.velocidad -= decremento
            if self.velocidad < 0:
                self.velocidad = 0
            print(f"El {self.marca} {self.modelo} ha frenado a {self.velocidad} km/h.")
        else:
            print(f"El {self.marca} {self.modelo} no está en marcha.")

    def parar(self):
        if self.arrancado:
            self.arrancado = False
            self.velocidad = 0
            print(f"El {self.marca} {self.modelo} se ha detenido.")
        else:
            print(f"El {self.marca} {self.modelo} ya se había detenido.")

# Ejemplo de uso
if __name__ == "__main__":
    mi_auto = Automovil("Volkswagen", "Polo")
    mi_auto.arrancar()
    mi_auto.acelerar(30)
    mi_auto.frenar(10)
    mi_auto.parar()

# 3. Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:

# 3.1 Coche
# 3.2 Moto
# 3.3 Camión

class Coche(Automovil):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas 

    def acelerar(self, incremento):
        if self.arrancado:
            print(f"El coche {self.marca} {self.modelo} acelera rápidamente.")
            super().acelerar(incremento)
        else:
            print(f"No puedes acelerar, el coche {self.marca} {self.modelo} está apagado.")

class Moto(Automovil):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada 

    def acelerar(self, incremento):
        if self.arrancado:
            print(f"La moto {self.marca} {self.modelo} acelera con agilidad.")
            super().acelerar(incremento * 1.5)  # Más potencia al acelerar
        else:
            print(f"No puedes acelerar, la moto {self.marca} {self.modelo} está apagada.")

class Camion(Automovil):
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self.capacidad_carga = capacidad_carga

    def acelerar(self, incremento):
        if self.arrancado:
            print(f"El camión {self.marca} {self.modelo} acelera lentamente debido a su peso.")
            super().acelerar(incremento * 0.5)  # Menos potencia al acelerar
        else:
            print(f"No puedes acelerar, el camión {self.marca} {self.modelo} está apagado.")

# Ejemplo de uso
if __name__ == "__main__":
    coche = Coche("Audi", "A3", puertas=4)
    moto = Moto("Yamaha", "R6", cilindrada=600)
    camion = Camion("Volvo", "FH16", capacidad_carga=20)

    coche.arrancar()
    coche.acelerar(30)
    coche.frenar(10)
    coche.parar()

    moto.arrancar()
    moto.acelerar(40)
    moto.frenar(20)
    moto.parar()

    camion.arrancar()
    camion.acelerar(50)
    camion.frenar(25)
    camion.parar()
