
lista_alumnos = []

while True:
    menu = input('''
    Hola, ¿qué deseas realizar?
    1. Añadir un alumno
    2. Eliminar alumno por NIF
    3. Actualizar datos de un alumno por NIF
    4. Mostrar datos de un alumno por NIF
    5. Mostrar datos de un alumno por email
    6. Listar todos los alumnos
    7. Aprobar alumno por NIF
    8. Suspender alumno por NIF
    9. Mostrar alumnos aprobados
    10. Mostrar alumnos suspendidos
    X. Finalizar programa\n''').upper()

    if menu == 'X':
        break
#1 Añadir un alumno 
    elif menu == '1':
        nuevo_alumno = {
            "NIF": input('Ingresa el NIF:\n'),
            "Nombre": input('Ingresa tu nombre:\n'),
            "Apellidos": input('Ingresa tu apellido:\n'),
            "Telefono": input('Ingresa tu telefono:\n'),
            "Email": input('Ingresa tu email:\n'),
            "Aprobado": True if input('¿Aprueba? (si/no):\n').lower() == 'si' else False
        }
        lista_alumnos.append(nuevo_alumno)
        print("Alumno agregado correctamente.")

#2 Eliminar alumno por NIF
    elif menu == '2':
        nif_eliminar = input('Ingresa el NIF del alumno que deseas eliminar:\n')
        for elemento in lista_alumnos:
            if nif_eliminar == elemento["NIF"]:
                lista_alumnos.remove(elemento)
                print(f"Alumno con NIF {nif_eliminar} eliminado exitosamente.")
                break
        else:
            print(f"No existe ningún alumno con este NIF {nif_eliminar}.")

#3 Actualizar datos de alumno por NIF
    elif menu == '3':
        actualizar_datos = input('Ingresa el NIF del alumno que deseas actualizar:\n')
        for elemento in lista_alumnos:
            if actualizar_datos == elemento["NIF"]:
                elemento["NIF"] = input('Ingresa el nif actualizado: \n')
                elemento["Nombre"] = input('Ingresa el nombre actualizado:\n')
                elemento["Apellidos"]= input('Ingresa el apellido actualizado:\n')
                elemento["Telefono"] = input('Ingresa el telefono actualizado:\n')
                elemento["Email"]= input('Ingresa el email actualizado:\n')
                print(f'Los datos han sido actualizados')
            
#4 Mostrar datos de un alumno por NIF
    elif menu == '4':
        mostrar = input('Ingresa el NIF del alumno que quieres consultar: \n')
        for elemento in lista_alumnos:
            if mostrar == elemento["NIF"]:
                print(elemento)
            
#5 Mostrar datos de un alumno por email
    elif menu == '5':
        email = input('Ingresa el correo del alumno para consultar: \n')
        for elemento in lista_alumnos:
            if email == elemento["Email"]:
                print(elemento)
            
#6 Listar todos los alumnos
    elif menu == '6':
        print(lista_alumnos)

#7 Aprobar alumno por NIF
    elif menu == '7':
        aprobar = input('Ingresa el NIF del alumno que deseas aprobar: \n')
        for elemento in lista_alumnos:
            if aprobar == elemento["NIF"]:
                elemento["Aprobado"] = True if input(f'Deseas aprobar a {elemento}, escribe si o no \n') == 'si' else False
            
#8 Suspender alumno por NIF
    elif menu == '8':
        suspendido = input('Ingresa el NIF del alumno que deseas suspender: \n')
        for elemento in lista_alumnos:
            if suspendido == elemento["NIF"]:
                elemento["Aprobado"] = False if input(f'Deseas suspender a {elemento}, escribe si o no \n') == 'si' else True
            
#9 Mostrar alumnos aprobados
    elif menu == '9':
        for alumno in lista_alumnos:
            if alumno["Aprobado"] == True:
                print(alumno)

#10 Mostrar alumnos suspendidos 
    elif menu == '10':
        for alumno in lista_alumnos:
            if alumno["Aprobado"] == False:
                print(alumno)
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")