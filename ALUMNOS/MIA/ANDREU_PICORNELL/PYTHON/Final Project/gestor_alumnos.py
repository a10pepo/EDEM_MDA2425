from alumno import Alumno

lista_alumnos = []

def agregar_alumno(nif, nombre, apellidos, telefono, email):
    nuevo_alumno = Alumno(nif, nombre, apellidos, telefono, email)
    lista_alumnos.append(nuevo_alumno)
    print(f"Ha sido añadido el alumno {nombre} {apellidos}.")

def eliminar_alumno(nif):
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            lista_alumnos.remove(alumno)
            print(f"El alumno con NIF {nif} ha sido eliminado.")
            return
    print(f"No se encontró ningún alumno con NIF {nif}.")

def modificar_alumno(nif):
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            _menu_modificar_alumno(alumno)
            print(f"El alumno con NIF {nif} ha sido modificado.")
            return
    print(f"No se encontró ningún alumno con NIF {nif}.")

def mostrar_alumno_por_nif(nif):
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre} {alumno.apellidos}, Teléfono: {alumno.telefono}, Email: {alumno.email}, Aprobado: {alumno.aprobado}")
            return
    print(f"No se encontró ningún alumno con NIF {nif}.")

def mostrar_alumno_por_email(email):
    for alumno in lista_alumnos:
        if alumno.email == email:
            print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre} {alumno.apellidos}, Teléfono: {alumno.telefono}, Email: {alumno.email}, Aprobado: {alumno.aprobado}")
            return
    print(f"No se encontró ningún alumno con Email: {email}.")

def mostrar_todos_los_alumnos():
    for alumno in lista_alumnos:
        print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre} {alumno.apellidos}, Teléfono: {alumno.telefono}, Email: {alumno.email}, Aprobado: {alumno.aprobado}")

def aprobar_alumno(nif):
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            alumno.aprobar()
            print(f"El alumno con NIF {nif} ha sido aprobado.")
            return
    print(f"No se encontró ningún alumno con NIF {nif}.")

def suspender_alumno(nif):
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            alumno.suspender()
            print(f"El alumno con NIF {nif} ha sido suspendido.")
            return
    print(f"No se encontró ningún alumno con NIF {nif}.")

def mostrar_los_alumnos_aprobados():
    for alumno in lista_alumnos:
        if alumno.aprobado == True:
            print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre} {alumno.apellidos}, Teléfono: {alumno.telefono}, Email: {alumno.email}, Aprobado: {alumno.aprobado}")

def mostrar_los_alumnos_suspendidos():
    for alumno in lista_alumnos:
        if alumno.aprobado == False:
            print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre} {alumno.apellidos}, Teléfono: {alumno.telefono}, Email: {alumno.email}, Aprobado: {alumno.aprobado}")

def _menu_modificar_alumno(alumno):
    print("(1) Modificar NIF")
    print("(2) Modificar nombre")
    print("(3) Modificar apellidos")
    print("(4) Modificar telefono")
    print("(5) Modificar Email")
    opcion = input("Seleccione una opción: ").strip().upper()
    if opcion == "1":
        nif = input("Nuevo NIF del alumno: ")
        alumno.nif = nif
    elif opcion == "2":
        nombre = input("Nuevo nombre del alumno: ")
        alumno.nombre = nombre
    elif opcion == "3":
        apellidos = input("Nuevo apellido del alumno: ")
        alumno.apellidos = apellidos
    elif opcion == "4":
        telefono = input("Nuevo teléfono del alumno: ")
        alumno.telefono = telefono
    elif opcion == "5":
        email = input("Nuevo Email del alumno: ")
        alumno.email = email