#Posible solucion al ejercicio 2 de la sesion 5

class Automovil:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.estado = "apagado"  # Puede ser 'apagado', 'arrancado', 'en movimiento'

    def arrancar(self):
        if self.estado == "apagado":
            self.estado = "arrancado"
            print(f"El automóvil {self.marca} {self.modelo} ha arrancado.")
        else:
            print("El automóvil ya está arrancado o en movimiento.")

    def acelerar(self, incremento):
        if self.estado == "arrancado" or self.estado == "en movimiento":
            self.velocidad_actual += incremento
            if self.velocidad_actual > self.velocidad_maxima:
                self.velocidad_actual = self.velocidad_maxima
                print(f"Has alcanzado la velocidad máxima: {self.velocidad_maxima} km/h.")
            else:
                print(f"El automóvil acelera a {self.velocidad_actual} km/h.")
            self.estado = "en movimiento"
        else:
            print("Debes arrancar el automóvil antes de acelerar.")

    def frenar(self, decremento):
        if self.estado == "en movimiento":
            self.velocidad_actual -= decremento
            if self.velocidad_actual <= 0:
                self.velocidad_actual = 0
                self.estado = "arrancado"
                print("El automóvil se ha detenido completamente.")
            else:
                print(f"El automóvil reduce la velocidad a {self.velocidad_actual} km/h.")
        else:
            print("El automóvil no está en movimiento para frenar.")

    def parar(self):
        if self.estado != "apagado":
            self.velocidad_actual = 0
            self.estado = "apagado"
            print(f"El automóvil {self.marca} {self.modelo} se ha apagado.")
        else:
            print("El automóvil ya está apagado.")

# Ejemplo de uso
if __name__ == "__main__":
    mi_auto = Automovil("Toyota", "Corolla", 180)

    mi_auto.arrancar()
    mi_auto.acelerar(50)
    mi_auto.acelerar(150)
    mi_auto.frenar(60)
    mi_auto.parar()
