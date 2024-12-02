class Alumno:
    def __init__(self, nif:str, nombre:str, apellidos:str, telefono:int, email:str, aprobado:bool = False):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado

    def aprobar(self):
        self.aprobado = True

    def suspender(self):
        self.aprobado = False
