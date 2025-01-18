def mostrar_aprobados(alumnos):

    for alumno in alumnos:
        if alumno['Aprobado'] == True:
            print(alumno)
    
    return alumnos