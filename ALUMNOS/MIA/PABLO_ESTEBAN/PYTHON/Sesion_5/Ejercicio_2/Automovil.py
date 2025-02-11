class Automovil:
    
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelerando = False
        self.frenando = False
        self.velocidad = 0
    
    def arrancar(self) -> None:
        self.enMarcha = True
    
    def acelerar(self) -> None:
        self.acelerando = True
        self.velocidad += 1
    
    def frenar(self) -> None:
        self.frenando = True
        self.velocidad -= 1
    
    def parar(self) -> None:
        self.enMarcha = False
        self.acelerando = False
        self.frenando = False
        self.velocidad = 0