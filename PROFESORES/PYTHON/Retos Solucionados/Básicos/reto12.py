'''
    ---------- RETO 12 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa que almacene en una lista (Array) todos los nombres de los alumnos del curso y los muestre en por pantalla.
'''

def reto12Basico():
  lista_alumnos: [str] = ['Julia', 'Hugo', 'Miguel', 
                        'Victor', 'Juan', 'Aberto', 
                        'María', 'Andreu', 'Borja',
                        'Claudio', 'Elisa', 'Diego',
                        'Enrique', 'Estela', 'Francisco',
                        'Irene', 'Isabel', 'Javier', 'Luis', 'Marta']

  print('*** ALUMNOS ***')
  for alumno in lista_alumnos:
      print(f"- {alumno}")