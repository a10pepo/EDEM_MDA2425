import re

class Alumno:
    def __init__(self, nif, nombre, apellidos, telefono, email, aprobado=False):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado

    def mostrar_datos(self):
        estado = "Aprobado" if self.aprobado else "Suspendido"
        print(f"NIF: {self.nif}, Nombre: {self.nombre} {self.apellidos}, "
              f"Teléfono: {self.telefono}, Email: {self.email}, Estado: {estado}")


class GestionAlumnos:
    def __init__(self):
        self.alumnos = []

    def validar_email(self, email):
        patron_email = r"[^@]+@[^@]+\.[^@]+"
        if re.match(patron_email, email):
            return True
        else:
            print("Formato de email inválido. Asegúrate de que contenga un '@' y un dominio.")
            return False

    def añadir_alumno(self):
        nif = input("Introduce NIF: ")
        nombre = input("Introduce nombre: ")
        apellidos = input("Introduce apellidos: ")
        telefono = input("Introduce teléfono: ")

        while True:
            email = input("Introduce email: ")
            if self.validar_email(email):
                break

        alumno = Alumno(nif, nombre, apellidos, telefono, email)
        self.alumnos.append(alumno)
        print("Alumno añadido correctamente.")

    def eliminar_alumno_por_nif(self):
        nif = input("Introduce el NIF del alumno que deseas eliminar: ")
        for alumno in self.alumnos:
            if alumno.nif == nif:
                self.alumnos.remove(alumno)
                print("Alumno eliminado correctamente.")
                return
        print("Alumno no encontrado.")

    def actualizar_alumno_por_nif(self):
        nif = input("Introduce el NIF del alumno que deseas actualizar: ")
        for alumno in self.alumnos:
            if alumno.nif == nif:
                alumno.nombre = input(f"Introduce nuevo nombre (actual: {alumno.nombre}): ")
                alumno.apellidos = input(f"Introduce nuevos apellidos (actual: {alumno.apellidos}): ")
                alumno.telefono = input(f"Introduce nuevo teléfono (actual: {alumno.telefono}): ")

                # Validar el nuevo email
                while True:
                    email = input(f"Introduce nuevo email (actual: {alumno.email}): ")
                    if self.validar_email(email):
                        alumno.email = email
                        break

                print("Datos actualizados correctamente.")
                return
        print("Alumno no encontrado.")

    def mostrar_alumno_por_nif(self):
        nif = input("Introduce el NIF del alumno que deseas consultar: ")
        for alumno in self.alumnos:
            if alumno.nif == nif:
                alumno.mostrar_datos()
                return
        print("Alumno no encontrado.")

    def mostrar_alumno_por_email(self):
        email = input("Introduce el email del alumno que deseas consultar: ")
        for alumno in self.alumnos:
            if alumno.email == email:
                alumno.mostrar_datos()
                return
        print("Alumno no encontrado.")

    def listar_todos_los_alumnos(self):
        if not self.alumnos:
            print("No hay alumnos en la lista.")
        else:
            for alumno in self.alumnos:
                alumno.mostrar_datos()

    def aprobar_alumno_por_nif(self):
        nif = input("Introduce el NIF del alumno que deseas aprobar: ")
        for alumno in self.alumnos:
            if alumno.nif == nif:
                alumno.aprobado = True
                print(f"El alumno {alumno.nombre} ha sido aprobado.")
                return
        print("Alumno no encontrado.")

    def suspender_alumno_por_nif(self):
        nif = input("Introduce el NIF del alumno que deseas suspender: ")
        for alumno in self.alumnos:
            if alumno.nif == nif:
                alumno.aprobado = False
                print(f"El alumno {alumno.nombre} ha sido suspendido.")
                return
        print("Alumno no encontrado.")

    def mostrar_alumnos_aprobados(self):
        print("\nAlumnos Aprobados:")
        aprobados = [alumno for alumno in self.alumnos if alumno.aprobado]
        if aprobados:
            for alumno in aprobados:
                alumno.mostrar_datos()
        else:
            print("No hay alumnos aprobados.")

    def mostrar_alumnos_suspendidos(self):
        print("\nAlumnos Suspendidos:")
        suspendidos = [alumno for alumno in self.alumnos if not alumno.aprobado]
        if suspendidos:
            for alumno in suspendidos:
                alumno.mostrar_datos()
        else:
            print("No hay alumnos suspendidos.")

    def finalizar_programa(self):
        print("Finalizando programa. ¡Adiós!")
        exit()


def mostrar_menu():
    print("\n*** GESTIÓN DE ALUMNOS ***")
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


def main():
    gestion = GestionAlumnos()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip().upper()

        if opcion == "1":
            gestion.añadir_alumno()
        elif opcion == "2":
            gestion.eliminar_alumno_por_nif()
        elif opcion == "3":
            gestion.actualizar_alumno_por_nif()
        elif opcion == "4":
            gestion.mostrar_alumno_por_nif()
        elif opcion == "5":
            gestion.mostrar_alumno_por_email()
        elif opcion == "6":
            gestion.listar_todos_los_alumnos()
        elif opcion == "7":
            gestion.aprobar_alumno_por_nif()
        elif opcion == "8":
            gestion.suspender_alumno_por_nif()
        elif opcion == "9":
            gestion.mostrar_alumnos_aprobados()
        elif opcion == "10":
            gestion.mostrar_alumnos_suspendidos()
        elif opcion == "X":
            gestion.finalizar_programa()
        else:
            print("Opción no válida. Inténtalo de nuevo.")


main()
