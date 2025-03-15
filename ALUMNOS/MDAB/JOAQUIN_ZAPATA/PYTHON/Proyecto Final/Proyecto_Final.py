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
        return f"NIF: {self.nif}, Nombre: {self.nombre} {self.apellidos}, Teléfono: {self.telefono}, Email: {self.email}, Estado: {estado}"

class GestionAlumnos:
    def __init__(self):
        self.alumnos = []

    def añadir_alumno(self):
        nif = input("Introduce el NIF del alumno: ")
        nombre = input("Introduce el nombre del alumno: ")
        apellidos = input("Introduce los apellidos del alumno: ")
        telefono = input("Introduce el teléfono del alumno: ")
        email = input("Introduce el email del alumno: ")
        alumno = Alumno(nif, nombre, apellidos, telefono, email)
        self.alumnos.append(alumno)
        print("Alumno añadido correctamente.")

    def eliminar_alumno(self):
        nif = input("Introduce el NIF del alumno a eliminar: ")
        alumno = self.buscar_alumno_por_nif(nif)
        if alumno:
            self.alumnos.remove(alumno)
            print("Alumno eliminado correctamente.")
        else:
            print("Alumno no encontrado.")

    def actualizar_datos(self):
        nif = input("Introduce el NIF del alumno a actualizar: ")
        alumno = self.buscar_alumno_por_nif(nif)
        if alumno:
            alumno.nombre = input(f"Introduce el nuevo nombre (actual: {alumno.nombre}): ")
            alumno.apellidos = input(f"Introduce los nuevos apellidos (actual: {alumno.apellidos}): ")
            alumno.telefono = input(f"Introduce el nuevo teléfono (actual: {alumno.telefono}): ")
            alumno.email = input(f"Introduce el nuevo email (actual: {alumno.email}): ")
            print("Datos del alumno actualizados.")
        else:
            print("Alumno no encontrado.")

    def mostrar_datos_por_nif(self):
        nif = input("Introduce el NIF del alumno: ")
        alumno = self.buscar_alumno_por_nif(nif)
        if alumno:
            print(alumno)
        else:
            print("Alumno no encontrado.")

    def mostrar_datos_por_email(self):
        email = input("Introduce el email del alumno: ")
        alumno = self.buscar_alumno_por_email(email)
        if alumno:
            print(alumno)
        else:
            print("Alumno no encontrado.")

    def listar_todos_alumnos(self):
        if self.alumnos:
            for alumno in self.alumnos:
                print(alumno)
        else:
            print("No hay alumnos registrados.")

    def aprobar_alumno(self):
        nif = input("Introduce el NIF del alumno a aprobar: ")
        alumno = self.buscar_alumno_por_nif(nif)
        if alumno:
            alumno.aprobado = True
            print("Alumno aprobado correctamente.")
        else:
            print("Alumno no encontrado.")

    def suspender_alumno(self):
        nif = input("Introduce el NIF del alumno a suspender: ")
        alumno = self.buscar_alumno_por_nif(nif)
        if alumno:
            alumno.aprobado = False
            print("Alumno suspendido correctamente.")
        else:
            print("Alumno no encontrado.")

    def mostrar_alumnos_aprobados(self):
        aprobados = [alumno for alumno in self.alumnos if alumno.aprobado]
        if aprobados:
            for alumno in aprobados:
                print(alumno)
        else:
            print("No hay alumnos aprobados.")

    def mostrar_alumnos_suspensos(self):
        suspensos = [alumno for alumno in self.alumnos if not alumno.aprobado]
        if suspensos:
            for alumno in suspensos:
                print(alumno)
        else:
            print("No hay alumnos suspensos.")

    def buscar_alumno_por_nif(self, nif):
        for alumno in self.alumnos:
            if alumno.nif == nif:
                return alumno
        return None

    def buscar_alumno_por_email(self, email):
        for alumno in self.alumnos:
            if alumno.email == email:
                return alumno
        return None

def main():
    gestion = GestionAlumnos()
    
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1) Añadir un alumno")
        print("2) Eliminar alumno por NIF")
        print("3) Actualizar datos de un alumno por NIF")
        print("4) Mostrar datos de un alumno por NIF")
        print("5) Mostrar datos de un alumno por Email")
        print("6) Listar TODOS los alumnos")
        print("7) Aprobar Alumno por NIF")
        print("8) Suspender Alumno por NIF")
        print("9) Mostrar alumnos aprobados")
        print("10) Mostrar alumnos suspensos")
        print("X) Finalizar Programa")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            gestion.añadir_alumno()
        elif opcion == "2":
            gestion.eliminar_alumno()
        elif opcion == "3":
            gestion.actualizar_datos()
        elif opcion == "4":
            gestion.mostrar_datos_por_nif()
        elif opcion == "5":
            gestion.mostrar_datos_por_email()
        elif opcion == "6":
            gestion.listar_todos_alumnos()
        elif opcion == "7":
            gestion.aprobar_alumno()
        elif opcion == "8":
            gestion.suspender_alumno()
        elif opcion == "9":
            gestion.mostrar_alumnos_aprobados()
        elif opcion == "10":
            gestion.mostrar_alumnos_suspensos()
        elif opcion.upper() == "X":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")
            
main()
