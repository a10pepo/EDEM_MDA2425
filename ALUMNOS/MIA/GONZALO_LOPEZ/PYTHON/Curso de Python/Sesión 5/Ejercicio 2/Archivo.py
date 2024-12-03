# Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
# Arrancar
# Acelerar
# Frenar
# Parar

class Automovil ():
    marca = str
    modelo = str
    color= str
    año = int

    def __init__(self, marca:str, modelo:str, año:int, color:str):
        self.marca=marca
        self.modelo=modelo
        self.año=año
        self.color=color
        self.en_marcha = False #Por defecto el automovil esta APAGADO


    def arrancar(self) :
        if not self.en_marcha :
            self.en_marcha=True
            print(f'El modelo : {self.modelo} de la marca {self.marca} ha arrancado') 
        else :
            print(f'El {self.modelo} de {self.marca} está apagado')

    def acelerar(self):
        if  self.en_marcha:
            print(f'El modelo:{self.modelo} de la marca {self.marca}  ha acelerado ')
        else :
            print(f'El modelo:{self.modelo} de la marca {self.marca} no ha acelerado ')

    def frenar (self) :
        if  self.en_marcha:
            print(f'El {self.modelo} de la marca {self.marca} ha  frenado')
        else:
            print(f'El {self.modelo} de la marca {self.marca} ya estaba frenado')

    def parar (self) :
        if self.en_marcha:
            self.en_marcha=False
            print(f'El {self.modelo} de la marca {self.marca}  ha  parado')
        else :
            print(f'El {self.modelo} de la marca {self.marca} ya estaba parado')

mi_automovil = Automovil('ferrari','modena','1942','rojo')
mi_automovil.arrancar()
mi_automovil.acelerar()
mi_automovil.frenar()
mi_automovil.parar()