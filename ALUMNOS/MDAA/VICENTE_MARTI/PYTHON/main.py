import re

alumnos = {}

def comprobarnif2(): 
    nif = ""
    while True:
        try:
            nif = input("Dame el nif ")
            
            if not re.fullmatch(r"\d{8}[A-Za-z]", nif): 
                raise ValueError("El formato no del NIF no es válido. Deben ser 8 números seguidos de 1 letra.")
            elif nif in alumnos:
                raise ValueError("Este nif ya está registrado")
            else:
                break
                 
        except ValueError as e:
            print(e)
    return nif

def comprobarnif(): 
    nif = ""
    while True:
        try:
            nif = input("Dame el nif ")
            
            if not re.fullmatch(r"\d{8}[A-Za-z]", nif): 
                raise ValueError("El formato no del NIF no es válido. Deben ser 8 números seguidos de 1 letra.")
            else:
                break
                 
        except ValueError as e:
            print(e)
    return nif

def comprobartelefono():
    telefono = 0
    while True:
        try:
            telefono = int(input("Dame el telefono "))
            if not re.fullmatch(r"\d{9}", str(telefono)): 
                raise ValueError()
            else:
                break
        except ValueError:
            print("Telefono incorrecto. Deben ser 9 números.")
    return telefono
    
def comprobarcorreo():
    correo = ""
    while True:
        try:
            correo= input("Dame el correo ")
            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", correo):
                raise ValueError
            else:
                break
        except ValueError:
            print("Correo incorrecto ")
    return correo

def comprobarnota():
    nota = 0.0
    while True:
        try:
            nota= float(input("Dame la nota "))
            if nota > 10 or nota < 0:
                raise ValueError
            elif nota < 5:
                return False
            else:
                return True
        except ValueError:
            print("Nota incorrecta")

def anyadiralumno():
    alumno = {}
    nif = comprobarnif2()
    alumno["nombre"] = input("Dame el nombre ")
    alumno["apellidos"] = input("Dame los apellidos ")
    alumno["telefono"] = comprobartelefono()
    alumno["correo"] = comprobarcorreo()
    alumno["aprobado"] = comprobarnota()
    alumnos[nif] = alumno
    
    
    print("Alumno registrado")
    
 
def eliminaralumno():
    nif = comprobarnif()
    if nif not in alumnos:
        print(f"No hay ningun alumno registrado con el nif {nif}")
    else:
        del alumnos[nif]
        print("Alumno eliminado")
        
def modificaralumno():
    nif= comprobarnif()
    Cortar = True
    while Cortar:
        opcion = input("""
Escoge que dato quieres modificar:
1: Nombre
2: Apellidos
3: Telefono
4: Email
5: Aprobado
6: No modificar nada
""")
        if opcion == "1":
            alumnos[nif]["nombre"] = input("Dime el nombre")
            print("Nombre modificado")
        if opcion == "2":
            alumnos[nif]["apellidos"] = input("Dime los apellidos")
            print("Apellidos modificados")
        if opcion == "3":
            alumnos[nif]["telefono"] = comprobartelefono()
            print("telefono modificado")
        if opcion == "4":
            alumnos[nif]["correo"] = comprobarcorreo()
            print("Correo modificado")
        if opcion == "5":
            alumnos[nif]["nota"]
            print("Aprobado modificado")
        if opcion == "6":
            Cortar = False
        else:
            print("Opcion incorrecta")

def mostrardatospornif():
    nif=comprobarnif()
    print(alumnos[nif])
    
def mostrardatosporemail():
    correo=comprobarcorreo()
    imprimido = False
    for nif in alumnos:
        if nif["correo"] == correo:
            print(alumnos[nif])
            imprimido = True
            break
    if not imprimido:
        print(f"No hay ningun alumno registrado con el correo {correo}")

def listaralumnos():
    for nif in alumnos:
        print(nif)
        print(alumnos[nif])
        
def aprobaralumno():
    nif= comprobarnif()
    alumnos[nif]["aprobado"] = True

def aprobados():
    for nif in alumnos:
        if nif["aprobado"]:
            print(alumnos[nif])

def suspensos():
    for nif in alumnos:
        if not nif["aprobado"]:
            print(alumnos[nif])           
    

if __name__ == "__main__":
    print("Bienvenido al registro de alumnos")
    Cortar = True
    while Cortar:
        opcion= input("""
Selecciona una de las siguientes opciones:

(1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno

(2) Eliminar alumno por NIF

(3) Actualizar datos de un alumno por NIF

(4) Mostrar datos de un alumno por NIF

(5) Mostrar datos de un alumno por Email

(6) Listar TODOS os alumnos

(7) Aprobar Alumno por NIF

(8) Suspender Alumno por NIF

(9) Mostrar alumnos aprobados

(10) Mostrar alumnos suspensos

(X) Finalizar Programa
""")
        if opcion == "1":
            anyadiralumno()
        if opcion == "2":
            eliminaralumno()
        if opcion == "3":
            modificaralumno()
        if opcion == "4":
            mostrardatospornif()
        if opcion == "5":
            mostrardatosporemail()
        if opcion == "6":
            listaralumnos()
        if opcion == "7":
            aprobaralumno()
        if opcion == "8":
            aprobados()
        if opcion == "9":
            suspensos()
        if opcion == "X":
            Cortar = False
        else:
            print("Opción incorrecta")
            
