
def mostrar_datos_nif(alumnos):

    nif = input ('Dame el NIF de un alumno para comprobar el alumno: ')

    for alumno in alumnos:
        if alumno['NIF'] == nif:
            print(alumno)
        else:
           print ('Alumno no encontrado')

    return alumnos