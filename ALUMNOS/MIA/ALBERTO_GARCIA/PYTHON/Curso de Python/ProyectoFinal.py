
class Alumno():
    nif:str
    nombre:str
    apellido:str
    telefono:str
    email:str
    aprobado:bool

    def __init__(self,nif:str,nombre:str,apellido:str,telefono:str,email:str,aprobado:bool):
        self.nif=nif
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        self.email=email
        self.aprobado=aprobado

    def __str__(self):
        estado = "Aprobado" if self.aprobado else "No aprobado"
        return (f"NIF: {self.nif}, Nombre: {self.nombre}, Apellido: {self.apellido}, "
                f"Teléfono: {self.telefono}, Email: {self.email}, Estado: {estado}")




lista_alumnos = []

#Definición de Funciones
def añadir_alumno(): #1
    while True:
        try:
            nif:str=input('Dame el NIF del alumno sin letra: ')
            nombre:str=input('Dame el nombre del alumno: ')
            apellido:str=input('Dame el apellido del alumno: ')
            telefono:str=input('Dame el teléfono del alumno: ')
            email:str=input('Dame el email del alumno: ')
            aprobado:bool=input('¿El alumno ha aprobado? (s/n):').strip().lower()=='s'
            break
        except ValueError:
            print('Introduce los valores correctamente')
    nuevo_alumno=Alumno(nif,nombre,apellido,telefono,email,aprobado)
    lista_alumnos.append(nuevo_alumno)
    print('Alumno añadido\n')



def eliminar_alumno(): #2
    alumno_eliminado=False
    while True:
        try:
            nif=input('Escribe el NIF del alumno sin letra\n')
            break
        except ValueError:
            print('Introdúcelo correctamente')
    for i, alumno in enumerate(lista_alumnos):
        if(alumno.nif==nif):
            del lista_alumnos[i]
            print(f'El alumno con NIF {nif} ha sido eliminado')
            alumno_eliminado=True
    if not alumno_eliminado:
            print('No se ha encontrado ningun alumno con ese NIF')

def actualizar_datos(): #3  
    alumno_encontrado=False
    while True:
        try:
            nif=input('Escribe el NIF del alumno sin letra\n')
            break
        except ValueError:
            print('Introdúcelo correctamente')
    for alumno in lista_alumnos:
        if alumno.nif==nif:
            alumno_encontrado=True
            print(f'Los datos actuales del alumno son los siguientes:\n{alumno}')
            print('Escriba los nuevos datos')
            nuevo_nombre:str=input('Dame el nombre del alumno: ')
            nuevo_apellido:str=input('Dame el apellido del alumno: ')
            nuevo_telefono:str=input('Dame el teléfono del alumno: ')
            nuevo_email:str=input('Dame el email del alumno: ')
            nuevo_aprobado:bool=input('¿El alumno ha aprobado? (s/n):').strip().lower()=='s'

            alumno.nombre=nuevo_nombre
            alumno.apellido=nuevo_apellido
            alumno.telefono=nuevo_telefono
            alumno.email=nuevo_email
            alumno.aprobado=nuevo_aprobado
            print("Los datos se han actualizado correctamente")
            break
    if not alumno_encontrado:
            print('No se ha encontrado el alumno con el NIF indicado')

def mostrar_datos_NIF(): #4 
    alumno_encontrado=False
    while True:
        try:
            nif=input('Escribe el NIF del alumno sin letra\n')
            break
        except ValueError:
            print('Introdúcelo correctamente')
    for i, alumno in enumerate(lista_alumnos):
        if alumno.nif==nif:
            print(f'Los datos del alumno son los siguientes:{lista_alumnos[i]}')
            alumno_encontrado=True
    if not alumno_encontrado:
            print('No se ha encontrado el alumno con el NIF indicado')


def mostrar_datos_mail(): #5
    alumno_encontrado=False
    while True:
        try:
            mail=input('Escribe el mail del alumno\n')
            break
        except ValueError:
            print('Introdúcelo correctamente')
    for i, alumno in enumerate(lista_alumnos):
        if alumno.nif==mail:
            print(f'Los datos del alumno son los siguientes:{lista_alumnos[i]}')
            alumno_encontrado=True
    if not alumno_encontrado:
            print('No se ha encontrado el alumno con el NIF indicado')

def listar_alumnos(): #6
    for i, alumno in enumerate(lista_alumnos):
        print(f"Los datos del alumno {i} son: {lista_alumnos[i]}")

def aprobar_alumno(): #7
    alumno_encontrado=False
    while True:
        try:
            nif=input('Escribe el NIF del alumno sin letra\n')
            break
        except ValueError:
            print('Introdúcelo correctamente')
    for i, alumno in enumerate(lista_alumnos):
        if alumno.nif==nif:
            alumno.aprobado=True
            print(f'El alumno ha sido aprobado')
            alumno_encontrado=True
    if not alumno_encontrado:
            print('No se ha encontrado el alumno con el NIF indicado')

def suspender_alumno(): #8
    alumno_encontrado=False
    while True:
        try:
            nif=input('Escribe el NIF del alumno sin letra\n')
            break
        except ValueError:
            print('Introdúcelo correctamente')
    for i, alumno in enumerate(lista_alumnos):
        if alumno.nif==nif:
            alumno.aprobado=False
            print(f'El alumno ha sido suspendido')
            alumno_encontrado=True
    if not alumno_encontrado:
            print('No se ha encontrado el alumno con el NIF indicado')

def listar_aprobados(): #9
    print('Los alumnos aprobados son:\n')
    aprobados_encontrados=False
    for alumno in lista_alumnos:
        if alumno.aprobado:
            print(alumno)
            aprobados_encontrados=True
    if not aprobados_encontrados:
        print('No hay alumnos aprobados, a estudiar más.')

def listar_suspensos(): #10
    print('Los alumnos suspensos son:\n')
    aprobados_encontrados=False
    for alumno in lista_alumnos:
        if not alumno.aprobado:
            print(alumno)
            aprobados_encontrados=True
    if not aprobados_encontrados:
        print('No hay alumnos suspensos, dejad de copiaros.')



#Main
while True:
    entrada=input("""¿Qué deseas hacer?
                      
(1) Añadir un alumno 

(2) Eliminar alumno por NIF

(3) Actualizar datos de un alumno por NIF

(4) Mostrar datos de un alumno por NIF

(5) Mostrar datos de un alumno por Email

(6) Listar TODOS os alumnos

(7) Aprobar Alumno por NIF

(8) Suspender Alumno por NIF

(9) Mostrar alumnos aprobados

(10) Mostrar alumnos suspensos

(X) Finalizar Programa 
                      
""" ).strip().upper()

    if(entrada=='1'):
        añadir_alumno()
    elif(entrada=='2'):
        eliminar_alumno()
    elif(entrada=='3'):
        actualizar_datos()
    elif(entrada=='4'):
        mostrar_datos_NIF()
    elif(entrada=='5'):
        mostrar_datos_mail()
    elif(entrada=='6'):
        listar_alumnos()
    elif(entrada=='7'):
        aprobar_alumno()
    elif(entrada=='8'):
        suspender_alumno()
    elif(entrada=='9'):
        listar_aprobados()
    elif(entrada=='10'):
        listar_suspensos()
    elif(entrada=='X'):
        print('Saliendo del programa')
        break
    else:
        print('Opción no válida, intente de nuevo')