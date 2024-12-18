from añadir_alumno import anyadir_alumno
from eliminar_alumno_nif import eliminar_alumno
from actualizar_datos import actualizar_datos
from mostrar_datos_nif import mostrar_datos_nif
from mostrar_datos_email import mostrar_datos_email
from aprobar_alumno import aprobar_alumno
from suspender_alumno import suspender_alumno
from mostrar_aprobados import mostrar_aprobados
from mostra_suspendidos import mostrar_suspendidos

alumnos = []
while True:

    print(''' \n Hola. Bienvenido al programa de la empresa de formación "Fórmate S.L". ¿Que desea hacer?
    
    1. Añadir un alumno 
    2. Eliminar un alumno por NIF
    3. Actualizar datos de un alumno por NIF
    4. Mostrar datos de un alumno por NIF
    5. Mostrar datos de un alumno por EMAIL
    6. Listar todos los alumnos
    7. Aprobar Alumno por NIF
    8. Suspender Alumno por NIF
    9. Mostrar alumnos aprobados
    10. Mostrar alumnos suspensos
    X. Finalizar Programa
    ''')

    opcion = input ()


    if opcion == '1':
        anyadir_alumno(alumnos)

    elif opcion == '2':
        eliminar_alumno(alumnos)
        
    elif opcion == '3':
        actualizar_datos(alumnos)

    elif opcion == '4':
        mostrar_datos_nif(alumnos)

    elif opcion == '5':
        mostrar_datos_email(alumnos)

    elif opcion == '6':
        print (alumnos)

    elif opcion == '7':
        aprobar_alumno(alumnos)

    elif opcion == '8':
        suspender_alumno(alumnos)

    elif opcion == '9':
        mostrar_aprobados(alumnos)
        
    elif opcion == '10':
        mostrar_suspendidos(alumnos)
        
    elif opcion == 'X':
        print ('¡Nos vemos en la siguiente consulta!')
        exit ()
    else:
        print('\n Opción incorrecta, selecciona una opción del 1 al 10 o X para salir')  
