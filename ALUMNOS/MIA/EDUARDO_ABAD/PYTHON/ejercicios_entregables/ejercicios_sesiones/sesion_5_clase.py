# Crear una clase Automóvil

class Automovil() :
    marca: str 
    modelo: str
    color: str
    matricula: str
    year: int
    titular : str
    velocidad : int

    def __init__(self,marca, modelo, color, matricula, year, titular,velocidad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.matricula = matricula
        self.year = year
        self.titular = titular
        self.velocidad = velocidad

    def arrancar(self):
        print(f'El coche {self.marca} {self.modelo} con matricula {self.matricula} ha arrancado ')

    def acelerar(self): 
        print(f'El coche {self.marca} {self.modelo} con matricula {self.matricula} ha acelerado {self.velocidad} km/h ')
    
    def frenar(self): 
        print(f'El coche {self.marca} {self.modelo} con matricula {self.matricula} ha frenado')

    def parar(self): 
        print(f'El coche {self.marca} {self.modelo} con matricula {self.matricula} ha parado ')


mi_coche=Automovil('Opel', 'Astra', 'Gris', '1234BCD', '2016', 'Eduardo', '30' )  # Establecemos mi coche

# Probamos que funcione correctamente

mi_coche.arrancar()
mi_coche.acelerar()
mi_coche.frenar()
mi_coche.parar()

# Herencia de otras clases

# MOTO

class Moto (Automovil):
    tipo_moto: str
    automatica: bool
    abs: bool
    kilometraje: int

    def __init__(self, marca, modelo, color, matricula, year, titular, velocidad, tipo_moto, automatica, abs, kilometraje):
      

        super(Moto, self).__init__(marca, modelo, color, matricula, year, titular, velocidad)
        self.tipo_moto= tipo_moto
        self.automatica = automatica
        self.abs = abs
        self.kilometraje = kilometraje

    def acelerar(self):
        print(f'La moto {self.marca} {self.modelo} de color {self.color} del tipo {self.tipo_moto} con {self.kilometraje} kilometros ha acelerado')

mi_moto=Moto('KTM', 'EXC', 'Naranja', '4567cvb', '2018', 'Eduardo', '60', 'Enduro', 'False', 'True', '17000')

mi_moto.acelerar()

# CAMION

class Camion(Automovil):
    empresa: str
    ruedas: int
    altura: float
    longitud: float

    def __init__(self, marca, modelo, color, matricula, year, titular, velocidad,empresa, ruedas, altura, longitud):
        
        super(Camion, self).__init__(marca, modelo, color, matricula, year, titular, velocidad)
        self.empresa = empresa
        self.ruedas= ruedas
        self.altura = altura
        self.longitud = longitud

def frenar(self):
    print(f'El camion {self.marca} {self.modelo} del año {self.year} que trabaja para la empresa {self.empresa} y que tiene {self.altura} metros de altura')

mi_camion=Camion('Volvo', 'ST100', 'Negro', '4567cvb', '2018', 'Eduardo', '40', 'GOI', '10', '4', '10')

mi_camion.acelerar()     