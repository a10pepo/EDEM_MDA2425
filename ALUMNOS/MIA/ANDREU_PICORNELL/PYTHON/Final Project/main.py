"""
File name: main.py
Author: Andreu Picornell
Creation date: 2024-11-07
Description: This script manages a list of students. It allows the user to:
    - Add a student
    - Delete a student by NIF
    - Update student details by NIF
    - Display student details by NIF or Email
    - List all students
    - Approve or suspend a student by NIF
    - Show approved or suspended students

Dependencies:
- None. The script runs with the standard Python library.

Usage instructions:
1. Run the script from the command line using: `python main.py`.
2. Follow the on-screen menu to manage students.
"""
from gestor_alumnos import *

def main_menu():
    while True:
        print("----------------Menú principal-------------------")
        print("(1) Añadir un alumno")
        print("(2) Eliminar alumno por NIF")
        print("(3) Actualizar datos de un alumno por NIF")
        print("(4) Mostrar datos de un alumno por NIF")
        print("(5) Mostrar datos de un alumno por Email")
        print("(6) Listar TODOS os alumnos")
        print("(7) Aprobar Alumno por NIF")
        print("(8) Suspender Alumno por NIF")
        print("(9) Mostrar alumnos aprobados")
        print("(10) Mostrar alumnos suspensos")
        print("(X) Finalizar Programa")
        opcion = input("Seleccione una opción: ").strip().upper()

        if opcion == "1":
            nif = input("NIF del alumno: ")
            nombre = input("Nombre del alumno: ")
            apellidos = input("Apellidos del alumno: ")
            telefono = input("Teléfono del alumno: ")
            email = input("Email del alumno: ")
            agregar_alumno(nif, nombre, apellidos, telefono, email)
        elif opcion == "2":
            nif = input("NIF del alumno a eliminar: ")
            eliminar_alumno(nif)
        elif opcion == "3":
            nif = input("NIF del alumno a actualizar: ")
            modificar_alumno(nif)
        elif opcion == "4":
            nif = input("NIF del alumno a mostrar: ")
            mostrar_alumno_por_nif(nif)
        elif opcion == "5":
            email = input("Email del alumno a mostrar: ")
            mostrar_alumno_por_email(email)
        elif opcion == "6":
            mostrar_todos_los_alumnos()
        elif opcion == "7":
            nif = input("NIF del alumno a aprobar: ")
            aprobar_alumno(nif)
        elif opcion == "8":
            nif = input("NIF del alumno a suspender: ")
            suspender_alumno(nif)
        elif opcion == "9":
            mostrar_los_alumnos_aprobados()
        elif opcion == "10":
            mostrar_los_alumnos_suspendidos()
        elif opcion == "X":
            print("Finalizando el programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main_menu()