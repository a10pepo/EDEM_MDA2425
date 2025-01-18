class Automovil:
    marca:str
    modelo:str
    color:str
    anyo_fabricacion:int
    matricula:str

    def __init__(self, marca:str, modelo:str, color:str, anyo_fabricacion:int, matricula:str):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anyo_fabricacion = anyo_fabricacion
        self.matricula = matricula
    
    def arrancar(self):
        print (f'Para arrancar el/la {self.modelo} introduzca la llave y ruedala')

    def acelerar(self):
        print(f'Para acelerar el {self.modelo} pisa embrague con el pie izquierdo, introduce primera y pisa el acelerador con el pie derecho soltando el embrague lentamente')
    
    def frenar(self):
        print (f'Para frenar aprete el freno. Para el {self.modelo} del año {self.anyo_fabricacion} debe revisar los frenos cada año')

    def parar(self):
        print (f'Para parar detener el {self.modelo} pisa embrague y freno hasta quedar detenido, pon punto muerto, pon el freno de mano y quite la llave')


#automovil_1: Automovil = Automovil('ford','mondeo','verde',2020,'3555WER')

#automovil_1.arrancar()
#automovil_1.acelerar()
#automovil_1.frenar()
#automovil_1.parar()