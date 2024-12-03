def aprobar_alumno(alumnos):

    nif = input ('Dame el NIF de un alumno para aprobarlo: ')

    for alumno in alumnos:
            if alumno['NIF'] == nif:
                if alumno['Aprobado'] == True:
                    print('Alumno ya aprobado')
                if alumno['Aprobado'] == False:
                    alumno['Aprobado'] = True
                    print('Alumno cambiado de supendido a aprobado')
            else:
                print ('Alumno no encontrado')
    
    return alumnos