'''
- Lea las palabras de un fichero de texto, una por línea
- Busque cada palabra y retorne los intentos necesarios para adivinarla
- Se pueda ejecutar con el siguiente comando: `python ahorcado.py palabras.txt`
'''
import sys #para que pueda leer por la línea de comandos
import pg8000.native #para crear una tabla en SQL
import datetime #para saber la hora

con = pg8000.native.Connection("postgres", password="Welcome01", host="postgres_container") #conexión con la base de datos postgres


abecedario_es_mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


with open (sys.argv[1], 'r') as archivo: #Abrimos el archivo; sys.argv[1] es el archivo que le metamos en la terminal
        palabras=archivo.read().split() #lee el archivo, lo separa por palabra; el split es para eliminar los saltos de línea (/n)

intentos=0 #inicializamos intentos


for palabra in palabras: #Bucle que me coge cada palabra dentro de la cadena de palabras que hemos leído del archivo
    long=len(palabra)   #longitud de la palabra
    letras_acertadas="" #inicializamos la cadena de letras_acertadas para la tabla sql
    letras_falladas=""
    for letra in abecedario_es_mayus:   #bucle para que recorra cada letra del abecedario
        if long>0:  #si long (palabras que quedan por adivinar) es mayor a 0 seguimos intentando adivinar la palabra
            
            intentos+=1 #suma 1 a los intentos
            if letra in palabra:    #si la letra del abecedario que estemos usando ahora en el bucle coincide con una letra de la variable palabra
                long=long-palabra.count(letra)  #restamos las letras adivinadas a la longitud (el count es por si hay más de una vez la misma letra)
                letras_acertadas=letras_acertadas+letra #vamos creando una cadena con las letras acertadas para crear la tabla sql
                tiempo=datetime.datetime.now()  
                con.run("INSERT INTO ahorcado (palabra,letras_acertadas, letras_falladas, intentos, tiempo) VALUES (:palabra,:letras_a, :letras_f, :i, :tiempo)", palabra=palabra, letras_a=letras_acertadas, letras_f=letras_falladas, i=intentos, tiempo=tiempo)
                #Inserta datos a la tabla ahorcado que ya habiamos creado en las columnas (entre parentesis), los valores (puente entre las columnas y las vbles) y igualamos los valores puente a las vbles que hemos ido creando
            else:   #sino se acierta 
                tiempo=datetime.datetime.now()
                con.run("INSERT INTO ahorcado (palabra, letras_acertadas, letras_falladas, intentos, tiempo) VALUES (:palabra,:letras_a, :letras_f, :i, :tiempo)", palabra=palabra, letras_a=letras_acertadas, letras_f=letras_falladas, i=intentos, tiempo=tiempo)
                letras_falladas=letras_falladas+letra   #la letra intentada pero fallada se va sumando a la cadena de letras falladas, dato columna sql
print(intentos)


