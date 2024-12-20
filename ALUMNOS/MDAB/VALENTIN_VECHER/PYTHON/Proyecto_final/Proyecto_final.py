import time
import sys

class Alumno:
    def __init__(self, nif, nombre, primer_apellido, segundo_apellido, telefono, email, aprobado=True):
        self.nif=nif
        self.nombre=nombre
        self.primer_apellido=primer_apellido
        self.segundo_appellido=segundo_apellido
        self.telefono=telefono
        self.email=email
        self.aprobado=aprobado

    def __str__(self):
        estado='Aprobado' if self.aprobado else 'Suspenso'
        return (f'''El alumno con NIF {self.nif}, es {self.nombre} {self.primer_apellido} {self.segundo_appellido}, con el numero de teléfono: {self.telefono}, email: {self.email}. Y su estado es de: {self.aprobado}''')
    
class Gestion_Alumnos:
    def __init__(self):
        self.alumnos= []

    def añadir_alumnos(self):
        nif= input('Ingresar el NIF del alumno de nuevo ingreso: ')
        nombre= input('Ingresar el nombre del alumno de nuevo ingreso: ')
        primer_apellido= input('Ingresar el primer apellido del alumno de nuevo ingreso: ')
        segundo_apellido= input('Ingresar el segundo apellido del alumno de nuevo ingreso: ')
        telefono= input('Ingresar el teléfono del alumno de nuevo ingreso: ')
        email= input('Ingresar el emial del alumno de nuevo ingreso: ')
        self.alumnos.append(Alumno(nif,nombre,primer_apellido,segundo_apellido,telefono,email))
        print('El alumno ya se ha registrado en nuestra base de datos, gracias.')

    def eliminar_alumno_por_nif(self):
        nif= input('Ingresar el NIF del alumno: ')
        self.alumnos=[alumno for alumno in self.alumnos if alumno.nif !=nif]
        print('El alumno ha sido eliminado.')

    def actualizar_datos_por_nif(self):
        nif= input('Ingresar el NIF del alumno: ')
        for alumno in self.alumnos:
                if alumno.nif==nif:
                    alumno.nombre=input(f'Introduce el nuevo nombre del alumno con NIF {nif}: ')
                    alumno.primer_apellido=input(f'Introduce el primer apellido el alumno con NIF {nif}: ')
                    alumno.segundo_apellido=input(f'Introduce el segundo apellido del alumno con NIF {nif}: ')
                    alumno.telefono=input(f'Introduce el telefono del alumno con NIF {nif}: ')
                    alumno.email=input(f'Introduce el email del alumno con NIF {nif}: ')
                    print('actualización completada con éxito')
                    return
        print('alumno no encontrado')

    def mostrar_datos_por_nif(self):
        nif= input('Ingresar el NIF del alumno: ')
        for alumno in self.alumnos:
            if alumno.nif== nif:
                print(alumno)
            return 
        print('Alumno no encontrado')
    
    def mostrar_datos_por_email(self):
        email=input('Ingresa el email del alumno: ')
        for alumno in self.alumnos:
            if alumno.email==email:
                print(alumno)
            return
        print('El alumno no ha sido encontrado, pon un mail correcto.')

    def listar_todos_alumnos(self):
        if not self.alumnos:
            print('No hay alumnos registrados.')
        for alumno in self.alumnos:
            print(alumno)

    def aprobar_alumno_por_nif(self):
        nif= input('Ingresar el NIF del alumno: ')
        for alumno in self.alumnos:
            if alumno.nif==nif:
                alumno.aprobado=True
                print(f'El alumno ahora está aprobado')
                return 
        print('El alumno no ha sido encontrado, marca bien el NIF')

    def suspender_alumno_por_nif(self):
        nif= input('Ingresar el NIF del alumno: ')
        for alumno in self.alumnos:
            if alumno.nif==nif:
                alumno.aprobado=False
                print(f'El alumno ahora está suspendido')
                return
        print('El alumno no ha sido encontrado, marca bien el NIF')

    def mostrar_alumnos_aprobados(self):
        aprobados=[alumno for alumno in self.alumnos if  alumno.aprobado]
        if not aprobados:
            print('No hay alumnos aprobados')
        else:
            for alumno in aprobados:
                print(alumno)
    
    def mostrar_alumnos_suspendidos(self):
        suspendidos=[alumno for alumno in self.alumnos if not alumno.aprobado]
        if not suspendidos:
            print('No hay alumnos suspendidos')
        else:
            for alumno in suspendidos:
                print(alumno)

    def menu(self):
        while True:
            print('')
            print("Bienvenido de nuevo al sistema de Alumnado Interactivo: ")
            print('(1) Añadir un alumno nuevo.')
            print('(2) Eliminar alumno por NIF.')
            print('(3) Actualizar datos de un alumno por NIF.')
            print('(4) Mostrar datos de un alumno por NIF.')
            print('(5) Mostrar datos de un alumno por Email.')
            print('(6) Listar TODOS os alumnos.')
            print('(7) Aprobar Alumno por NIF.')
            print('(8) Suspender Alumno por NIF.')
            print('(9) Mostrar alumnos aprobados.')
            print('(10) Mostrar alumnos suspensos.')
            print('(X) Finalizar Programa.')
            seleccionar=input('Seleccione la acción que desee: ').strip().upper()

            if seleccionar=='1':
                self.añadir_alumnos()
            elif seleccionar=='2':
                self.eliminar_alumno_por_nif()
            elif seleccionar=='3':
                self.actualizar_datos_por_nif()
            elif seleccionar=='4':
                self.mostrar_datos_por_nif()
            elif seleccionar=='5':
                self.mostrar_datos_por_email()
            elif seleccionar=='6':
                self.listar_todos_alumnos()
            elif seleccionar=='7':
                self.aprobar_alumno_por_nif()
            elif seleccionar=='8':
                self.suspender_alumno_por_nif()
            elif seleccionar=='9':
                self.mostrar_alumnos_aprobados()
            elif seleccionar=='10':
                self.mostrar_alumnos_suspendidos()
            elif seleccionar=='X':
                print('Cerrando el programa... Deseamos verle de nuevo pronto')
                print("Cerrando el programa:")
                duracion=2.5
                longitud=50
                for i in range(longitud + 1):
                    time.sleep(duracion / longitud)  # Simula el tiempo de carga
                    porcentaje = (i / longitud) * 100
                    barra = "_" * i + " " * (longitud - i)
                    sys.stdout.write(f"\r[{barra}] {porcentaje:.2f}%")
                    sys.stdout.flush()
                break
            else:
                print('Opción no valida, tan solo debe seleccionar los valores que salen entre paréntesis. Todos los demás no serán válidos')

gestion= Gestion_Alumnos()
gestion.menu()

        





        



