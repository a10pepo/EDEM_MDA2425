# 1. Enunciado Proyecto FInal
# Una empresa de formación quiere gestionar su cartera de alumnos.
# Escribe un programa que guarde una lista de alumnos. Cada Alumno dispone de los siguientes campos:

# NIF (string)
# Nombre (string)
# Apellidos (string)
# Teléfono (string)
# Email (string)
# Aprobado (boolean)


# El programa debe mostrar las siguientes opciones por consola para que escoja el usuario:

# (1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno
# (2) Eliminar alumno por NIF
# (3) Actualizar datos de un alumno por NIF
# (4) Mostrar datos de un alumno por NIF
# (5) Mostrar datos de un alumno por Email
# (6) Listar TODOS os alumnos
# (7) Aprobar Alumno por NIF
# (8) Suspender Alumno por NIF
# (9) Mostrar alumnos aprobados
# (10) Mostrar alumnos suspensos
# (X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X

class Alumno ():
    nif:str
    nombre:str
    apellidos:str
    telefono:str
    email:str
    aprobado:bool

    def __init__(self,nif,nombre,apellidos,telefono,email,aprobado):
        self.nif=nif
        self.nombre=nombre
        self.apellidos=apellidos
        self.telefono=telefono
        self.email=email
        self.aprobado=aprobado

    def __str__(self):
        estado = "Aprobado" if self.aprobado else "Suspenso"
        return f"NIF: {self.nif}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, Teléfono: {self.telefono}, Email: {self.email}, Estado: {estado}"


def añadir_alumno(lista_alumnos):    # CREO UNA FUNCION PARA CADA OPCION DEL MENU
    nif = input("Introduce el NIF del alumno: ").strip()
    if any(alumno.nif == nif for alumno in lista_alumnos):
        print("Ya existe un alumno con ese NIF.")
        return
    
    nombre=str(input("Introduce el nombre del alumno:"))
    apellidos=str(input("Introduce los apellidos del alumno:"))
    telefono=str(input("Introduce el telefono del alumno :"))
    email=str(input("Introduce el email del alumno:"))
    aprobado=bool(input("Introduce el estado del alumno:"))

    nuevo_alumno=Alumno(nif,nombre,apellidos,telefono,email,aprobado)
    lista_alumnos.append(nuevo_alumno)
    print("Se ha añadido el nuevo alumno con exito.")

def eliminar_alumno_por_nif (lista_alumnos):
    nif=input('Introduce el NIF del alumno a eliminar:').strip()
    for alumno in lista_alumnos:
        if alumno.nif==nif:
            lista_alumnos.remove(alumno)
            print('Alumno eliminado con exito')
            return
    print('No encontrado')
    

def actualizar_alumno(lista_alumnos):
    nif = input("Introduce el NIF del alumno a actualizar: ").strip()
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            print("Introduce los nuevos datos. Presiona Enter para mantener el dato actual.")
            nombre = input(f"Nombre actual ({alumno.nombre}): ").strip() or alumno.nombre
            apellidos = input(f"Apellidos actuales ({alumno.apellidos}): ").strip() or alumno.apellidos
            telefono = input(f"Teléfono actual ({alumno.telefono}): ").strip() or alumno.telefono
            email = input(f"Email actual ({alumno.email}): ").strip() or alumno.email
            aprobado_str = input(f"Estado actual ({'Aprobado' if alumno.aprobado else 'Suspenso'}). ¿Aprobado? (si/no): ").strip().lower()
            aprobado = alumno.aprobado if aprobado_str == "" else aprobado_str == "si"

            alumno.nombre = nombre
            alumno.apellidos = apellidos
            alumno.telefono = telefono
            alumno.email = email
            alumno.aprobado = aprobado
            print("Alumno actualizado con éxito.")
            return
    print("Alumno no encontrado.")

def mostrar_alumno_por_nif(lista_alumnos) :
    nif=input('Introduce el NIF del alumno para ver sus datos:').strip()
    for alumno in lista_alumnos:
        if alumno.nif==nif:
            print(alumno)
            return
        
    print('No hay datos de ningún alumno con ese NIF')

def mostrar_alumno_por_email(lista_alumnos):
    email=input('Introduce el email del alumno para ver sus datos:').strip()
    for alumno in lista_alumnos:
        if alumno.email==email:
            print(alumno)
            return
    print('No hay datos de ningún alumno con ese email.')    


def listar_alumnos(lista_alumnos):
    if not lista_alumnos:
        print('No hay ningún alumno en la lista.')
    else:
        for alumno in lista_alumnos:
            print(alumno)


def aprobar_alumno_por_nif(lista_alumnos):
    nif=input('Introduce el NIF del alumno que quieres aprobar:').strip()
    for alumno in lista_alumnos:
        if alumno.nif==nif:
            alumno.aprobado=True
            print('Alumno aprobado con exito')
            return
    print('No hay ningún alumno con ese NIF')    

def suspender_alumno_por_nif(lista_alumnos):
    nif=input('Introduce el NIF del alumno que quieres suspender:').strip()
    for alumno in lista_alumnos:
        if alumno.nif==nif:
            alumno.aprobado=False
            print('Alumno suspendido con exito')
    print('No hay ningún alumno con ese NIF')

def mostrar_alumnos_aprobados(lista_alumnos):
    aprobados=[alumno for alumno in lista_alumnos if alumno.aprobado]
    if not aprobados:
        print(' No hay ningún alumno aprobado')
    else:
        for alumno in aprobados:
            print(alumno)

def mostrar_alumnos_suspensos(lista_alumnos):
    suspensos=[alumno for alumno in lista_alumnos if not  alumno.aprobado]
    if not suspensos:
        print('No hay alumnos suspensos')
    else:
        for alumno in suspensos:
            print(alumno)    




def mostrar_menu():
    print( """
(1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno
(2) Eliminar alumno por NIF
(3) Actualizar datos de un alumno por NIF
(4) Mostrar datos de un alumno por NIF
(5) Mostrar datos de un alumno por Email
(6) Listar TODOS os alumnos
(7) Aprobar Alumno por NIF
(8) Suspender Alumno por NIF
(9) Mostrar alumnos aprobados
(10) Mostrar alumnos suspensos
(X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X"""

)
mostrar_menu()



def main():
    while True:
        mostrar_menu()   # Mostrar menú cada vez que entra al bucle
        opcion=input('Selecciona la opción deseada:').strip().lower()
        if opcion == '1':
            añadir_alumno(lista_alumnos)
        elif opcion == '2':
            eliminar_alumno_por_nif(lista_alumnos)
        elif opcion == '3':
            actualizar_alumno(lista_alumnos)
        elif opcion == '4':
            mostrar_alumno_por_nif(lista_alumnos)
        elif opcion == '5':
            mostrar_alumno_por_email(lista_alumnos)
        elif opcion == '6':
            listar_alumnos(lista_alumnos)
        elif opcion == '7':
            aprobar_alumno_por_nif(lista_alumnos)
        elif opcion == '8':
            suspender_alumno_por_nif(lista_alumnos)
        elif opcion == '9':
            mostrar_alumnos_aprobados(lista_alumnos)
        elif opcion == '10':
            mostrar_alumnos_suspensos(lista_alumnos)
        elif opcion == 'x':
            print("Finalizando el programa...")
            break
        else:
            print("Opción no válida.")        

if __name__ == "__main__":
    main()





    













