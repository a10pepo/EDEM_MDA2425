class Alumno:
    def __init__(self, nif, nombre, apellidos, telefono, email, aprobado=False):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado

    def mostrar_datos(self):
        aprobado_str = "Aprobado" if self.aprobado else "Suspenso"
        return (f"NIF: {self.nif}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, "
                f"Teléfono: {self.telefono}, Email: {self.email}, Estado: {aprobado_str}")

def mostrar_menu():
    print("\nOpciones del Programa:")
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
    print("(X) Finalizar Programa\n")

def buscar_alumno(lista_alumnos, clave, valor):
    for alumno in lista_alumnos:
        if getattr(alumno, clave) == valor:
            return alumno
    return None

def main():
    alumnos = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip().upper()
        
        if opcion == "1":
            nif = input("Ingrese NIF: ")
            nombre = input("Ingrese nombre: ")
            apellidos = input("Ingrese apellidos: ")
            telefono = input("Ingrese teléfono: ")
            email = input("Ingrese email: ")
            alumnos.append(Alumno(nif, nombre, apellidos, telefono, email))
            print("Alumno añadido con éxito.")
        
        elif opcion == "2":
            nif = input("Ingrese el NIF del alumno a eliminar: ")
            alumno = buscar_alumno(alumnos, "nif", nif)
            if alumno:
                alumnos.remove(alumno)
                print("Alumno eliminado.")
            else:
                print("Alumno no encontrado.")
        
        elif opcion == "3":
            nif = input("Ingrese el NIF del alumno a actualizar: ")
            alumno = buscar_alumno(alumnos, "nif", nif)
            if alumno:
                alumno.nombre = input("Ingrese nuevo nombre: ")
                alumno.apellidos = input("Ingrese nuevos apellidos: ")
                alumno.telefono = input("Ingrese nuevo teléfono: ")
                alumno.email = input("Ingrese nuevo email: ")
                print("Datos actualizados.")
            else:
                print("Alumno no encontrado.")
        
        elif opcion == "4":
            nif = input("Ingrese el NIF del alumno: ")
            alumno = buscar_alumno(alumnos, "nif", nif)
            if alumno:
                print(alumno.mostrar_datos())
            else:
                print("Alumno no encontrado.")
        
        elif opcion == "5":
            email = input("Ingrese el email del alumno: ")
            alumno = buscar_alumno(alumnos, "email", email)
            if alumno:
                print(alumno.mostrar_datos())
            else:
                print("Alumno no encontrado.")
        
        elif opcion == "6":
            if alumnos:
                for alumno in alumnos:
                    print(alumno.mostrar_datos())
            else:
                print("No hay alumnos en la lista.")
        
        elif opcion == "7":
            nif = input("Ingrese el NIF del alumno a aprobar: ")
            alumno = buscar_alumno(alumnos, "nif", nif)
            if alumno:
                alumno.aprobado = True
                print("Alumno aprobado.")
            else:
                print("Alumno no encontrado.")
        
        elif opcion == "8":
            nif = input("Ingrese el NIF del alumno a suspender: ")
            alumno = buscar_alumno(alumnos, "nif", nif)
            if alumno:
                alumno.aprobado = False
                print("Alumno suspendido.")
            else:
                print("Alumno no encontrado.")
        
        elif opcion == "9":
            aprobados = [alumno for alumno in alumnos if alumno.aprobado]
            if aprobados:
                for alumno in aprobados:
                    print(alumno.mostrar_datos())
            else:
                print("No hay alumnos aprobados.")
        
        elif opcion == "10":
            suspensos = [alumno for alumno in alumnos if not alumno.aprobado]
            if suspensos:
                for alumno in suspensos:
                    print(alumno.mostrar_datos())
            else:
                print("No hay alumnos suspensos.")
        
        elif opcion == "X":
            print("Finalizando programa...")
            break
        
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
