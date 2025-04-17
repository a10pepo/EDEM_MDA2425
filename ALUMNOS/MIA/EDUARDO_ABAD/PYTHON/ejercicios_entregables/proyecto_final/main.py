import pandas as pd
from funciones import añadir_alumno, eliminar_alumno, actualizar_alumno, mostrar_alumno, mostrar_alumno_correo, mostrar_alumnos, aprobar_alumno, suspender_alumno, mostrar_aprobados, mostrar_suspenso   # Importamos todas las funciones

lista_alumnos_completa={}
    
'''
Mostramos todas las opciones por pantalla y hacemos que si pulsa algún
botón para el que no hay designado nada, de un error y pruebe otra vez
''' 
# Si me da tiempo puedo ponerle un pause, sleep entre que me da un print y luego vuelvo a mostrarle todas las opciones

while True:
    opcion=input('Selecciona una opcion: \n (1) Añadir alumno  \n (2) Eliminar alumno por NIF \n (3) Actualizar datos del alumno por NIF \n (4) Mostrar datos del alumno por NIF \n (5) Mostrar todos los datos de un alumno por correo \n (6) Listar todos los alumnos \n (7) Aprobar alumno por NIF \n (8) Suspender alumno por NIF \n (9) Mostrar los alumnos aprobados \n'\
            ' (10) Mostrar los alumnos suspensos \n (x) Finalizar programa \n ' )  
    if opcion == 'x':   # Condición para que si pulsa x se cierre el programa
        break
    elif opcion == '1':
        añadir_alumno(lista_alumnos_completa)
        print('Alumno creado con exito')
    elif opcion == '2':
        por_dni = input('Introduce un NIF de un alumno: ')
        eliminar_alumno(lista_alumnos_completa, por_dni)  
    elif opcion == '3':
        por_dni = input('Introduce un NIF de un alumno: ')
        actualizar_alumno(lista_alumnos_completa,por_dni)
    elif opcion == '4':
        por_dni = input('Introduce un NIF de un alumno: ')
        mostrar_alumno(lista_alumnos_completa, por_dni)
    elif opcion == '5':
        introduce_correo = input('Introduce el correo electronico: ')
        mostrar_alumno_correo(lista_alumnos_completa, introduce_correo)
    elif opcion == '6':
        mostrar_alumnos(lista_alumnos_completa)
    elif opcion == '7':
        por_dni = input('Introduce un NIF de un alumno: ')
        aprobar_alumno(lista_alumnos_completa,por_dni)
    elif opcion == '8':
        por_dni = input('Introduce un NIF de un alumno: ')
        suspender_alumno(lista_alumnos_completa,por_dni)
    elif opcion == '9':
        mostrar_aprobados(lista_alumnos_completa)
    elif opcion == '10':
        mostrar_suspenso(lista_alumnos_completa)        
    else:
        break


     