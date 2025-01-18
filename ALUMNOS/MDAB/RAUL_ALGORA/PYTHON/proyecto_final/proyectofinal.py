class Alumno:
    NIF : str
    Nombre: str
    Apellidos: str
    Telefono: str
    Email: str
    Aprobado: bool
    def __init__(self, NIF: str, Nombre: str, Apellidos: str, Telefono: str, Email: str, Aprobado:bool):
        self.NIF= NIF
        self.Nombre = Nombre
        self.Apellidos= Apellidos
        self.Telefono= Telefono
        self.Email= Email
        self.Aprobado = Aprobado

    def añadir_alumno(self, lista_alumnos):
        self.NIF = input('Cual es el NIF del alumno?')
        self.Nombre = input('Cual es el Nombre del alumno?')
        self.Apellidos = input('Cuales son los apellidos del alumno?')
        self.Telefono = input('¿Cuál es el teléfono del alumno? ')
        self.Email = input('¿Cuál es el email del alumno? ')
        self.Aprobado = False

        lista_alumnos.append(self)
        print(f"Alumno {self.Nombre} {self.Apellidos} añadido exitosamente.")

    

    def eliminar_alumno(self, lista_alumnos, NIF_eliminar:str):
        for alumno in lista_alumnos:
            if NIF_eliminar == alumno.NIF:
                lista_alumnos.remove(alumno)
                print(F'Alumno con NIF {NIF_eliminar} eliminado.')
    
    
    def actualizar(self, lista_alumnos, NIF_actualizar: str):
        for alumno in lista_alumnos:
            if NIF_actualizar == alumno.NIF:
                print(f'Alumno encontrado: {alumno.Nombre} {alumno.Apellidos}')

                alumno.Nombre = input(f'Nuevo nombre (actual: {alumno.Nombre}): ') or alumno.Nombre
                alumno.Apellidos = input(f"Nuevos apellidos (actual: {alumno.Apellidos}): ") or alumno.Apellidos
                alumno.Telefono = input(f"Nuevo teléfono (actual: {alumno.Telefono}): ") or alumno.Telefono
                alumno.Email = input(f"Nuevo email (actual: {alumno.Email}): ") or alumno.Email

                
                print(f"Datos del alumno {alumno.Nombre} {alumno.Apellidos} actualizados exitosamente.")
                return  
            
        print(f"No se encontró un alumno con NIF {NIF_actualizar}.")

    def mostrar_datos_NIF(self, lista_alumnos, NIF_mostrar: str):
        for alumno in lista_alumnos:
            if NIF_mostrar == alumno.NIF:
                print(f'El NIF del alumno es {alumno.NIF}')
                print(f'El nombre del alumno es {alumno.Nombre}')
                print(f'Los apellidos del alumno son {alumno.Apellidos}')
                print(f'El teléfono del alumno es {alumno.Telefono}')
                print(f'El email del alumno es {alumno.Email}')
                print(f'El estado del alumno es: {"Aprobado" if alumno.Aprobado else "Suspendido"}')
                return  
    
        print(f"No se encontró un alumno con NIF {NIF_mostrar}.")

    def mostrar_datos_mail(self, lista_alumnos, mail_mostrar: str):
        for alumno in lista_alumnos:
            if mail_mostrar == alumno.Email:
                print(f'El NIF del alumno es {alumno.NIF}')
                print(f'El nombre del alumno es {alumno.Nombre}')
                print(f'Los apellidos del alumno son {alumno.Apellidos}')
                print(f'El teléfono del alumno es {alumno.Telefono}')
                print(f'El email del alumno es {alumno.Email}')
                print(f'El estado del alumno es: {"Aprobado" if alumno.Aprobado else "Suspendido"}')
                return  
    
        print(f"No se encontró un alumno con NIF {mail_mostrar}.")

    def listar(self, lista_alumnos):
        for alumno in lista_alumnos:
            print(f'Nombre: {alumno.Nombre} // NIF: {alumno.NIF}')


    def aprobar_NIF(self, lista_alumnos, aprobar_NIF: str):
        for alumno in lista_alumnos:
            if aprobar_NIF == alumno.NIF:
                alumno.Aprobado = True
                print(f'El alumno {alumno.Nombre} {alumno.Apellido} ha sido aprobado')
                return
    

    def suspender_NIF(self, lista_alumnos, suspender_NIF: str):
        for alumno in lista_alumnos:
            if suspender_NIF == alumno.NIF:
                alumno.Aprobado = False
                print(f'El alumno {alumno.Nombre} {alumno.Apellido} ha sido suspendido')
                return
    
    def mostrar_aprobados(self, lista_alumnos):
        aprobados_encontrados = False
        for alumno in lista_alumnos:
            if alumno.Aprobado:
                print(f'El alumno {alumno.Nombre} esta aprobado')
                aprobados_encontrados = True
            if not aprobados_encontrados: 
                print('No hay alumnos aprobados')

    def mostrar_suspensos(self, lista_alumnos):
        suspensos_encontrados = False  
        for alumno in lista_alumnos:
            if not alumno.Aprobado:  
                print(f'El alumno {alumno.Nombre} {alumno.Apellidos} está suspendido.')
                suspensos_encontrados = True  

            if not suspensos_encontrados:  
                print("No hay alumnos suspendidos.")



lista_alumnos = []

while True:
    print("\nMenú de opciones:")
    print('1. Añadir alumno')
    print('2. Eliminar alumno por NIF')
    print('3. Actualizar datos de alumno por NIF')
    print('4. Mostrar datos de un alumno por NIF')
    print('5. Mostrar datos de un alumno por Email')
    print('6. Listar TODOS los alumnos')
    print('7. Aprobar alumno por NIF')
    print('8. Suspender alumno por NIF')
    print('9. Mostrar alumnos aprobados')
    print('10. Mostrar alumnos suspendidos')
    print('X. Salir')

    opcion = input('Elige una opción: ')

    if opcion == '1':
        nuevo_alumno = Alumno("", "", "", "", "", False)
        nuevo_alumno.añadir_alumno(lista_alumnos)

    elif opcion == '2':
        NIF_eliminar = input('Escribe el NIF del alumno a eliminar: ')
        alumno = Alumno("", "", "", "", "", False)
        alumno.eliminar_alumno(lista_alumnos, NIF_eliminar)

    elif opcion == '3':
        NIF_actualizar = input('Escribe el NIF del alumno a actualizar: ')
        alumno = Alumno("", "", "", "", "", False)
        alumno.actualizar(lista_alumnos, NIF_actualizar)

    elif opcion == '4':
        NIF_mostrar = input('Escribe el NIF del alumno a mostrar: ')
        alumno = Alumno("", "", "", "", "", False)
        alumno.mostrar_datos_NIF(lista_alumnos, NIF_mostrar)

    elif opcion == '5':
        mail_mostrar = input('Escribe el email del alumno a mostrar: ')
        alumno = Alumno("", "", "", "", "", False)
        alumno.mostrar_datos_mail(lista_alumnos, mail_mostrar)

    elif opcion == '6':
        alumno = Alumno("", "", "", "", "", False)
        alumno.listar(lista_alumnos)

    elif opcion == '7':
        NIF_aprobar = input('Escribe el NIF del alumno a aprobar: ')
        alumno = Alumno("", "", "", "", "", False)
        alumno.aprobar_NIF(lista_alumnos, NIF_aprobar)

    elif opcion == '8':
        NIF_suspender = input('Escribe el NIF del alumno a suspender: ')
        alumno = Alumno("", "", "", "", "", False)
        alumno.suspender_NIF(lista_alumnos, NIF_suspender)

    elif opcion == '9':
        alumno = Alumno("", "", "", "", "", False)
        alumno.mostrar_aprobados(lista_alumnos)

    elif opcion == '10':
        alumno = Alumno("", "", "", "", "", False)
        alumno.mostrar_suspensos(lista_alumnos)

    elif opcion.upper() == 'X':
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, elige una opción correcta.")