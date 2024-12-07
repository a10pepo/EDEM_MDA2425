# 3
## Lo de las potencias entiendo que habría que moficar las funciones dentro de cada subclase, 
'''
Para la parte de "salvo que algunos deben tener más potencia que otros", 
entiendo que habría que moficar las funciones de arrancar, parar, acelerar para tener en cuenta la potencia de cada tipo de automóvil.
Por ejemplo (coche):
def arrancar(self):
        self.velocidad = 10 => multiplicarlo por un valor para señalar que es más potente?

No sé muy bien qué criterio seguir...
'''
from entregable52 import Automovil

class Coche(Automovil):
    n_plazas:int
    n_puertas:int
    caballos:int

    def __init__(self, marca:str, modelo:str, color:str, velocidad:float, n_plazas:int, n_puertas:int, caballos:int):
        super().__init__(marca, modelo, color, velocidad)
        self.n_plazas = n_plazas
        self.n_puertas = n_puertas
        self.caballos = caballos
    
    
class Camion(Automovil):
    carga:float
    n_contenedores:int

    def __init__(self, marca: str, modelo: str, color: str, carga:float, n_contenedores:int):
        super().__init__(marca, modelo, color)
        self.carga = carga
        self.n_contenedores = n_contenedores


class Moto(Automovil):
    tipo_manillar:str
    maletero:bool
    cilindradas:int

    def __init__(self, marca: str, modelo: str, color: str, tipo_manillar:str, maletero:bool, cilindradas:int):
        super().__init__(marca, modelo, color)
        self.tipo_manillar = tipo_manillar
        self.maletero = maletero
        self.cilindradas = cilindradas


