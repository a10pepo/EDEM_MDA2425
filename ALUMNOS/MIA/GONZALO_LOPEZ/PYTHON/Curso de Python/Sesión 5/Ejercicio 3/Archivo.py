
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

# Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:
# Coche
# Moto
# Camión

class Coche(Automovil):
    marca=str
    modelo=str
    año=int
    color=str
    en_marcha=False
    caballos=int
    n_puertas=4 #Por defecto tienen 4 puertas

    def __init__(self,marca:str,modelo:str,año:int,color:str,caballos:int,n_puertas:int=4):
        super().__init__(marca,modelo,año,color)
        self.caballos=caballos
        self.n_puertas=n_puertas

class Moto(Automovil):
    modelo=str
    marca=str
    año=int
    color=str
    en_marcha=False
    caballos=int
    
    def __init__(self,marca:str,modelo:str,año:int,color:str,caballos:int):
        super().__init__(marca,modelo,año,color)
        self.caballos=caballos

class Camion(Automovil):
    modelo=str
    marca=str
    año=int
    color=str
    en_marcha=False
    caballos=int
    n_puertas=int

    def __init__(self,marca:str,modelo:str,año:int,color:str,caballos:int,n_puertas:int):
        super().__init__(marca,modelo,año,color)
        self.caballos=caballos
        self.n_puertas=n_puertas

mi_moto=Automovil('Beta','RR Factory','2017','Roja y Blanca',)
mi_moto.arrancar()
mi_moto.acelerar()
mi_moto.frenar()
mi_moto.parar()

mi_coche=Automovil('ford','mustang','2020','Rojo')
mi_coche.arrancar()
mi_coche.acelerar()
mi_coche.frenar()
mi_coche.parar()

mi_camion=Automovil('mercedes','truck','1850','blanco')
mi_camion.arrancar()
mi_camion.acelerar()
mi_camion.frenar()
mi_camion.parar()
