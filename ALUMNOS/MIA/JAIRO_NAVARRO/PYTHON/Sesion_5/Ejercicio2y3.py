class Automovil:
    arrancar: str
    acelerar: str
    frenar: str
    parar: str

    def __init__(self, ar: str, ac: str, fr:str, pr:str):
        self.arrancar = ar == 'ok' 
        self.acelerar = ac == 'ok'
        self.frenar = fr == 'ok'
        self.parar = pr == 'ok'


class Moto(Automovil):
    potencia:int
    def __init__(self, ar:str, ac:str, fr:str, pr:str, ve:str, potencia:int):
        super().__init__(ar, ac, fr, pr)
        self.potencia = potencia
        self.vehiculo = ve
    def tipoautomovil(self):
        print(f'el vehiculo {self.vehiculo}, tiene potencia {self.potencia}, con estatus arrancar: {self.arrancar}, acelerar: {self.acelerar}, frenar {self.frenar}, y parar {self.parar}')


class Coche(Automovil):
    potencia:int
    def __init__(self, ar:str, ac:str, fr:str, pr:str, ve:str, potencia:int):
        super().__init__(ar, ac, fr, pr)
        self.potencia = potencia
        self.vehiculo = ve
    def tipoautomovil(self):
        print(f'el vehiculo {self.vehiculo}, tiene potencia {self.potencia}, con estatus arrancar: {self.arrancar}, acelerar: {self.acelerar}, frenar {self.frenar}, y parar {self.parar}')

class Camion(Automovil):
    potencia:int
    def __init__(self, ar:str, ac:str, fr:str, pr:str, ve:str, potencia:int):
        super().__init__(ar, ac, fr, pr)
        self.potencia = potencia
        self.vehiculo = ve
    def tipoautomovil(self):
        print(f'el vehiculo {self.vehiculo}, tiene potencia {self.potencia}, con estatus arrancar: {self.arrancar}, acelerar: {self.acelerar}, frenar {self.frenar}, y parar {self.parar}')

mi_moto = Moto("ok", "ok", "ok", "ok", "Moto Deportiva", 50)
mi_coche = Coche("ok", "ok", "ok", "ok", "Coche Deportivo", 100)
mi_camion = Camion("ok", "ok", "ok", "ok", "Camión de Carga", 150) 
# obtener valores de un objeto
print('Potencia de Moto:', mi_moto.potencia)
print('Potencia de Coche:', mi_coche.potencia)
print('Potencia de Camión', mi_camion.potencia)

