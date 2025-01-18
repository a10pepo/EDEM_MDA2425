# Funciones para las operaciones de los alumnos
def agregar_alumno(alumnos):
    nif = input("NIF: ")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    aprobado = input("¿Aprobado? (s/n): ").strip().lower() == 's'
    alumno = {
        "NIF": nif,
        "Nombre": nombre,
        "Apellidos": apellidos,
        "Teléfono": telefono,
        "Email": email,
        "Aprobado": aprobado
    }
    alumnos.append(alumno)
    print("Alumno añadido correctamente.\n")

def eliminar_alumno(alumnos, nif):
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            alumnos.remove(alumno)
            print(f"Alumno con NIF {nif} eliminado.\n")
            return
    print(f"No se encontró un alumno con NIF {nif}.\n")

def actualizar_alumno(alumnos, nif):
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            print("Deja en blanco si no deseas cambiar un campo.")
            alumno["Nombre"] = input("Nuevo Nombre: ") or alumno["Nombre"]
            alumno["Apellidos"] = input("Nuevos Apellidos: ") or alumno["Apellidos"]
            alumno["Teléfono"] = input("Nuevo Teléfono: ") or alumno["Teléfono"]
            alumno["Email"] = input("Nuevo Email: ") or alumno["Email"]
            aprobado = input("¿Aprobado? (s/n): ").strip().lower()
            if aprobado:
                alumno["Aprobado"] = aprobado == 's'
            print("Alumno actualizado correctamente.\n")
            return
    print(f"No se encontró un alumno con NIF {nif}.\n")

def mostrar_alumno_por_nif(alumnos, nif):
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            print(alumno)
            return
    print(f"No se encontró un alumno con NIF {nif}.\n")

def mostrar_alumno_por_email(alumnos, email):
    for alumno in alumnos:
        if alumno["Email"] == email:
            print(alumno)
            return
    print(f"No se encontró un alumno con Email {email}.\n")

def listar_alumnos(alumnos):
    if not alumnos:
        print("No hay alumnos registrados.\n")
    else:
        for alumno in alumnos:
            print(alumno)
        print()

def aprobar_alumno(alumnos, nif):
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            alumno["Aprobado"] = True
            print(f"Alumno con NIF {nif} aprobado.\n")
            return
    print(f"No se encontró un alumno con NIF {nif}.\n")

def suspender_alumno(alumnos, nif):
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            alumno["Aprobado"] = False
            print(f"Alumno con NIF {nif} suspendido.\n")
            return
    print(f"No se encontró un alumno con NIF {nif}.\n")

def mostrar_alumnos_aprobados(alumnos):
    aprobados = [alumno for alumno in alumnos if alumno["Aprobado"]]
    if not aprobados:
        print("No hay alumnos aprobados.\n")
    else:
        for alumno in aprobados:
            print(alumno)
        print()

def mostrar_alumnos_suspendidos(alumnos):
    suspendidos = [alumno for alumno in alumnos if not alumno["Aprobado"]]
    if not suspendidos:
        print("No hay alumnos suspendidos.\n")
    else:
        for alumno in suspendidos:
            print(alumno)
        print()

# Programa principal
def main():
    alumnos = []
    while True:
        print("""
        (1) Añadir un alumno
        (2) Eliminar alumno por NIF
        (3) Actualizar datos de un alumno por NIF
        (4) Mostrar datos de un alumno por NIF
        (5) Mostrar datos de un alumno por Email
        (6) Listar TODOS los alumnos
        (7) Aprobar Alumno por NIF
        (8) Suspender Alumno por NIF
        (9) Mostrar alumnos aprobados
        (10) Mostrar alumnos suspensos
        (X) Finalizar Programa
        """)
        opcion = input("Selecciona una opción: ").strip().upper()

        if opcion == '1':
            agregar_alumno(alumnos)
        elif opcion == '2':
            nif = input("Introduce el NIF del alumno a eliminar: ")
            eliminar_alumno(alumnos, nif)
        elif opcion == '3':
            nif = input("Introduce el NIF del alumno a actualizar: ")
            actualizar_alumno(alumnos, nif)
        elif opcion == '4':
            nif = input("Introduce el NIF del alumno a mostrar: ")
            mostrar_alumno_por_nif(alumnos, nif)
        elif opcion == '5':
            email = input("Introduce el Email del alumno a mostrar: ")
            mostrar_alumno_por_email(alumnos, email)
        elif opcion == '6':
            listar_alumnos(alumnos)
        elif opcion == '7':
            nif = input("Introduce el NIF del alumno a aprobar: ")
            aprobar_alumno(alumnos, nif)
        elif opcion == '8':
            nif = input("Introduce el NIF del alumno a suspender: ")
            suspender_alumno(alumnos, nif)
        elif opcion == '9':
            mostrar_alumnos_aprobados(alumnos)
        elif opcion == '10':
            mostrar_alumnos_suspendidos(alumnos)
        elif opcion == 'X':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
