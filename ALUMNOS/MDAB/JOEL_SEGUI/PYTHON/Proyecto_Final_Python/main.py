import functions

def main():
    gestor = functions.GestorAlumnos()  # Para poder utilizar la clase creada

    while True:
        print("\n" + "="*50)
        print(" " * 10 + "🎓✨ Menú de Opciones 🎓✨")
        print("="*50)
        print(" " * 5 + "[1]  ➜ 🌟 Registrar alumno")
        print(" " * 5 + "[2]  ➜ 📝 Editar o actualizar alumno")
        print(" " * 5 + "[3]  ➜ 📚 Mostrar todos los alumnos")
        print(" " * 5 + "[4]  ➜ 🔍 Mostrar alumno por NIF")
        print(" " * 5 + "[5]  ➜ 📧 Mostrar alumno por Email")
        print(" " * 5 + "[6]  ➜ ✅ Aprobar alumno por NIF")
        print(" " * 5 + "[7]  ➜ ❌ Suspender alumno por NIF")
        print(" " * 5 + "[8]  ➜ 🎉 Mostrar alumnos aprobados")
        print(" " * 5 + "[9]  ➜ 🚫 Mostrar alumnos suspendidos")
        print(" " * 5 + "[10] ➜ 🗑️ Eliminar alumno")
        print(" " * 5 + "[X]  ➜ 🚪 Salir")
        print("="*50)

        opcion = input("Selecciona una opción: ").lower()

        if opcion == "1":
            gestor.registrar_alumno()
        elif opcion == "2":
            gestor.editar_alumno()
        elif opcion == "3":
            gestor.mostrar_alumnos()
        elif opcion == "4":
            gestor.mostrar_alumno_NIF()
        elif opcion == "5":
            gestor.mostrar_alumno_email()
        elif opcion == "6":
            gestor.aprobar_alumno()
        elif opcion == "7":
            gestor.suspender_alumno()
        elif opcion == "8":
            gestor.mostrar_aprobados()
        elif opcion == "9":
            gestor.mostrar_suspensos()
        elif opcion == "10":
            gestor.eliminar_alumno()
        elif opcion == "x":
            print("\n🎓✨ Saliendo del programa... 🎓✨\n")
            break
        else:
            print("\n🚫 Opción no válida, por favor inténtelo de nuevo 🚫")
      

main()