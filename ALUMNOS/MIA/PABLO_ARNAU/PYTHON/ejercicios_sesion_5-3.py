from ejercicios_sesion_5_2 import Automovil

class coche(Automovil):
    puertas: int
    rueda_recambio: bool

    def __init__(self, marca:str, modelo:str, color:str, anyo_fabricacion:int, matricula:str, puertas:int, rueda_recambio:bool):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anyo_fabricacion = anyo_fabricacion
        self.matricula = matricula
        self.puertas = puertas
        self.rueda_recambio = rueda_recambio

#Aqui he cambiado el método arrancar en la clase coche para que especifique las puertas del coche ya que es algo que puede variar

    def arrancar(self):
        print (f'Para arrancar el {self.modelo} con {self.puertas} puertas introduzca la llave y ruedala')


class moto(Automovil):
    cilindrada: int
    permiso_necesario: str

    
    def __init__(self, marca:str, modelo:str, color:str, anyo_fabricacion:int, matricula:str, cilindrada:int, permiso_necesario:str):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anyo_fabricacion = anyo_fabricacion
        self.matricula = matricula
        self.cilindrada = cilindrada
        self.permiso_necesario = permiso_necesario


class camion(Automovil):
    tipo_remolque: str
    carga_max: int


    
    def __init__(self, marca:str, modelo:str, color:str, anyo_fabricacion:int, matricula:str,tipo_remolque:str, carga_max:int):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anyo_fabricacion = anyo_fabricacion
        self.matricula = matricula
        self.tipo_remolque = tipo_remolque
        self.carga_max = carga_max


coche_1: coche=coche("ford","focus","rojo",2223, "4455VVV",4,False)

coche_1.arrancar()

moto_1: moto=moto("kawasaki","ninja","verde",2020,"3333RRR",250,"C2")

#En este caso el métoco no se ha modifica por tanto utiliza el definido en la clase Automóvil
moto_1.arrancar()