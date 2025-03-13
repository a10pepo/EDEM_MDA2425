from funciones_alumnos import (
    cargar_alumnos,
    guardar_alumnos,
    añadir_alumno,
    eliminar_alumno,
    actualizar_alumno,
    buscar_alumno_por_nif,
    buscar_alumno_por_email,
    listar_alumnos,
    cambiar_estado_aprobado,
    listar_alumnos_por_estado,
)

def main():
    alumnos = cargar_alumnos()  # Ahora `alumnos` es un DataFrame

    while True:
        print("""
Menú de opciones:
(1) Añadir un alumno
(2) Eliminar alumno por NIF
(3) Actualizar datos de un alumno por NIF
(4) Mostrar datos de un alumno por NIF
(5) Mostrar datos de un alumno por Email
(6) Listar TODOS los alumnos
(7) Aprobar Alumno por NIF
(8) Suspender Alumno por NIF
(9) Mostrar alumnos aprobados
(10) Mostrar alumnos suspensos
(X) Finalizar Programa
""")


        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            # Añadir un alumno
            nuevo_alumno = {
                "NIF": input("NIF: ").strip(),
                "Nombre": input("Nombre: ").strip(),
                "Apellidos": input("Apellidos: ").strip(),
                "Teléfono": input("Teléfono: ").strip(),
                "Email": input("Email: ").strip(),
            }

            # Bucle para validar la entrada del campo "Aprobado"
            while True:
                aprobado_input = input("¿Está aprobado? (sí/no): ").strip().lower()
                if aprobado_input in ["sí", "no"]:
                    nuevo_alumno["Aprobado"] = aprobado_input == "sí"  # True si es "sí", False si es "no"
                    break
                else:
                    print("Por favor, escribe 'sí' o 'no'.")
            
            alumnos = añadir_alumno(alumnos, nuevo_alumno)

        elif opcion == "2":
            # Eliminar alumno por NIF
            nif = input("Introduce el NIF del alumno a eliminar: ").strip()
            alumnos = eliminar_alumno(alumnos, nif)

        elif opcion == "3":
            # Actualizar datos de un alumno por NIF
            nif = input("Introduce el NIF del alumno: ").strip()
            alumno = buscar_alumno_por_nif(alumnos, nif)
            if alumno is not None:
                nuevos_datos = {
                    "Nombre": input(f"Nombre ({alumno['Nombre']}): ").strip() or alumno["Nombre"],
                    "Apellidos": input(f"Apellidos ({alumno['Apellidos']}): ").strip() or alumno["Apellidos"],
                    "Teléfono": input(f"Teléfono ({alumno['Teléfono']}): ").strip() or alumno["Teléfono"],
                    "Email": input(f"Email ({alumno['Email']}): ").strip() or alumno["Email"],
                }
                alumnos = actualizar_alumno(alumnos, nif, nuevos_datos)
            else:
                print("Alumno no encontrado.")

        elif opcion == "4":
            # Mostrar datos de un alumno por NIF
            nif = input("Introduce el NIF: ").strip()
            alumno = buscar_alumno_por_nif(alumnos, nif)
            if alumno is not None:
                print(alumno)
            else:
                print("Alumno no encontrado.")

        elif opcion == "5":
            # Mostrar datos de un alumno por Email
            email = input("Introduce el Email: ").strip()
            alumno = buscar_alumno_por_email(alumnos, email)
            if alumno is not None:
                print(alumno)
            else:
                print("Alumno no encontrado.")

        elif opcion == "6":
            # Listar todos los alumnos
            for index, alumno in alumnos.iterrows():
                print(alumno.to_dict())  # Convertimos cada fila en un diccionario para mostrarla

        elif opcion == "7":
            # Aprobar alumno por NIF
            nif = input("Introduce el NIF: ").strip()
            alumnos = cambiar_estado_aprobado(alumnos, nif, True)

        elif opcion == "8":
            # Suspender alumno por NIF
            nif = input("Introduce el NIF: ").strip()
            alumnos = cambiar_estado_aprobado(alumnos, nif, False)

        elif opcion == "9":
            # Mostrar alumnos aprobados
            aprobados = listar_alumnos_por_estado(alumnos, True)
            for index, alumno in aprobados.iterrows():
                print(alumno.to_dict())

        elif opcion == "10":
            # Mostrar alumnos suspensos
            suspensos = listar_alumnos_por_estado(alumnos, False)
            for index, alumno in suspensos.iterrows():
                print(alumno.to_dict())

        elif opcion.upper() == "X":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
