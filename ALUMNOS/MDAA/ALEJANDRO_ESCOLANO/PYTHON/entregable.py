alumnos = []

def mostrar_menu():
    print("\nOpciones:")
    print("(1) Añadir un alumno")
    print("(2) Eliminar alumno por NIF")
    print("(3) Actualizar datos de un alumno por NIF")
    print("(4) Mostrar datos de un alumno por NIF")
    print("(5) Mostrar datos de un alumno por Email")
    print("(6) Listar TODOS los alumnos")
    print("(7) Aprobar Alumno por NIF")
    print("(8) Suspender Alumno por NIF")
    print("(9) Mostrar alumnos aprobados")
    print("(10) Mostrar alumnos suspensos")
    print("(X) Finalizar Programa")

def nif_existe(nif):
    """Comprueba si un NIF existe en la lista de alumnos."""
    return any(alumno["NIF"] == nif for alumno in alumnos)

def añadir_alumno():
    nif = input("Introduce el NIF: ")
    if nif_existe(nif):
        print("El NIF ya está registrado. No se puede añadir.")
        return
    nombre = input("Introduce el Nombre: ")
    apellidos = input("Introduce los Apellidos: ")
    telefono = input("Introduce el Teléfono: ")
    email = input("Introduce el Email: ")
    aprobado = False  # Por defecto, el alumno no está aprobado
    alumnos.append({
        "NIF": nif,
        "Nombre": nombre,
        "Apellidos": apellidos,
        "Teléfono": telefono,
        "Email": email,
        "Aprobado": aprobado
    })
    print("Alumno añadido correctamente.")

def eliminar_alumno():
    nif = input("Introduce el NIF del alumno a eliminar: ")
    if not nif_existe(nif):
        print("El NIF no existe.")
        return
    global alumnos
    alumnos = [alumno for alumno in alumnos if alumno["NIF"] != nif]
    print("Alumno eliminado correctamente.")

def actualizar_alumno():
    nif = input("Introduce el NIF del alumno a actualizar: ")
    if not nif_existe(nif):
        print("El NIF no existe.")
        return
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            alumno["Nombre"] = input("Introduce el nuevo Nombre: ")
            alumno["Apellidos"] = input("Introduce los nuevos Apellidos: ")
            alumno["Teléfono"] = input("Introduce el nuevo Teléfono: ")
            alumno["Email"] = input("Introduce el nuevo Email: ")
            print("Datos actualizados correctamente.")
            return

def mostrar_alumno_por_nif():
    nif = input("Introduce el NIF del alumno: ")
    if not nif_existe(nif):
        print("El NIF no existe.")
        return
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            print(alumno)
            return

def aprobar_alumno():
    nif = input("Introduce el NIF del alumno a aprobar: ")
    if not nif_existe(nif):
        print("El NIF no existe. ")
        return
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            alumno["Aprobado"] = True
            print("Alumno aprobado.")
            return

def suspender_alumno():
    nif = input("Introduce el NIF del alumno a suspender: ")
    if not nif_existe(nif):
        print("El NIF no existe.")
        return
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            alumno["Aprobado"] = False
            print("Alumno suspendido.")
            return

def mostrar_alumnos_aprobados():
    """Muestra todos los alumnos aprobados."""
    aprobados = [alumno for alumno in alumnos if alumno["Aprobado"]]
    if not aprobados:
        print("No hay alumnos aprobados.")
    else:
        print("Alumnos aprobados:")
        for alumno in aprobados:
            print(alumno)

def mostrar_alumnos_suspensos():
    """Muestra todos los alumnos suspensos."""
    suspensos = [alumno for alumno in alumnos if not alumno["Aprobado"]]
    if not suspensos:
        print("No hay alumnos suspensos.")
    else:
        print("Alumnos suspensos:")
        for alumno in suspensos:
            print(alumno)

def mostrar_alumno_por_email():
    """Muestra los datos de un alumno por su email."""
    email = input("Introduce el Email del alumno: ")
    for alumno in alumnos:
        if alumno["Email"] == email:
            print(alumno)
            return
    print("No se encontró ningún alumno con ese Email.")

def listar_alumnos():
    """Muestra todos los alumnos registrados."""
    if not alumnos:
        print("No hay alumnos registrados.")
    else:
        print("Lista de todos los alumnos:")
        for alumno in alumnos:
            print(alumno)

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ").strip()
    if opcion == "1":
        añadir_alumno()
    elif opcion == "2":
        eliminar_alumno()
    elif opcion == "3":
        actualizar_alumno()
    elif opcion == "4":
        mostrar_alumno_por_nif()
    elif opcion == "5":
        mostrar_alumno_por_email()
    elif opcion == "6":
        listar_alumnos()
    elif opcion == "7":
        aprobar_alumno()
    elif opcion == "8":
        suspender_alumno()
    elif opcion == "9":
        mostrar_alumnos_aprobados()
    elif opcion == "10":
        mostrar_alumnos_suspensos()
    elif opcion.upper() == "X":
        break
    else:
        print("Opción no válida.")