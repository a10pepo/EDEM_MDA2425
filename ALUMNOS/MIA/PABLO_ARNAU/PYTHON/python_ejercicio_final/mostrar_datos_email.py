def mostrar_datos_email(alumnos):

    email = input ('Dame el Email de un alumno para comprobar el alumno: ')

    for alumno in alumnos:
        if alumno['Email'] == email:
            print(alumno)
        else:
           print ('Alumno no encontrado')
    

    return alumnos