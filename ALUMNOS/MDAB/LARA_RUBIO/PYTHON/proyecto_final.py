"""""

1. Enunciado Proyecto FInal
Una empresa de formación quiere gestionar su cartera de alumnos.

Escribe un programa que guarde una lista de alumnos. Cada Alumno dispone de los siguientes campos:

NIF (string)
Nombre (string)
Apellidos (string)
Teléfono (string)
Email (string)
Aprobado (boolean)
El programa debe mostrar las siguientes opciones por consola para que escoja el usuario:

(1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno
(2) Eliminar alumno por NIF
(3) Actualizar datos de un alumno por NIF
(4) Mostrar datos de un alumno por NIF
(5) Mostrar datos de un alumno por Email
(6) Listar TODOS os alumnos
(7) Aprobar Alumno por NIF
(8) Suspender Alumno por NIF
(9) Mostrar alumnos aprobados
(10) Mostrar alumnos suspensos
(X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X

"""
class Alumno:
    def __init__(self, nif, nombre, apellidos, telefono, email, aprobado=False):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado

    def __str__(self):
        estado = "Aprobado" if self.aprobado else "Suspendido"
        return (f"NIF: {self.nif}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, "
                f"Teléfono: {self.telefono}, Email: {self.email}, Estado: {estado}")

class GestorAlumnos:
    def __init__(self):
        self.lista_alumnos = []

    def añadir_alumno(self):
        nif = input("Introduce el NIF: ")
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        telefono = input("Introduce el teléfono: ")
        email = input("Introduce el email: ")
        alumno = Alumno(nif, nombre, apellidos, telefono, email)
        self.lista_alumnos.append(alumno)
        print(f"Alumno {nombre} {apellidos} añadido correctamente.")

    def eliminar_alumno(self):
        nif = input("Introduce el NIF del alumno a eliminar: ")
        for alumno in self.lista_alumnos:
            if alumno.nif == nif:
                self.lista_alumnos.remove(alumno)
                print(f"Alumno con NIF {nif} eliminado.")
                return
        print(f"No se encontró un alumno con NIF {nif}.")

    def actualizar_alumno(self):
        nif = input("Introduce el NIF del alumno a actualizar: ")
        for alumno in self.lista_alumnos:
            if alumno.nif == nif:
                print("Introduce los nuevos datos (deja en blanco para no cambiar):")
                alumno.nombre = input(f"Nombre ({alumno.nombre}): ") or alumno.nombre
                alumno.apellidos = input(f"Apellidos ({alumno.apellidos}): ") or alumno.apellidos
                alumno.telefono = input(f"Teléfono ({alumno.telefono}): ") or alumno.telefono
                alumno.email = input(f"Email ({alumno.email}): ") or alumno.email
                print("Alumno actualizado correctamente.")
                return
        print(f"No se encontró un alumno con NIF {nif}.")

    def mostrar_por_nif(self):
        nif = input("Introduce el NIF: ")
        for alumno in self.lista_alumnos:
            if alumno.nif == nif:
                print(alumno)
                return
        print(f"No se encontró un alumno con NIF {nif}.")

    def mostrar_por_email(self):
        email = input("Introduce el email: ")
        for alumno in self.lista_alumnos:
            if alumno.email == email:
                print(alumno)
                return
        print(f"No se encontró un alumno con email {email}.")

    def listar_todos(self):
        if not self.lista_alumnos:
            print("No hay alumnos registrados.")
        for alumno in self.lista_alumnos:
            print(alumno)

    def aprobar_alumno(self):
        nif = input("Introduce el NIF del alumno a aprobar: ")
        for alumno in self.lista_alumnos:
            if alumno.nif == nif:
                alumno.aprobado = True
                print(f"Alumno {alumno.nombre} aprobado.")
                return
        print(f"No se encontró un alumno con NIF {nif}.")

    def suspender_alumno(self):
        nif = input("Introduce el NIF del alumno a suspender: ")
        for alumno in self.lista_alumnos:
            if alumno.nif == nif:
                alumno.aprobado = False
                print(f"Alumno {alumno.nombre} suspendido.")
                return
        print(f"No se encontró un alumno con NIF {nif}.")

    def mostrar_aprobados(self):
        aprobados = [alumno for alumno in self.lista_alumnos if alumno.aprobado]
        if not aprobados:
            print("No hay alumnos aprobados.")
        for alumno in aprobados:
            print(alumno)

    def mostrar_suspensos(self):
        suspensos = [alumno for alumno in self.lista_alumnos if not alumno.aprobado]
        if not suspensos:
            print("No hay alumnos suspendidos.")
        for alumno in suspensos:
            print(alumno)

def main():
    gestor = GestorAlumnos()
    while True:
        print("\nMenú de opciones:")
        print("1. Añadir alumno")
        print("2. Eliminar alumno por NIF")
        print("3. Actualizar datos de alumno por NIF")
        print("4. Mostrar datos de un alumno por NIF")
        print("5. Mostrar datos de un alumno por Email")
        print("6. Listar TODOS los alumnos")
        print("7. Aprobar alumno por NIF")
        print("8. Suspender alumno por NIF")
        print("9. Mostrar alumnos aprobados")
        print("10. Mostrar alumnos suspendidos")
        print("X. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            gestor.añadir_alumno()
        elif opcion == "2":
            gestor.eliminar_alumno()
        elif opcion == "3":
            gestor.actualizar_alumno()
        elif opcion == "4":
            gestor.mostrar_por_nif()
        elif opcion == "5":
            gestor.mostrar_por_email()
        elif opcion == "6":
            gestor.listar_todos()
        elif opcion == "7":
            gestor.aprobar_alumno()
        elif opcion == "8":
            gestor.suspender_alumno()
        elif opcion == "9":
            gestor.mostrar_aprobados()
        elif opcion == "10":
            gestor.mostrar_suspensos()
        elif opcion.upper() == "X":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
