class Alumno:
    def __init__(self, nif, nombre, apellidos, telefono, email, aprobado=False):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado

    def __str__(self):
        estado = "Aprobado" if self.aprobado else "Suspenso"
        return f"NIF: {self.nif}, Nombre: {self.nombre} {self.apellidos}, Teléfono: {self.telefono}, Email: {self.email}, Estado: {estado}"

class GestionAlumnos:
    def __init__(self):
        self.alumnos = {}

    def agregar_alumno(self):
        nif = input("Introduce el NIF: ")
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        telefono = input("Introduce el teléfono: ")
        email = input("Introduce el email: ")
        self.alumnos[nif] = Alumno(nif, nombre, apellidos, telefono, email)
        print("Alumno añadido correctamente.")

    def eliminar_alumno(self):
        nif = input("Introduce el NIF del alumno a eliminar: ")
        if nif in self.alumnos:
            del self.alumnos[nif]
            print("Alumno eliminado correctamente.")
        else:
            print("Alumno no encontrado.")

    def actualizar_alumno(self):
        nif = input("Introduce el NIF del alumno a actualizar: ")
        if nif in self.alumnos:
            nombre = input("Nuevo nombre: ") or self.alumnos[nif].nombre
            apellidos = input("Nuevos apellidos: ") or self.alumnos[nif].apellidos
            telefono = input("Nuevo teléfono: ") or self.alumnos[nif].telefono
            email = input("Nuevo email: ") or self.alumnos[nif].email
            self.alumnos[nif] = Alumno(nif, nombre, apellidos, telefono, email, self.alumnos[nif].aprobado)
            print("Alumno actualizado correctamente.")
        else:
            print("Alumno no encontrado.")

    def mostrar_alumno_por_nif(self):
        nif = input("Introduce el NIF del alumno: ")
        if nif in self.alumnos:
            print(self.alumnos[nif])
        else:
            print("Alumno no encontrado.")

    def mostrar_alumno_por_email(self):
        email = input("Introduce el email del alumno: ")
        for alumno in self.alumnos.values():
            if alumno.email == email:
                print(alumno)
                return
        print("Alumno no encontrado.")

    def listar_alumnos(self):
        for alumno in self.alumnos.values():
            print(alumno)

    def aprobar_alumno(self):
        nif = input("Introduce el NIF del alumno a aprobar: ")
        if nif in self.alumnos:
            self.alumnos[nif].aprobado = True
            print("Alumno aprobado.")
        else:
            print("Alumno no encontrado.")

    def suspender_alumno(self):
        nif = input("Introduce el NIF del alumno a suspender: ")
        if nif in self.alumnos:
            self.alumnos[nif].aprobado = False
            print("Alumno suspendido.")
        else:
            print("Alumno no encontrado.")

    def mostrar_aprobados(self):
        for alumno in self.alumnos.values():
            if alumno.aprobado:
                print(alumno)

    def mostrar_suspensos(self):
        for alumno in self.alumnos.values():
            if not alumno.aprobado:
                print(alumno)

def menu():
    gestion = GestionAlumnos()
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
        opcion = input("Elige una opción: ").strip()
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
            gestion.mostrar_aprobados()
        elif opcion == "10":
            gestion.mostrar_suspensos()
        elif opcion.upper() == "X":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
