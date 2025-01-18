class Alumno:
    def __init__(self, nif, nombre, apellidos, telefono, email, aprobado=False):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado

    def __repr__(self):
        return (f"NIF: {self.nif}, Nombre: {self.nombre} {self.apellidos}, Teléfono: {self.telefono}, "
                f"Email: {self.email}, Aprobado: {'Sí' if self.aprobado else 'No'}")

def mostrar_menu():
    print("""
    Opciones:
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

def main():
    alumnos = {}

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip().upper()

        if opcion == "1":
            nif = input("Introduce el NIF del alumno: ")
            nombre = input("Introduce el nombre del alumno: ")
            apellidos = input("Introduce los apellidos del alumno: ")
            telefono = input("Introduce el teléfono del alumno: ")
            email = input("Introduce el email del alumno: ")
            alumnos[nif] = Alumno(nif, nombre, apellidos, telefono, email)
            print("Alumno añadido exitosamente.")

        elif opcion == "2":
            nif = input("Introduce el NIF del alumno a eliminar: ")
            if nif in alumnos:
                del alumnos[nif]
                print("Alumno eliminado exitosamente.")
            else:
                print("Alumno no encontrado.")

        elif opcion == "3":
            nif = input("Introduce el NIF del alumno a actualizar: ")
            if nif in alumnos:
                nombre = input("Introduce el nuevo nombre (deja en blanco para mantener el actual): ")
                apellidos = input("Introduce los nuevos apellidos (deja en blanco para mantener los actuales): ")
                telefono = input("Introduce el nuevo teléfono (deja en blanco para mantener el actual): ")
                email = input("Introduce el nuevo email (deja en blanco para mantener el actual): ")

                if nombre:
                    alumnos[nif].nombre = nombre
                if apellidos:
                    alumnos[nif].apellidos = apellidos
                if telefono:
                    alumnos[nif].telefono = telefono
                if email:
                    alumnos[nif].email = email

                print("Datos actualizados exitosamente.")
            else:
                print("Alumno no encontrado.")

        elif opcion == "4":
            nif = input("Introduce el NIF del alumno: ")
            alumno = alumnos.get(nif)
            if alumno:
                print(alumno)
            else:
                print("Alumno no encontrado.")

        elif opcion == "5":
            email = input("Introduce el email del alumno: ")
            encontrados = [a for a in alumnos.values() if a.email == email]
            if encontrados:
                for alumno in encontrados:
                    print(alumno)
            else:
                print("Alumno no encontrado.")

        elif opcion == "6":
            if alumnos:
                for alumno in alumnos.values():
                    print(alumno)
            else:
                print("No hay alumnos registrados.")

        elif opcion == "7":
            nif = input("Introduce el NIF del alumno a aprobar: ")
            if nif in alumnos:
                alumnos[nif].aprobado = True
                print("Alumno aprobado.")
            else:
                print("Alumno no encontrado.")

        elif opcion == "8":
            nif = input("Introduce el NIF del alumno a suspender: ")
            if nif in alumnos:
                alumnos[nif].aprobado = False
                print("Alumno suspendido.")
            else:
                print("Alumno no encontrado.")

        elif opcion == "9":
            aprobados = [a for a in alumnos.values() if a.aprobado]
            if aprobados:
                for alumno in aprobados:
                    print(alumno)
            else:
                print("No hay alumnos aprobados.")

        elif opcion == "10":
            suspensos = [a for a in alumnos.values() if not a.aprobado]
            if suspensos:
                for alumno in suspensos:
                    print(alumno)
            else:
                print("No hay alumnos suspensos.")

        elif opcion == "X":
            print("Finalizando programa...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()