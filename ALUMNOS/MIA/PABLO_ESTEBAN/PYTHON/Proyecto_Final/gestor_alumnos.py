import os


class Alumno:
    def __init__(self, nif: str, nombre: str, apellidos: str, telefono: str = None, email: str = None, aprobado: bool = False):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

    def data_string(self):
        return f"{self.nombre} {self.apellidos}\n  NIF: {self.nif}\n  Telefono: {self.telefono}\n  Email: {self.email}\n  Aprobado: {self.aprobado}"
    

class App:
    def __init__(self):
        self.alumnos = []

    def start(self):
        menu = """
        -----------------------------------
            Gestor de Alumnos
        -----------------------------------
        Seleccione una opción

            1. Añadir un alumno
            2. Eliminar alumno por NIF
            3. Actualizar datos de un alumno por NIF
            4. Mostrar datos de un alumno por NIF
            5. Mostrar datos de un alumno por Email
            6. Listar TODOS os alumno
            7. Aprobar Alumno por NIF
            8. Suspender Alumno por NIF
            9. Mostrar alumno aprobados
            10. Mostrar alumno suspensos
            X. Finalizar Programa

        """
        incorrect_option = False

        while True:
            os.system("cls")
            print(menu)
            print("Opción incorrecta") if incorrect_option else None
            option = self.get_input_option()
            print()

            incorrect_option = False
            if option == "1":
                self.add_student()
            elif option == "2":
                self.remove_student_by_nif()
            elif option == "3":
                self.update_student_by_nif()
            elif option == "4":
                self.get_student_by_nif()
            elif option == "5":
                self.get_student_by_email()
            elif option == "6":
                self.list_students()
            elif option == "7":
                self.approve_student_by_nif()
            elif option == "8":
                self.suspend_student_by_nif()
            elif option == "9":
                self.list_approved_students()
            elif option == "10":
                self.list_suspended_students()
            elif option == "x":
                exit()
            else:
                incorrect_option = True
    

    # Inputs

    def get_input_option(self):
        option = input("> ").strip().lower()
        if option in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "x"]:
            return option
        return None
    
    def get_input_str(self, message: str) -> str:
        value = input(message).strip()
        return value
    
    


    # App options

    def add_student(self) -> None:
        nif = input("NIF > ")
        nombre = input("Nombre > ")
        apellidos = input("Apellidos > ")
        telefono = input("Telefono [None] > ")
        email = input("Email [None] > ")
        aprobado = input("¿Es un alumno aprobado? (Si / No) [False] > ")

        if telefono == "":
            telefono = None
        if email == "":
            email = None        
        if aprobado == "":
            aprobado = False

        student = Alumno(nif, nombre, apellidos, telefono, email, aprobado)
        self.alumnos.append(student)

        print(f"\nAlumno añadido: {student}")
        input("Presiona enter para continuar...")

    def remove_student_by_nif(self):
        nif = input("NIF >")
        student = self._get_student_by_nif(nif)
        if student is not None:
            self.alumnos.remove(student)
            print(f"Alumno eliminado: {student}")
        else:
            print(f"Alumno con nif {nif} no encontrado")
        
        input("\nPresiona enter para continuar...")

    def update_student_by_nif(self) -> None:

        nif = input("NIF > ")
        student = self._get_student_by_nif(nif)

        nif_new = input("NIF Nuevo [Previo] > ")
        nombre = input("Nombre [Previo] > ")
        apellidos = input("Apellidos [Previo] > ")
        telefono = input("Telefono [Previo] > ")
        email = input("Email [Previo] > ")
        aprobado = input("¿Es un alumno aprobado? (Si / No) [False] [Previo] > ")

        if student is None:
            print(f"Alumno con nif {nif} no encontrado")

        if nif_new is not None:
            student.nif = nif_new
        if nombre is not None:
            student.nombre = nombre
        if apellidos is not None:
            student.apellidos = apellidos
        if telefono is not None:    
            student.telefono = telefono
        if email is not None:
            student.email = email
        if aprobado is not None:
            student.aprobado = aprobado

        print(f"\nAlumno actualizado: {student}")
        input("\nPresiona enter para continuar...")
    
    def get_student_by_nif(self) -> None:
        nif = input("NIF > ")
        student = self._get_student_by_nif(nif)
        if student is not None:
            print(student.data_string())
        else:
            print(f"Alumno con nif {nif} no encontrado")
        
        input("\nPresiona enter para continuar...")

    def get_student_by_email(self) -> None:
        email = input("Email > ")
        student = self._get_student_by_email(email)
        if student is not None:
            print(student.data_string())
        else:
            print(f"Alumno con email {email} no encontrado")
        
        input("\nPresiona enter para continuar...")

    def list_students(self):
        for n, student in enumerate(self.alumnos):
            print(f"{n+1}. {student}")
        
        input("\nPresiona enter para continuar...")

    def approve_student_by_nif(self):

        nif = input("NIF > ")

        student = self._get_student_by_nif(nif)
        if student is not None:
            student.aprobado = True
            print(f"Alumno aprobado: {student}")
        else:
            print(f"Alumno con nif {nif} no encontrado")

        input("\nPresiona enter para continuar...")

    def suspend_student_by_nif(self):
        nif = input("NIF > ")
        student = self._get_student_by_nif(nif)
        if student is not None:
            student.aprobado = False
            print(f"Alumno suspendido: {student}")
        else:
            print(f"Alumno con nif {nif} no encontrado")

        input("\nPresiona enter para continuar...")

    def list_approved_students(self):
        for n, student in enumerate(self.alumnos):
            if student.aprobado:
                print(f"{n+1}. {student}")
        
        input("\nPresiona enter para continuar...")

    def list_suspended_students(self):
        for n, student in enumerate(self.alumnos):
            if not student.aprobado:
                print(f"{n+1}. {student}")
        
        input("\nPresiona enter para continuar...")


    # Private methods

    def _get_student_by_email(self, email: str) -> Alumno:
        for student in self.alumnos:
            if student.email == email:
                return student
        return None

    def _get_student_by_nif(self, nif: str) -> Alumno:
        for student in self.alumnos:
            if student.nif == nif:
                return student
        return None

if __name__ == "__main__":
    app = App()
    app.start()