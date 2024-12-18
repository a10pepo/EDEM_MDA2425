
def anyadir_alumno(alumnos):

    print("\n Introduce los datos del alumno")
    a = input ("Introduce el NIF con la letra en mayúscula: ")
    b = input ("Introduce el nombre en mayúsculas: ")
    c = input ("Introduce los apellidos en mayúsculas: ")
    d = input ("Introduce tu teléfono: ")
    e = input ("Introduce tu Email: ")
    f = bool(input ("Introduce APROBADO (Escribe cualquier cosa) o SUSPENDIDO (Deja vacío): "))

    alumno = {
        "NIF": a,
        "Nombre": b,
        "Apellidos": c,
        "Telefono": d,
        "Email": e,
        "Aprobado": f
    }

    alumnos.append(alumno)

    return alumnos


