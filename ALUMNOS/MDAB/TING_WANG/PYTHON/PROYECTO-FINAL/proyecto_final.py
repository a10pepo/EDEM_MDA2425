from lista_alumnos import *
from funciones import *

with open('mensaje.txt', 'r') as fichero:
    mensaje = fichero.read()

alumno_nuevo = {
    "Nombre": None,
    "Apellidos": None,
    "NIF": None,
    "Teléfono": None,
    "email":None,
    "Aprobado":None
    }


while (True):
    inicio = input(mensaje)
    
    if (inicio == '1'):
        alumno_amacenado = nuevo_alumno()
        reiniciar_programa()
        
    elif (inicio == '2'):
        eliminar_alumno()
        reiniciar_programa()
                  
    elif (inicio == '3'):
        actualizar_alumno()
        reiniciar_programa()
        
    elif (inicio == '4'):
        mostrarPorNIF()
        reiniciar_programa()
        
    elif (inicio == '5'): 
        mostrarPorEMAIL()  
        reiniciar_programa()
        
    elif (inicio == '6'):
        mostrar_alumnos()
        reiniciar_programa()

    elif (inicio == '7'):
        aprobar_alumno()
        reiniciar_programa()

    elif (inicio == '8'):
        suspender_alumno()
        reiniciar_programa()

    elif (inicio == '9'):
        alumnos_aprobados()
        reiniciar_programa()
    
    elif (inicio == '10'):
        alumnos_suspensos()
        reiniciar_programa()

    elif (inicio.upper() == 'X'):
        print('¡Nos vemos!')
        break

    else:
        input('Por favor, eliga una opción del 1-10 o X para salir')
        continue
  