'''
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
(6) Listar TODOS los alumnos
(7) Aprobar Alumno por NIF
(8) Suspender Alumno por NIF
(9) Mostrar alumnos aprobados
(10) Mostrar alumnos suspensos
(X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X'''

alumnos = []

#Añadir un alumno
def añadir_alumno():
    print("Añadir un nuevo alumno")
    nombre = input("Introduce tu nombre: ")
    apellidos = input("Introduce tus apellidos: ")
    telefono = input("Introduce tu teléfono: ")
    email = input("Introduce tu email: ")
    nif = input("Introduce tu NIF: ")
    aprobado = False  

    alumno = {
        "NIF": nif,
        "Nombre": nombre,
        "Apellidos": apellidos,
        "Teléfono": telefono,
        "Email": email,
        "Aprobado": aprobado
    }

    alumnos.append(alumno)

    print("Alumno añadido con éxito.")


# Eliminar alumno por NIF
def eliminar_alumno():
    print("Eliminar un alumno")
    nif = input("Introduce el NIF del alumno que quieres eliminar: ")
    
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            alumnos.remove(alumno)
            print("Alumno eliminado con éxito.")
            return
    print("No se encontró ningún alumno con ese NIF.")

# Actualizar datos de un alumno por NIF
def actualizar_alumno():
    print("Actualizar datos de un alumno")
    nif = input("Introduce el NIF del alumno que quieres actualizar: ")
    
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            print(f"Datos actuales del alumno: {alumno}")
            
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_apellidos = input("Nuevos apellidos: ")
            nuevo_telefono = input("Nuevo teléfono: ")
            nuevo_email = input("Nuevo email: ")

            if nuevo_nombre:
                alumno["Nombre"] = nuevo_nombre
            if nuevo_apellidos:
                alumno["Apellidos"] = nuevo_apellidos
            if nuevo_telefono:
                alumno["Teléfono"] = nuevo_telefono
            if nuevo_email:
                alumno["Email"] = nuevo_email
            
            print("Datos actualizados con éxito.")
            return  
        
    print("No se encontró ningún alumno con ese NIF.")

# Mostrar datos de un alumno por NIF
def mostrar_alumno_nif():
    print("Mostrar datos de un alumno")
    nif = input("Introduce el NIF del alumno que quieras consultar: ")
    
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            print(f"Datos del alumno: {alumno}")
            return
    
    print("No se encontró ningún alumno con ese NIF.")

# Mostrar datos de un alumno por Email
def mostrar_alumno_email():
    print("Mostrar datos de un alumno")
    email = input("Introduce el email del alumno que quieras consultar: ")
    
    for alumno in alumnos:
        if alumno["Email"] == email:
            print(f"Datos del alumno: {alumno}")
            return
    
    print("No se encontró ningún alumno con ese email.")

# Listar TODOS los alumnos
def todos_los_alumnos():
    print("Lista de todos los alumnos")
    
    if not alumnos:
        print("No hay ningún alumno.")
        return
    
    for alumno in alumnos:
        print(alumno)

# Aprobar Alumno por NIF
def aprobar_alumno():
    print("Aprobar un alumno")
    nif = input("Introduce el NIF del alumno que quieras aprobar: ")
    
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            if not alumno["Aprobado"]:
                alumno["Aprobado"] = True
                print(f"El alumno {alumno["Nombre"]} está aprobado.")
            else:
                print(f"El alumno {alumno["Nombre"]} ya estaba aprobado.")
            return
    
    print("No se encontró ningún alumno con ese NIF.")

# Suspender Alumno por NIF
def suspender_alumno():
    print("Suspender un alumno")
    nif = input("Introduce el NIF del alumno que quieras suspender: ")
    
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            if alumno["Aprobado"]:
                alumno["Aprobado"] = False
                print(f"El alumno {alumno["Nombre"]} está suspendido.")
            else:
                print(f"El alumno {alumno["Nombre"]} ya estaba suspendido.")
            return
    
    print("No se encontró ningún alumno con ese NIF.")

# Mostrar alumnos aprobados
def mostrar_aprobados():
    print("Alumnos aprobados:")
    aprobados = [alumno for alumno in alumnos if alumno["Aprobado"]]
    
    if aprobados:
        for alumno in aprobados:
            print(alumno)
    else:
        print("No hay alumnos aprobados.")

# Mostrar alumnos suspensos
def mostrar_suspesos():
    print("Alumnos suspesos:")
    suspesos = [alumno for alumno in alumnos if not alumno["Aprobado"]]
    
    if suspesos:
        for alumno in suspesos:
            print(alumno)
    else:
        print("No hay alumnos suspensos.")

# Menú (X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X
def menu():
    while True:
        print("MENÚ PRINCIPAL")
        print("1. Añadir un alumno")
        print("2. Eliminar un alumno por NIF")
        print("3. Actualizar datos de un alumno por NIF")
        print("4. Mostrar datos de un alumno por NIF")
        print("5. Mostrar datos de un alumno por Email")
        print("6. Listar TODOS los alumnos")
        print("7. Aprobar un alumno por NIF")
        print("8. Suspender un alumno por NIF")
        print("9. Mostrar alumnos aprobados")
        print("10. Mostrar alumnos suspensos")
        print("X. Finalizar Programa")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            añadir_alumno()
        elif opcion == "2":
            eliminar_alumno()
        elif opcion == "3":
            actualizar_alumno()
        elif opcion == "4":
            mostrar_alumno_email()
        elif opcion == "5":
            mostrar_alumno_email()
        elif opcion == "6":
            todos_los_alumnos()
        elif opcion == "7":
            aprobar_alumno()
        elif opcion == "8":
            suspender_alumno()
        elif opcion == "9":
            mostrar_aprobados()
        elif opcion == "10":
            mostrar_suspesos()
        elif opcion.upper() == "X":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, escoje una opción valida.")

menu()
