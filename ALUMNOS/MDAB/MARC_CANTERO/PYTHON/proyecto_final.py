# Programa para gestionar la cartera de alumnos

# Lista para almacenar los alumnos
alumnos = []

# Función para mostrar el menú
def mostrar_menu():
    print("\nOpciones del programa:")
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

# Función para añadir un alumno
def añadir_alumno():
    nif = input("Introduce el NIF del alumno: ")
    nombre = input("Introduce el nombre del alumno: ")
    apellidos = input("Introduce los apellidos del alumno: ")
    telefono = input("Introduce el teléfono del alumno: ")
    email = input("Introduce el email del alumno: ")
    aprobado = False  # Por defecto, el alumno no está aprobado
    alumnos.append({
        "NIF": nif,
        "Nombre": nombre,
        "Apellidos": apellidos,
        "Teléfono": telefono,
        "Email": email,
        "Aprobado": aprobado
    })
    print(f"Alumno con NIF {nif} añadido correctamente.")

# Función para eliminar un alumno por NIF
def eliminar_alumno():
    nif = input("Introduce el NIF del alumno a eliminar: ")
    global alumnos
    alumnos = [alumno for alumno in alumnos if alumno["NIF"] != nif]
    print(f"Alumno con NIF {nif} eliminado, si existía.")

# Función para actualizar datos de un alumno por NIF
def actualizar_alumno():
    nif = input("Introduce el NIF del alumno a actualizar: ")
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            print("Introduce los nuevos datos (deja en blanco para no cambiar):")
            alumno["Nombre"] = input(f"Nombre actual ({alumno['Nombre']}): ") or alumno["Nombre"]
            alumno["Apellidos"] = input(f"Apellidos actuales ({alumno['Apellidos']}): ") or alumno["Apellidos"]
            alumno["Teléfono"] = input(f"Teléfono actual ({alumno['Teléfono']}): ") or alumno["Teléfono"]
            alumno["Email"] = input(f"Email actual ({alumno['Email']}): ") or alumno["Email"]
            print(f"Datos del alumno con NIF {nif} actualizados.")
            return
    print(f"No se encontró un alumno con NIF {nif}.")

# Función para mostrar datos de un alumno por NIF
def mostrar_alumno_por_nif():
    nif = input("Introduce el NIF del alumno: ")
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            print(alumno)
            return
    print(f"No se encontró un alumno con NIF {nif}.")

# Función para mostrar datos de un alumno por Email
def mostrar_alumno_por_email():
    email = input("Introduce el Email del alumno: ")
    for alumno in alumnos:
        if alumno["Email"] == email:
            print(alumno)
            return
    print(f"No se encontró un alumno con Email {email}.")

# Función para listar todos los alumnos
def listar_alumnos():
    if alumnos:
        for alumno in alumnos:
            print(alumno)
    else:
        print("No hay alumnos en la lista.")

# Función para aprobar un alumno por NIF
def aprobar_alumno():
    nif = input("Introduce el NIF del alumno a aprobar: ")
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            alumno["Aprobado"] = True
            print(f"Alumno con NIF {nif} aprobado.")
            return
    print(f"No se encontró un alumno con NIF {nif}.")

# Función para suspender un alumno por NIF
def suspender_alumno():
    nif = input("Introduce el NIF del alumno a suspender: ")
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            alumno["Aprobado"] = False
            print(f"Alumno con NIF {nif} suspendido.")
            return
    print(f"No se encontró un alumno con NIF {nif}.")

# Función para mostrar alumnos aprobados
def mostrar_aprobados():
    aprobados = [alumno for alumno in alumnos if alumno["Aprobado"]]
    if aprobados:
        for alumno in aprobados:
            print(alumno)
    else:
        print("No hay alumnos aprobados.")

# Función para mostrar alumnos suspensos
def mostrar_suspensos():
    suspensos = [alumno for alumno in alumnos if not alumno["Aprobado"]]
    if suspensos:
        for alumno in suspensos:
            print(alumno)
    else:
        print("No hay alumnos suspensos.")

# Función principal
def main():
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
            mostrar_aprobados()
        elif opcion == "10":
            mostrar_suspensos()
        elif opcion.upper() == "X":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

# Ejecutar el programa
if __name__ == "__main__":
    main()