class Automovil():
    marca:str
    modelo:str
    color:str
    matricula:str    
    id_seguro:str
    titular:str
    velocidad:float = 0
    
    
    def __init__(self, marca, modelo, color, matricula, id_seguro, titular):
      self.marca = marca
      self.modelo = modelo
      self.color = color
      self.matricula = matricula
      self.id_seguro = id_seguro
      self.titular = titular
    
    def arrancar(self):
      self.velocidad = 10
      print('El automovil ha arrancado')
      
    def frenar(self, presion: float):
      self.velocidad -= (presion - 10)
      print(f'El automovil ha frenado. Su velocidad ahora es {self.velocidad}km/h')
    
    def acelerar(self, presion: float):
      self.velocidad += (presion + 10)
      print(f'El automovil ha acelerado. Su velocidad ahora es {self.velocidad}km/h')

    def parar(self):
      self.velocidad = 0
      print('El automovil ha parado')