lista_alumnos_id= []
lista_alumnos_completa={}

def añadir_alumno(lista_alumnos_completa):
    nombre: str =input('Introduce tu nombre: ')
    apellidos: str = input('Introduce tus apellidos: ')
    NIF: str = input('Introduce tu NIF: ')
    telefono: str = input('Introduce tu telefono: ')
    email: str = input('Introduce tu email: ')
    aprobado:bool= bool(input ('Introduce si está aprobado (True) o suspenso (False): '))
    datos_alumno={
        'nombre': nombre,
        'apellidos': apellidos,
        'NIF': NIF,
        'telefono': telefono,
        'email': email,
        'aprobado': aprobado
        }
    lista_alumnos_completa[NIF]= datos_alumno
    

def eliminar_alumno(lista_alumnos_completa,por_dni):       
    if por_dni in lista_alumnos_completa:
        del(lista_alumnos_completa[por_dni])
        print('Alumno eliminado con éxito')
    else:
        print('El DNI no se encuentra en la lista de alumnos')    

def actualizar_alumno(lista_alumnos_completa,por_dni):     
    if por_dni in lista_alumnos_completa:
         lista_alumnos_completa[por_dni]['nombre'] = input('Introduce nuevo nombre: ')
         lista_alumnos_completa[por_dni]['apellidos'] = input('Introduce nuevos apellidos: ')
         lista_alumnos_completa[por_dni]['NIF'] = input('Introduce un nuevo NIF: ')
         lista_alumnos_completa[por_dni]['telefono'] = input('Introduce nuevo telefono: ')
         lista_alumnos_completa[por_dni]['email'] = input('Introduce nuevo email: ')
         lista_alumnos_completa[por_dni]['aprobado'] = input('Introduce si está aprobado (True) o suspenso (False): ')
         print('Información actualizada correctamente')
    else:
        print('El DNI no se encuentra en la lista de alumnos')

def mostrar_alumno(lista_alumnos_completa, por_dni):
    if por_dni in lista_alumnos_completa:
        print(lista_alumnos_completa[por_dni])

def mostrar_alumno_correo(lista_alumnos_completa, introduce_correo):
    for alumno in lista_alumnos_completa.values():
        if alumno['email'] == introduce_correo :
            print(alumno)
        else:
            print('El correo no se encuentra en la lista de alumnos')

def mostrar_alumnos(lista_alumnos_completa):
    print(lista_alumnos_completa)

def aprobar_alumno(lista_alumnos_completa,por_dni):
    if por_dni in lista_alumnos_completa:
      lista_alumnos_completa[por_dni]['aprobado'] = True
      print('El alumno ha sido aprobado')  

def suspender_alumno(lista_alumnos_completa, por_dni):
    if por_dni in lista_alumnos_completa:
      lista_alumnos_completa[por_dni]['aprobado'] = False
      print('El alumno ha sido suspendido')  

def mostrar_aprobados(lista_alumnos_completa):
    for alumno in lista_alumnos_completa.values():
        if alumno['aprobado']== True:  
           print(alumno)
        else:
            print('No hay alumnos aprobados')

def mostrar_suspenso(lista_alumnos_completa):
    for alumno in lista_alumnos_completa.values():
        if alumno['aprobado'] == False:  
           print(alumno)
