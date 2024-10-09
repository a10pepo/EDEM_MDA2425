class Alumno: 
    def __init__(self,nif: str, nombre: str, apellidos: str, telefono: str, email: str, aprobado: bool):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado
    
    def get_nif(self) -> str:
        return self.nif

    def get_nombre(self) -> str:
        return self.nombre

    def get_apellidos(self) -> str:
        return self.apellidos
    
    def get_telefono(self) -> str:
        return self.telefono
    
    def get_email(self) -> str:
        return self.email

    def get_aprobado(self) -> bool:
        return self.aprobado
    
    def get_alumno(self) -> str:
        return (f'''NIF: {self.nif}, Nombre: {self.nombre} {self.apellidos}, 
                Teléfono: {self.telefono}, Email: {self.email}, 
                Aprobado: {self.aprobado}''')
    
class ListaAlumnos:
    def __init__(self):
        self.lista_alumnos = []

    def agregar_alumno(self):
        nif: str = input("NIF: ")
        nombre: str = input("Nombre: ")
        apellidos: str = input("Apellidos: ")
        telefono: str = input("Telefono: ")
        email: str = input("Email: ")
        while(True):
            aux: str = input("¿Aprobado? [Y/n]: ").upper()
            if (aux == "Y"):
                aprobado: bool = True
                break
            elif (aux == "N"):
                aprobado: bool = False
                break
        self.lista_alumnos.append(Alumno(nif, nombre, apellidos, telefono, email, aprobado))

    def buscar_alumno_nif(self, nif) -> Alumno:
        for alumno in self.lista_alumnos:
            if alumno.get_nif() == nif:
                return alumno
        return None

    def buscar_alumno_email(self, email) -> Alumno:
        for alumno in self.lista_alumnos:
            if alumno.get_email() == email:
                return alumno
        return None

    def eliminar_alumno(self) -> Alumno:
        nif: str = input("NIF: ")
        alumno: Alumno = self.buscar_alumno_nif(nif)
        if(alumno != None):
            self.lista_alumnos.remove(alumno)
            print(f"Alumno con NIF: {nif} ha sido eliminado.")
        else:
            print(f"Alumno con NIF: {nif} no ha sido encontrado.")


    def  actualizar_datos(self):
        nif: str = input("NIF del alumno a modificar: ")
        alumno: Alumno = self.buscar_alumno_nif(nif)
        if (alumno != None):

            cambio: str = input(f"¿Quieres modificar el nombre del alumno con NIF: {nif}? [Y/n]:  ").upper()
            while(cambio != "Y" and cambio != "N"):
                cambio: str = input(f'''No has introducido un valor valido.
                                    ¿Quieres modificar el nombre del alumno con NIF: {nif}? [Y/n]:  ''').upper()
            if (cambio == "Y"):
                aux: str = input("¿Cual es el nombre nuevo?: ")
                alumno.nombre = aux
            
            cambio: str = input(f"¿Quieres modificar los apellidos del alumno con NIF: {nif}? [Y/n]:  ").upper()
            while(cambio != "Y" and cambio != "N"):
                cambio: str = input(f'''No has introducido un valor valido.
                                    ¿Quieres modificar los apellidos del alumno con NIF: {nif}? [Y/n]:  ''').upper()
            if (cambio == "Y"):
                aux: str = input("¿Cuales son los apellidos nuevos?: ")
                alumno.apellidos = aux

            cambio: str = input(f"¿Quieres modificar el telefono del alumno con NIF: {nif}? [Y/n]:  ").upper()
            while(cambio != "Y" and cambio != "N"):
                cambio: str = input(f'''No has introducido un valor valido.
                                    ¿Quieres modificar el telefono del alumno con NIF: {nif}? [Y/n]:  ''').upper()
            if (cambio == "Y"):
                aux: str = input("¿Cual es el telefono nuevo?: ")
                alumno.telefono = aux
            
            cambio: str = input(f"¿Quieres modificar el email del alumno con NIF: {nif}? [Y/n]:  ").upper()
            while(cambio != "Y" and cambio != "N"):
                cambio: str = input(f'''No has introducido un valor valido.
                                    ¿Quieres modificar el email del alumno con NIF: {nif}? [Y/n]:  ''').upper()
            if (cambio == "Y"):
                aux: str = input("¿Cual es el email nuevo?: ")
                alumno.email = aux

            cambio: str = input(f"¿Quieres modificar el aprobado del alumno con NIF: {nif}? [Y/n]:  ").upper()
            while(cambio != "Y" and cambio != "N"):
                cambio: str = input(f'''No has introducido un valor valido.
                                    ¿Quieres modificar el aprobado del alumno con NIF: {nif}? [Y/n]:  ''').upper()
            if (cambio.upper == "Y"):
                aux: str = input("¿Ha aprobado? [Y/n]: ").upper()
                while (aux != "Y" and aux != "N"):
                    aux: str = input(f'''No has introducido un valor valido.
                                    ¿Ha aprobado el alumno con NIF: {nif}? [Y/n]:  ''').upper()
                if (aux == "Y"):
                    alumno.aprobado = True
                else:
                    alumno.aprobado = False

        else:
            print(f"Alumno con NIF: {nif} no ha sido encontrado")
        
    def mostrar_datos_nif(self):
        nif: str = input("NIF: ")
        alumno: Alumno = self.buscar_alumno_nif(nif)
        if (alumno != None):
            print(f"El alumno es: {alumno.get_alumno()}")
        else:
            print(f"Alumno con NIF: {nif} no ha sido encontrado")

    def mostrar_datos_mail(self):
        email: str = input("Email del alumno: ")
        alumno: Alumno = self.buscar_alumno_email(email)
        if(alumno != None):
            print(f"El alumno es: {alumno.get_alumno()}")
        else:
            print(f"Alumno con email: {email} no ha sido encontrado")

    def mostrar_alumnos(self):
        for alumno in self.lista_alumnos:
            print(alumno.get_alumno())

    def aprobar(self):
        nif: str = input("NIF: ")
        alumno: Alumno = self.buscar_alumno_nif(nif)
        if(alumno != None):
            alumno.aprobado = True
            print("Nota cambiada")
        else:
            print(f"Alumno con NIF: {nif} no ha sido encontrado")

    def suspender(self):
        nif: str = input("NIF: ")
        alumno: Alumno = self.buscar_alumno_nif(nif)
        if(alumno != None):
            alumno.aprobado = False
            print("Suspendido")
        else:
            print(f"Alumno con NIF: {nif} no ha sido encontrado")
    
    def alumnos_aprobados(self):
        for alumno in self.lista_alumnos:
            if(alumno.get_aprobado() == True):
                print(alumno.get_alumno())
    
    def alumnos_suspendidos(self):
        for alumno in self.lista_alumnos:
            if(alumno.get_aprobado() == False):
                print(alumno.get_alumno())
            
def cartera():
    alumnos: ListaAlumnos = ListaAlumnos()

    while True:
        print('''(1) Añadir un alumno
(2) Eliminar alumno por NIF
(3) Actualizar datos de un alumno por NIF
(4) Mostrar datos de un alumno por NIF
(5) Mostrar datos de un alumno por Email
(6) Listar TODOS os alumnos
(7) Aprobar Alumno por NIF
(8) Suspender Alumno por NIF
(9) Mostrar alumnos aprobados
(10) Mostrar alumnos suspensos
(X) Finalizar Programa
''')
        respuesta: str = input("Seleccione la opción: ")
        if (respuesta == "1"):
            alumnos.agregar_alumno()
        elif (respuesta=="2"):
            alumnos.eliminar_alumno()
        elif (respuesta=="3"):
            alumnos.actualizar_datos()
        elif (respuesta=="4"):
            alumnos.mostrar_datos_nif()
        elif (respuesta=="5"):
            alumnos.mostrar_datos_mail()
        elif (respuesta=="6"):
            alumnos.mostrar_alumnos()
        elif (respuesta=="7"):
            alumnos.aprobar()
        elif (respuesta=="8"):
            alumnos.suspender()
        elif (respuesta=="9"):
            alumnos.alumnos_aprobados()
        elif (respuesta=="10"):
            alumnos.alumnos_suspendidos()
        elif (respuesta=="X"):
            print("Saliendo de la cartera de alumnos.")
            break
        else:
            print("Opción no valida.")

if __name__=="__main__":
    cartera()


