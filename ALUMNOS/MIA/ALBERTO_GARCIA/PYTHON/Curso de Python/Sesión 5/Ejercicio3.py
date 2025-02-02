from Ejercicio2 import Automovil

class moto(Automovil):
    cilindrada:int

    def __init__(self, marca, modelo, color, matricula, id_seguro, titular,cilindrada:int):
        super().__init__(marca, modelo, color, matricula, id_seguro, titular)
        self.cilindrada = cilindrada

    def arrancar(self):
      self.velocidad = 10
      print('La moto ha arrancado')
      
    def frenar(self, presion: float):
      self.velocidad -= (presion - 5)
      print(f'La moto ha frenado. Su velocidad ahora es {self.velocidad}km/h')
    
    def acelerar(self, presion: float):
      self.velocidad += (presion + 20)
      print(f'LA moto ha acelerado. Su velocidad ahora es {self.velocidad}km/h')

    def parar(self):
      self.velocidad = 0
      print('La moto ha parado')

class coche(Automovil):
    n_puertas:int

    def __init__(self, marca, modelo, color, matricula, id_seguro, titular,n_puertas:int):
        super().__init__(marca, modelo, color, matricula, id_seguro, titular)
        self.n_puertas = n_puertas

    def arrancar(self):
      self.velocidad = 10
      print('El coche ha arrancado')
      
    def frenar(self, presion: float):
      self.velocidad -= (presion - 10)
      print(f'El coche ha frenado. Su velocidad ahora es {self.velocidad}km/h')
    
    def acelerar(self, presion: float):
      self.velocidad += (presion + 10)
      print(f'El coche ha acelerado. Su velocidad ahora es {self.velocidad}km/h')

    def parar(self):
      self.velocidad = 0
      print('El coche ha parado')

class camion(Automovil):
    carga_max:int

    def __init__(self, marca, modelo, color, matricula, id_seguro, titular,carga_max:int):
        super().__init__(marca, modelo, color, matricula, id_seguro, titular)
        self.carga_max = carga_max

    def arrancar(self):
      self.velocidad = 10
      print('El camión ha arrancado')
      
    def frenar(self, presion: float):
      self.velocidad -= (presion - 15)
      print(f'El camión ha frenado. Su velocidad ahora es {self.velocidad}km/h')
    
    def acelerar(self, presion: float):
      self.velocidad += (presion + 5)
      print(f'El camión ha acelerado. Su velocidad ahora es {self.velocidad}km/h')

    def parar(self):
      self.velocidad = 0
      print('El camión ha parado')