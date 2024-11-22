class Alumno:
    def __init__(self, nif, nombre, apellidos, telefono, email, aprobado=False):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado

    def __str__(self):
        return f"NIF: {self.nif}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, Teléfono: {self.telefono}, Email: {self.email}, Aprobado: {'Sí' if self.aprobado else 'No'}"


class GestionAlumnos:
    def __init__(self):
        self.alumnos = {}

    def agregar_alumno(self):
        nif = input("Ingrese el NIF del alumno: ")
        nombre = input("Ingrese el nombre del alumno: ")
        apellidos = input("Ingrese los apellidos del alumno: ")
        telefono = input("Ingrese el teléfono del alumno: ")
        email = input("Ingrese el email del alumno: ")
        self.alumnos[nif] = Alumno(nif, nombre, apellidos, telefono, email)
        print("Alumno agregado exitosamente.")

    def eliminar_alumno(self):
        nif = input("Ingrese el NIF del alumno a eliminar: ")
        if nif in self.alumnos:
            del self.alumnos[nif]
            print("Alumno eliminado exitosamente.")
        else:
            print("Alumno no encontrado.")

    def actualizar_alumno(self):
        nif = input("Ingrese el NIF del alumno a actualizar: ")
        if nif in self.alumnos:
            nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
            apellidos = input("Nuevos apellidos (dejar vacío para no cambiar): ")
            telefono = input("Nuevo teléfono (dejar vacío para no cambiar): ")
            email = input("Nuevo email (dejar vacío para no cambiar): ")
            if nombre:
                self.alumnos[nif].nombre = nombre
            if apellidos:
                self.alumnos[nif].apellidos = apellidos
            if telefono:
                self.alumnos[nif].telefono = telefono
            if email:
                self.alumnos[nif].email = email
            print("Alumno actualizado exitosamente.")
        else:
            print("Alumno no encontrado.")

    def mostrar_alumno_por_nif(self):
        nif = input("Ingrese el NIF del alumno a mostrar: ")
        if nif in self.alumnos:
            print(self.alumnos[nif])
        else:
            print("Alumno no encontrado.")

    def mostrar_alumno_por_email(self):
        email = input("Ingrese el email del alumno a mostrar: ")
        for alumno in self.alumnos.values():
            if alumno.email == email:
                print(alumno)
                return
        print("Alumno no encontrado.")

    def listar_alumnos(self):
        if not self.alumnos:
            print("No hay alumnos registrados.")
        else:
            for alumno in self.alumnos.values():
                print(alumno)

    def aprobar_alumno(self):
        nif = input("Ingrese el NIF del alumno a aprobar: ")
        if nif in self.alumnos:
            self.alumnos[nif].aprobado = True
            print("Alumno aprobado.")
        else:
            print("Alumno no encontrado.")

    def suspender_alumno(self):
        nif = input("Ingrese el NIF del alumno a suspender: ")
        if nif in self.alumnos:
            self.alumnos[nif].aprobado = False
            print("Alumno suspendido.")
        else:
            print("Alumno no encontrado.")

    def mostrar_alumnos_aprobados(self):
        aprobados = [alumno for alumno in self.alumnos.values() if alumno.aprobado]
        if aprobados:
            for alumno in aprobados:
                print(alumno)
        else:
            print("No hay alumnos aprobados.")

    def mostrar_alumnos_suspensos(self):
        suspensos = [alumno for alumno in self.alumnos.values() if not alumno.aprobado]
        if suspensos:
            for alumno in suspensos:
                print(alumno)
        else:
            print("No hay alumnos suspensos.")

    def finalizar_programa(self):
        print("Finalizando programa.")
        exit()


def menu():
    gestion = GestionAlumnos()
    while True:
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

        opcion = input("Seleccione una opción: ").upper()
        
        if opcion == "1":
            gestion.agregar_alumno()
        elif opcion == "2":
            gestion.eliminar_alumno()
        elif opcion == "3":
            gestion.actualizar_alumno()
        elif opcion == "4":
            gestion.mostrar_alumno_por_nif()
        elif opcion == "5":
            gestion.mostrar_alumno_por_email()
        elif opcion == "6":
            gestion.listar_alumnos()
        elif opcion == "7":
            gestion.aprobar_alumno()
        elif opcion == "8":
            gestion.suspender_alumno()
        elif opcion == "9":
            gestion.mostrar_alumnos_aprobados()
        elif opcion == "10":
            gestion.mostrar_alumnos_suspensos()
        elif opcion == "X":
            gestion.finalizar_programa()
        else:
            print("Opción no válida, por favor seleccione una opción válida.")

menu()


