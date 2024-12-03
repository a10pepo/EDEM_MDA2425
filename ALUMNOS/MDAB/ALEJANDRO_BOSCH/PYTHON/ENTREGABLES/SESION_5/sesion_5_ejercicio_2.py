class Automovil:
    marca:str
    modelo:str
    encendido:bool
    velocidad_actual: int

    def __init__(self, marca:str, modelo:str):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.velocidad_actual = 0

    def arrancar(self):
        if not self.encendido:
                self.encendido = True
                print(f"El automovil {self.marca} {self.modelo} esta arrancando")
        else:
                print(f"El automovil {self.marca} {self.modelo} ya esta arrancado")

    def acelerar(self, incremento):
            if self.encendido:
                self.velocidad_actual += incremento
                print(f"El automovil {self.marca} {self.modelo} ha acelerado a {self.velocidad_actual} KM/H")
            else: 
                print(f"No es posible acelerar, el automovil {self.marca} {self.modelo} esta apagado")



    def frenar(self, decremento):
            if not self.encendido:
                print(f"El automóvil {self.marca} {self.modelo} está apagado y no puede frenar.")
                return

            if self.velocidad_actual - decremento >= 0:
                self.velocidad_actual -= decremento
                print(f"El automóvil {self.marca} {self.modelo} ha frenado, la velocidad actual es de {self.velocidad_actual} KM/H")
            else:
                self.velocidad_actual = 0
                print(f"El automóvil {self.marca} {self.modelo} se ha detenido por completo.")



    def parar(self):
        if self.encendido:
            self.velocidad_actual = 0
            self.encendido = False
            print(f"El automovil {self.marca} {self.modelo} ha parado")
        else:
            print(f"El automovil {self.marca} {self.modelo} esta en marcha")


#se prueba el automovil 🏎️👍

mi_automovil = Automovil("Ferrari", "LaFerrari")
mi_automovil.arrancar(mi_automovil)
mi_automovil.acelerar(mi_automovil, 400)
mi_automovil.frenar(mi_automovil, 20)
mi_automovil.parar(mi_automovil)