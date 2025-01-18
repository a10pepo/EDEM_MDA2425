def actualizar_datos (alumnos):
    
    nif = input ('Dame el NIF de un alumno para realizar una modificación: ')

    for alumno in alumnos:
        if alumno['NIF'] == nif:
           while True:
                print('''¿Que desea modificar?
    1. Nombre
    2. Apellidos
    3. Teléfono
    4. Email
    5. APROBADO O SUSPENSO
    X. NADA
                   ''')
                opcion = input()

                if opcion == '1':
                    n_nombre = input ('Introduce el nuevo nombre: ')
                    alumno["Nombre"] = n_nombre
                    print ('Nombre modificado correctamente')
                    return alumnos

                elif opcion == '2':
                    n_apellidos = input ('Introduce los nuevos apellidos: ')
                    alumno["Apellidos"] = n_apellidos
                    print ('Apellidos modificados correctamente')
                    return alumnos

                elif opcion == '3':
                    n_telefono = input ('Introduce el nuevo telefono: ')
                    alumno["Telefono"] = n_telefono
                    print ('Telefono modificado correctamente')
                    return alumnos

                elif opcion == '4':
                    n_email = input ('Introduce el nuevo email: ')
                    alumno["Email"] = n_email
                    print ('Email modificado correctamente')
                    return alumnos

                elif opcion == '5':
                    n_estado = input ('Está aprobado (Escribe culquier cosa) o suspenso (Deje vacío): ')
                    alumno["Aprobado"] = bool(n_estado)
                    print ('Estado modificado correctamente')
                    return alumnos
                
                elif opcion == 'X':
                    print ('¡Se cierra la función "actualizar datos"!')
                    return alumnos
        else :
            print ('Alumno no encontrado')
    
    return alumnos