import re #Este módulo sirve para forzar una estructura de email

class Alumno:
    #Realmente la definición de los tipos de datos es opcional
    NIF: str
    nombre: str
    apellidos: str
    telefono: str
    email: str
    aprobado = "Aún no ha sido evaluado" #De base el alumno no tiene nota
    
    def __init__(self, NIF: str, nombre: str, apellidos: str, telefono: str, email: str):
        self.NIF = NIF
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
       # self.aprobado = aprobado

class GestorAlumnos:

    def __init__(self):
        self.lista_alumnos = []
    
    def verificar_lista_vacia(self): 
        if not self.lista_alumnos:
            print("\nNo hay alumnos registrados.")
            return True  # Retorna True si está vacía
        return False  # Retorna False si hay alumnos
    
    #Función para forzar estructura del email
    #Esto lo he buscado para hacerlo más realista (me aburro)

    def es_email_valido(self,email):
        # Expresión regular para validar un email
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None


    def registrar_alumno(self):
        #Hay que confirmar que no se creen varios alumnos con el mismo NIF
        
        while True:
            NIF = input("Introduce tu NIF: ")
            encontrado = False

            for alumno in self.lista_alumnos:
                if alumno.NIF == NIF:
                    print(f"Lo siento, ya se ha registrado un alumno con el NIF - {NIF}")
                    encontrado = True
                    break #Salir del bucle for si se encuentra un NIF repetido
            
            if encontrado == True:
                continue #Vuelve a pedir el NIF
            else:
                break

        nombre = input("Introduce tu nombre: ")
        apellidos = input("Introduce tus apellidos: ")
        
        #Validar el teléfono
        while True:
            telefono = input("Introduce tu teléfono personal español: ")

            if telefono.isdigit() and len(telefono) == 9: #Función para comprobar que solo se han introducido números
                break
            else:
                print("Error: El teléfono debe contener solo números y tener 9 dígitos. Inténtalo de nuevo.")

        #Validar el email
        while True:
            email = input("Introduce tu correo electrónico: ")
            if self.es_email_valido(email):
                break  # Salir del bucle si el email es válido
            else:
                print("Error: El formato del email no es válido (Ej: usuario@gmail.com). Inténtalo de nuevo.")

        #Creamos una nueva instancia de Alumno (el alumno añadido "se envia a Alumno")   
        # Aquí se esta llamando el constructor __init__ de la clase Alumno  
        nuevo_alumno = Alumno(NIF, nombre, apellidos, telefono, email)

        #Agregar el nuevo alumno a la lista
        self.lista_alumnos.append(nuevo_alumno)
        print(f"Alumno {nuevo_alumno.nombre} {nuevo_alumno.apellidos} añadido con éxito.")
    

    def eliminar_alumno(self):
        # Comprobar si la lista está vacía
        if self.verificar_lista_vacia():
            return 
        
        NIF = input("Introduce el 'NIF' de la persona que desee eliminar: ")
        for alumno in self.lista_alumnos:
            if alumno.NIF == NIF:

                #Confirmación de eliminación
                print(f'Se ha encontrado el alumno: {alumno.nombre} {alumno.apellidos}')
                while True:
                    confirm = input(f"¿Estás seguro que desea eliminar el alumno {alumno.nombre} {alumno.apellidos}? [Si, No]: ").lower()
                    
                    if confirm == "si":
                        #Se elimina el alumno
                        print(f'Alumno {alumno.nombre} {alumno.apellidos} eliminado con éxito') #eliminamos despues para saber el nombre y apellido (si se borra no existe)
                        self.lista_alumnos.remove(alumno) #Eliminamos alumno de la lista
                        break #Salir del bucle una vez encontrado y eliminado

                    elif confirm == "no":
                        print("No se ha eliminado al alumno")
                        break
  
                    else:
                     print("Por favor, introduce 'Si' o 'No'... ") 

                break #Para salir del bucle while una vez la eliminacion o no  

        else:
            #Este else se ejecuta si el bucle no encuentra coincidencias
            print(f"el NIF {NIF} no se encuentra registrado en nuestra base de datos...")
            

    def mostrar_alumno_NIF(self):
        # Comprobar si la lista está vacía
        if self.verificar_lista_vacia():
            return 
        
        NIF = input("Introduce el 'NIF' del alumno que desea visualizar: ")
        encontrado = False #Variable para confirmar si se encuentra o no

        for alumno in self.lista_alumnos:
            if alumno.NIF == NIF:
                print("Se ha encontrado con éxito al alumno... \n")
                print(f"NIF: {alumno.NIF}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, "
                      f"Teléfono: {alumno.telefono}, Email: {alumno.email}, Aprobado: {alumno.aprobado}")
                    #Lo de arriba lo hago para que sea más legible (sino es muy largo)
                encontrado = True

                break

        if not encontrado: #Es decir, si es false
            print(f"No se ha encontrado un alumno con el NIF: {NIF}")


    def mostrar_alumno_email(self):
        # Comprobar si la lista está vacía
        if self.verificar_lista_vacia():
            return 
        
        email = input("Introduce el 'email' del alumno que desea visualizar: ")
        encontrado = False #Variable para confirmar si se encuentra o no

        for alumno in self.lista_alumnos:
            if alumno.email == email:
                print("Se ha encontrado con éxito al alumno... \n")
                print(f"NIF: {alumno.NIF}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, "
                      f"Teléfono: {alumno.telefono}, Email: {alumno.email}, Aprobado: {alumno.aprobado}")
                encontrado = True

                break

        if not encontrado: #Es decir, si es false
            print(f"No se ha encontrado un alumno con el email: {email}")


    def mostrar_alumnos(self):
        #Comprobar si la lista está vacía
        if self.verificar_lista_vacia():
            return

        print("\nLista de alumnos:")
        for index, alumno in enumerate(self.lista_alumnos, start=1):  # Enumerar para añadir un índice
            print(f"{index}. NIF: {alumno.NIF}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, "
                  f"Teléfono: {alumno.telefono}, Email: {alumno.email}, Aprobado: {alumno.aprobado}")


    def aprobar_alumno(self):
        #Comprobar si la lista está vacía
        if self.verificar_lista_vacia():
            return 
        
        NIF = input("Introduce el 'NIF' del alumno que desea aprobar: ")
        encontrado = False #Variable para confirmar si se encuentra o no

        for alumno in self.lista_alumnos:
            if alumno.NIF == NIF:
                print(f'Se ha encontrado el siguiente alumno con el NIF {alumno.NIF}: {alumno.nombre} {alumno.apellidos}')

                #Confirmación de aprobado
                while True:
                    confirm = input(f"¿Estás seguro que desea aprobar el alumno {alumno.nombre} {alumno.apellidos}? [Si, No]: ").lower()
                    
                    if confirm == "si":
                        print(f'Alumno {alumno.nombre} {alumno.apellidos} ha sido aprobado.') 
                        alumno.aprobado = True # Se aprueba el alumno
                        break #Salir del bucle una vez encontrado y aprobado

                    elif confirm == "no":
                        print(f"No se ha alterado la nota de {alumno.nombre} {alumno.apellidos}")
                        break
  
                    else:
                        print("Por favor, introduce 'Si' o 'No'... ") 
                
                encontrado = True

                break

        if not encontrado: #Es decir, si es false
            print(f"No se ha encontrado un alumno con el NIF: {NIF}")
    

    def suspender_alumno(self):
        #Comprobar si la lista está vacía
        if self.verificar_lista_vacia():
            return       
        
        NIF = input("Introduce el 'NIF' del alumno que desea suspender: ")
        encontrado = False #Variable para confirmar si se encuentra o no

        for alumno in self.lista_alumnos:
            
            if alumno.NIF == NIF:
                print(f'Se ha encontrado el siguiente alumno con el NIF {alumno.NIF}: {alumno.nombre} {alumno.apellidos}')

                #Confirmación de suspenso
                while True:
                    confirm = input(f"¿Estás seguro que desea suspender el alumno {alumno.nombre} {alumno.apellidos}? [Si, No]: ").lower()
                    
                    if confirm == "si":
                        print(f'Alumno {alumno.nombre} {alumno.apellidos} ha sido suspendido.') 
                        alumno.aprobado = False # Se suspende el alumno
                        break #Salir del bucle una vez encontrado y suspendido

                    elif confirm == "no":
                        print(f"No se ha alterado la nota de {alumno.nombre} {alumno.apellidos}")
                        break
  
                    else:
                        print("Por favor, introduce 'Si' o 'No'... ") 
                
                encontrado = True

                break

        if not encontrado: #Es decir, si es false
            print(f"No se ha encontrado un alumno con el NIF: {NIF}")
 

    def mostrar_aprobados(self):
        #Comprobar si la lista está vacía
        if self.verificar_lista_vacia():
            return

        aprobados_encontrados = False

        for index, alumno in enumerate(self.lista_alumnos, start=1):
            if alumno.aprobado == True:
                if not aprobados_encontrados:
                    print("\nLista de alumnos aprobados: \n")
                    aprobados_encontrados = True 
                    print(f"{index}. NIF: {alumno.NIF}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, "
                        f"Teléfono: {alumno.telefono}, Email: {alumno.email}, Aprobado: {alumno.aprobado}")
                     
        if not aprobados_encontrados: #Si es false (si no hay personas aprobadas)
            print("\nNingun alumno está aprobado")


    def mostrar_suspensos(self):
        #Comprobar si la lista está vacía
        if self.verificar_lista_vacia():
            return

        suspensos_encontrados = False

        for index, alumno in enumerate(self.lista_alumnos, start=1):
            if alumno.aprobado == False:
                if not suspensos_encontrados:
                    print("\nLista de alumnos suspendidos: \n")
                    suspensos_encontrados = True
                    print(f"{index}. NIF: {alumno.NIF}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, "
                        f"Teléfono: {alumno.telefono}, Email: {alumno.email}, Aprobado: {alumno.aprobado}") 

        if not suspensos_encontrados: #Si es false (si no hay personas suspendidas)
            print("\nNingun alumno está suspendidos")


    def editar_alumno(self):
        #Comprobar si la lista está vacía
        if self.verificar_lista_vacia():
            return
        
        NIF = input("Introduce el 'NIF' del alumno que desea editar: ")
        encontrado = False 

        for alumno in self.lista_alumnos:
            if alumno.NIF == NIF:
                print(f'Se ha encontrado el siguiente alumno con el NIF {alumno.NIF}: {alumno.nombre} {alumno.apellidos}')

                # Confirmar si se desea editar el alumno
                while True:
                    confirm = input(f"¿Estás seguro que desea editar el alumno {alumno.nombre} {alumno.apellidos}? [Si, No]: ").lower()
                    if confirm == "si":
                        while True:
                            print("¿Qué campo desea modificar?:")
                            print("[1] Nombre")
                            print("[2] Apellidos")
                            print("[3] Teléfono")
                            print("[4] Email")
                            print("[X] Salir")
                            eleccion_editar = input("").lower()  # Añadir () para llamar a la función input()

                            if eleccion_editar == "1":
                                edit_nombre = input("Introduce el nuevo nombre: ")
                                alumno.nombre = edit_nombre
                                print(f"El nombre ha sido actualizado a: {alumno.nombre}")

                            elif eleccion_editar == "2":
                                edit_apellidos = input("Introduce los nuevos apellidos: ")
                                alumno.apellidos = edit_apellidos
                                print(f"Los apellidos han sido actualizados a: {alumno.apellidos}")

                            elif eleccion_editar == "3":
                                while True: 
                                        edit_telf = input("Introduce el nuevo teléfono: ")
                                        if edit_telf.isdigit() and len(edit_telf) == 9:  # Verificar que el nuevo teléfono sea válido
                                            alumno.telefono = edit_telf
                                            print(f"El teléfono ha sido actualizado a: {alumno.telefono}")
                                            break
                                        else:
                                            print("Error: El teléfono debe contener solo números y tener 9 dígitos. Inténtalo de nuevo.")

                            elif eleccion_editar == "4":
                                while True:
                                    edit_email = input("Introduce el nuevo Email: ")
                                    if self.es_email_valido(edit_email):  # Validar el nuevo email
                                        alumno.email = edit_email
                                        print(f"El Email ha sido actualizado a: {alumno.email}")
                                        break  # Salir del bucle si el email es válido
                                    else:
                                        print("Error: El formato del email no es válido (Ej: usuario@gmail.com). Inténtalo de nuevo.")

                            elif eleccion_editar == "x":
                                print("Saliendo de la edición.")
                                break
                            
                            else:
                                print("🚫 Opción no válida, por favor inténtelo de nuevo.")

                            # Preguntar si desea modificar otro campo
                            while True:  # Añadir un bucle aquí para asegurar que se obtiene una respuesta válida
                                continuar = input("¿Deseas editar otro campo? [Si, No]: ").lower()
                                if continuar == "si":
                                    break  # Sale del bucle y continúa editando
                                elif continuar == "no":
                                    print("Saliendo de la edición.")
                                    break
                                else:
                                    print("Por favor, introduce 'Si' o 'No'... ") 

                            if continuar == "no":
                                break  # Sale del bucle de edición

                        break  # Salir del bucle de confirmación de edición

                    elif confirm == "no":
                        print(f"No se ha alterado la información del alumno {alumno.nombre} {alumno.apellidos}")
                        break
                    else:
                        print("Por favor, introduce 'Si' o 'No'... ") 
                    
                encontrado = True
                break

        if not encontrado:
            print(f"No se ha encontrado un alumno con el NIF: {NIF}")

#Fino señores 👌
