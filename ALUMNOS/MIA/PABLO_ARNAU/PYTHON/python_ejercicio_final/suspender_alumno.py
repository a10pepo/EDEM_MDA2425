def suspender_alumno(alumnos):

    nif = input ('Dame el NIF de un alumno para aprobarlo: ')

    for alumno in alumnos:
            if alumno['NIF'] == nif:
                if alumno['Aprobado'] == False:
                    print('Alumno ya suspendido')
                if alumno['Aprobado'] == True:
                    alumno['Aprobado'] = False
                    print('Alumno cambiado de aprobado a suspendido')
            else:
                print ('Alumno no encontrado')
    
    return alumnos