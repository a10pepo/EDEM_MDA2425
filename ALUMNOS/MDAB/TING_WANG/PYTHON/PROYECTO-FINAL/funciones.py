from lista_alumnos import *

def nuevo_alumno():
    alumno_nuevo = {
        "Nombre": input('Introduce su nombre: '),
        "Apellidos": input('Introduce sus apellidos: '),
        "NIF": input('Intruduce su NIF: '),
        "Teléfono": input('Intruduce su teléfono: '),
        "email": input('Intruduce su e-mail: '),
        "Aprobado": input('¿Ha aprobado? (Yes/No): ').lower() == 'yes'
    }
    lista_alumnos.append(alumno_nuevo)
    print('Alumno añadido:', alumno_nuevo)
    return alumno_nuevo


def eliminar_alumno():
    alumnoNIF = input('¿Qué alumno quieres eliminar? Introduce su NIF:' )
    for alumno in lista_alumnos:
         if alumno['NIF'] == alumnoNIF:
            lista_alumnos.remove(alumno)
            print(f'El alumno con NIF {alumnoNIF} ha sido eliminado')
            return


def actualizar_alumno():
    alumnoNIF = input('¿Quieres actualizar la información de un alumno? Introduce su NIF:' )
    encontrado = False
    for alumno in lista_alumnos:
        if alumno['NIF'] == alumnoNIF:
            encontrado = True
            print('Los datos actuales del alumno son:', alumno)

            respuesta = input('¿Quieres cambiar el nombre? (Yes/No): ').lower()
            while respuesta not in ('yes', 'no'):
                respuesta = input('Por favor, responde "Yes" o "No": ').lower()
            if respuesta == 'yes':
                alumno['Nombre'] = input('Introduce el nuevo nombre: ')
            
            respuesta = input('¿Quieres cambiar los apellidos? (Yes/No): ').lower()
            while respuesta not in ('yes', 'no'):
                respuesta = input('Por favor, responde "Yes" o "No": ').lower()
            if respuesta == 'yes':
                alumno['Apellidos'] = input('Introduce los nuevos apellidos: ')

            respuesta = input('¿Quieres cambiar el teléfono? (Yes/No): ').lower()
            while respuesta not in ('yes', 'no'):
                respuesta = input('Por favor, responde "Yes" o "No": ').lower()
            if respuesta == 'yes':
                alumno['Teléfono'] = input('Introduce el nuevo teléfono: ')

            respuesta = input('¿Quieres cambiar el e-mail? (Yes/No): ').lower()
            while respuesta not in ('yes', 'no'):
                respuesta = input('Por favor, responde "Yes" o "No": ').lower()
            if respuesta == 'yes':
                alumno['email'] = input('Introduce el nuevo e-mail: ')
            
            respuesta = input('¿Quieres cambiar el estado de aprobado? (Yes/No): ').lower()
            while respuesta not in ('yes', 'no'):
                respuesta = input('Por favor, responde "Yes" o "No": ').lower()
            if respuesta == 'yes':
                nuevo_aprobado = input('¿Ha aprobado? (Yes/No): ').lower()
                alumno['Aprobado'] = nuevo_aprobado == 'yes'
            print('Información actualizada: ', alumno)
            return


def mostrarPorNIF():
    alumnoNIF = input('Introduzca el NIF del alumno para mostrar sus datos: ')
    encontrado = False
    for alumno in lista_alumnos:
        if alumno['NIF'] == alumnoNIF:
            print(alumno)
            encontrado = True
            break
    if not encontrado:
        print(f'No se ha encontrado el alumno con NIF {alumnoNIF}')


def mostrarPorEMAIL():
    alumnoCorreo = input('Introduzca el e-mail del alumno para mostrar sus datos: ')
    encontrado = False
    for alumno in lista_alumnos:
        if alumno['email'] == alumnoCorreo:
            print(alumno)
            encontrado = True
            break
    if not encontrado:
        print(f'No se ha encontrado el alumno con e-mail {alumnoCorreo}')
    

def mostrar_alumnos():
    print(lista_alumnos)


def aprobar_alumno():
    alumnoNIF = input('Indica el NIF del alumno que quieres aprobar: ')
    encontrado = False
    for alumno in lista_alumnos:
        if alumno['NIF'] == alumnoNIF:
            alumno['Aprobado'] = True
            print(f'El alumno con NIF {alumnoNIF} ha sido aprobado')
            encontrado = True
            return
    if not encontrado:
        print(f'No se ha encontrado el alumno con NIF {alumnoNIF}')


def suspender_alumno():
    alumnoNIF = input('Indica el NIF del alumno que quieres suspender: ')
    encontrado = False
    for alumno in lista_alumnos:
        if alumno['NIF'] == alumnoNIF:
            alumno['Aprobado'] = False
            print(f'El alumno con NIF {alumnoNIF} ha sido suspendido')
            encontrado = True
            return
    if not encontrado:
        print(f'No se ha encontrado el alumno con NIF {alumnoNIF}')

def alumnos_aprobados():
    for alumno in lista_alumnos:
        if alumno["Aprobado"] == True:
            print(alumno)
            

def alumnos_suspensos():
    for alumno in lista_alumnos:
        if alumno["Aprobado"] == False:
            print(alumno)


def reiniciar_programa():
    while (True):
        reinicio = input('¿Quieres realizar otra acción? Yes/No: ').lower()
        if reinicio == 'yes':
            with open('mensaje.txt', 'r') as fichero:
                mensaje = fichero.read()
            print(mensaje)
            break
        if reinicio == 'no':
            print('¡Nos vemos!')
            exit()
        else:
            continue
        
