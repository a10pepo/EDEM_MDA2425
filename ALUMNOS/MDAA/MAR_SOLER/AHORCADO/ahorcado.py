import sys
import pg8000.native
from datetime import datetime

# nos conectamos a pgadmin
con = pg8000.native.Connection("postgres",password="Welcome01", host="postgres")

# creamos abecedario
abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# creamos listado de palabras desde el txt que pongamos como argumento
with open(sys.argv[1]) as archivo:
    palabras = archivo.read().splitlines()

# definimos las variables que necesitaremos luego
intentos = 0
aciertos = 0
fallos = 0

# creamos la tabla por si no existe
con.run(
    """CREATE TABLE IF NOT EXISTS public.ahorcado(
    palabra character varying(50) COLLATE pg_catalog."default" NOT NULL,
    letras_acertadas character varying(50) COLLATE pg_catalog."default" NOT NULL,
    letras_falladas character varying(50) COLLATE pg_catalog."default" NOT NULL,
    intentos integer NOT NULL,
    fecha timestamp without time zone NOT NULL
    )""")

# vaciamos la tabla para que esté limpia para nuevos registros
con.run ("delete from public.ahorcado")

for palabra in palabras:
    # definición de variables
    letras = len(palabra)
    letra_acertada = ""
    letra_fallada = ""

    for letra in abc:   # bucle por palabra de cada letra del abecedario
        if letras > 0:
            fecha = datetime.now() # definimos cuándo se hace cada intento para meterlo en la tabla
            intentos = intentos + 1
            if letra in palabra:
                aciertos = aciertos + 1 # contamos los aciertos
                letras = letras - palabra.count(letra) # vamos restando las letras acertadas de cada palabra
                letra_acertada = letra_acertada + letra # concatenamos las letras que han pasado por aciertos
            else:
                fallos = fallos + 1 # contamos los fallos
                letra_fallada = letra_fallada + letra # concatenamos las letras que han pasado por fallos
            # código sql para que meta los datos en la tabla
            con.run("insert into public.ahorcado values (:palabra, :letras_acertadas, :letras_falladas, :intentos, :tiempo)", palabra=palabra, letras_acertadas=letra_acertada, letras_falladas=letra_fallada, intentos=intentos, tiempo=fecha)

# comprobamos los registros:
primer_registro = con.run ("select min(fecha) from public.ahorcado")
ultimo_registro = con.run ("select max(fecha) from public.ahorcado")

# extraemos los objetos datetime de las listas
primer_registro_datetime = primer_registro[0][0]
ultimo_registro_datetime = ultimo_registro[0][0]

# formateamos las fechas
primer_registro_str = primer_registro_datetime.strftime("el día %d/%m/%Y a las %H:%M:%S")
ultimo_registro_str = ultimo_registro_datetime.strftime("el día %d/%m/%Y a las %H:%M:%S")

# mostramos el resultado
print(f"De {intentos} intentos, hay {aciertos} aciertos y {fallos} fallos.")
print(f"El primer registro es {primer_registro_str} y el último es {ultimo_registro_str}")