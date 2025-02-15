#5. Ejercicios Sesión 5
    #2.Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
        #1.Arrancar

class Coche:
    velocidad:float=0
    nombre:str

    def __init__(self,nombre) -> None:
        self.nombre=nombre

    def mostrar_velocidad(self):
        print(f"El veiculo, {self.nombre}, se desplaza a {self.velocidad}KM/H")

    def arrancar(self):
        if self.velocidad > 0:
            print(f"El veiculo, {self.nombre}, ya esta en marcha" )
        else:
            self.velocidad=10

        #2.Acelerar

    def acelerar(self):
        if self.velocidad > 0:
            self.velocidad=self.velocidad+10
        else:
            print(f"El veiculo, {self.nombre}, no ha arrancado. No puede acelerar si estar en marcha" )
            
        #3.Frenar

    def frenar(self):
        if self.velocidad > 0:
            self.velocidad=self.velocidad-10
        else:
            print(f"El veiculo, {self.nombre}, ya esta detenido y, por tanto, no puede frenar más" )

        #4.Parar

    def parar(self):
        if self.velocidad > 0:
            self.velocidad=0
        else:
            print(f"El veiculo, {self.nombre}, ya esta detenido." )

mi_carro: Coche = Coche("panda")

mi_carro.mostrar_velocidad()
mi_carro.frenar()
mi_carro.arrancar()
mi_carro.mostrar_velocidad()
mi_carro.acelerar()
mi_carro.mostrar_velocidad()
mi_carro.frenar()
mi_carro.mostrar_velocidad()
mi_carro.parar()
mi_carro.mostrar_velocidad()
