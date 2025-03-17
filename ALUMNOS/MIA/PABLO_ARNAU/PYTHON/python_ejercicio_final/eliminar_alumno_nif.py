def eliminar_alumno(alumnos):

    nif = input ('Dame el NIF de un alumno para eliminarlo: ')

    for alumno in alumnos:
        if alumno['NIF'] == nif:
            alumnos.remove(alumno)
            print(f"\nAlumno con NIF {nif} se ha eliminado correctamente.")
            
        else :
            print ('Alumno no encontrado')

    return alumnos