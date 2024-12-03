
class Alumno:
    nif:str
    nombre: str
    apellidos: str
    telefono:str
    email: str
    aprobado: bool

    def __init__(self, nif:str, nombre:str, apellidos:str, telefono:str, email:str, aprobado:bool):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado

    def mostrar_alumnos(self):
        if self.aprobado:
            estado = "Aprobado"
        else: 
            estado = "Suspendido"
        return (f"NIF: {self.nif}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, "
        f"Telefono: {self.telefono}, Email: {self.email}, Estado: {estado}")
    
class Lista_Alumnos():
    def __init__(self):
        self.alumnos = []

    def añadir_alumno(self):
        nif = input("Introduce tu NIF: ")
        nombre = input("Introduce tu nombre: ")
        apellidos = input("Introduce tus apellidos: ")
        telefono = input("Introduce tu telefono: ")
        email = input("Introduce tu email: ")
        aprobado = input("Está aprobado? [s/n]: ").lower() == "s"

        alumno = Alumno(nif, nombre, apellidos, telefono, email, aprobado)
        self.alumnos.append(alumno)
        print(f"El alumno {alumno.nombre} {alumno.apellidos}, se ha agregado correctamente")


    def eliminar_alumno_nif(self):
        nif = input("Introduce el NIF del alumno que deseas eliminar: ")
        for alumno in self.alumnos:
            if alumno.nif == nif:
                self.alumnos.remove(alumno)
                print(f"El alumno con NIF {alumno.nif} ha sido eliminado")
                return
            else:
                print("El NIF introducido no corresponde con ningun registro")


    def actualizar_datos_nif(self):
        nif = input("Introduzca el NIF que quiere actualizar: ")
        for alumno in self.alumnos:
            if alumno.nif == nif:
                alumno.nombre = input(f"Introduce el nuevo nombre (el actual es {alumno.nombre}) : ")
                alumno.apellido = input(f"Introduce los apellidos nuevos (los actuales son {alumno.apellidos}):  ")
                alumno.telefono = input(f"Introduce el nuevo telefono (el actual es {alumno.telefono}): ")
                alumno.email = input(f"Introduce el nuevo email (el actual es {alumno.email}): ")
                print("Datos actualizados correctamente!")
                return
                
        print("El NIF introducido no corresponde con ningun registro en la base de datos")

    def mostrar_alumno_nif(self):
        nif = input("Introduzca el NIF que quiere consultar: ")
        for alumno in self.alumnos:
            if alumno.nif == nif:
                print(alumno.mostrar_alumnos())
                break
        else:  
            print("El NIF introducido no corresponde con ningun registro en la base de datos")

    def mostrar_alumno_email(self):
        email = input("Introduzca el Email que quiere consultar: ")
        for alumno in self.alumnos:
            if alumno.email == email:
                print(alumno.mostrar_alumnos())
                break
        else:
            print("El Email introducido no corresponde con ningun registro en la base de datos")

    def mostrar_todos_alumnos(self):
        if not self.alumnos:  
            print("No hay alumnos registrados")
        else:
            print("Lista de todos los alumnos:")
            for alumno in self.alumnos:
                print(alumno.mostrar_alumnos())

    def mostrar_aprobados(self):
        print("Alumnos aprobados:")
        aprobados = [alumno for alumno in self.alumnos if alumno.aprobado]
        if aprobados:
            for alumno in aprobados:
                print(alumno.mostrar_alumnos())
        else:
            print("No hay alumnos aprobados")

    def mostrar_suspensos(self):
        print("Alumnos suspensos:")
        suspensos = [alumno for alumno in self.alumnos if not alumno.aprobado]
        if suspensos:
            for alumno in suspensos:
                print(alumno.mostrar_alumnos())
        else:
            print("No hay alumnos suspensos")
    
    def salir_menu(self):
        print("Saliendo del programa...")
        exit()



def mostrar_menu():
    print("GESTIÓN ALUMNOS")
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


def aplicacion():
    gestion = Lista_Alumnos()
    while True: 
        mostrar_menu()
        opcion = input("Elige que quieres hacer: ").strip().upper()

        if opcion == "1":
            gestion.añadir_alumno()
        elif opcion == "2":
            gestion.eliminar_alumno_nif()
        elif opcion == "3":
            gestion.actualizar_datos_nif()
        elif opcion == "4":
            gestion.mostrar_alumno_nif()
        elif opcion == "5":
            gestion.mostrar_alumno_email()
        elif opcion == "6":
            gestion.mostrar_todos_alumnos()
        elif opcion == "7":
            gestion.aprobar_alumno_nif()
        elif opcion == "8":
            gestion.suspender_alumno_nif()
        elif opcion == "9":
            gestion.mostrar_aprobados()
        elif opcion == "10":
            gestion.mostrar_suspensos()
        elif opcion == "X":
            gestion.salir_menu()
        else:
            print("Opción no valida, por favor pulsa la opción que desees.")


aplicacion()



                






