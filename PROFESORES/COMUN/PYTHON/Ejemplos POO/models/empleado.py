from persona import Persona

class Empleado(Persona):
  puesto:str
  pHora:float
  hTrabajadas: int = 0
  cobro: float = 0.0

  def __init__(self, nombre, apellidos, edad, puesto, pHora):
    # Llamamos al constructor del padre (Persona)
    super(Empleado, self).__init__(nombre, apellidos, edad)
    # Inicializar los atributos propios de Empleado
    self.puesto = puesto
    self.pHora = pHora
  
  def trabajar(self, horas:int):
    self.hTrabajadas += horas
    print(f'{self.nombre} ha trabajado {horas} horas. En total lleva trabajadas: {self.hTrabajadas} horas')
  
  def cobrar(self):
    self.cobro = self.pHora*self.hTrabajadas
    print(f'{self.nombre} cobra: {self.cobro}€')