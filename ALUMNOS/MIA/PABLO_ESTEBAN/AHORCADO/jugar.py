import sys
from ahorcado import Ahorcado

ABECEDARIO = "abcdefghijklmnñopqrstuvwxyz"

import psycopg2

# Configuración de conexión
connection = psycopg2.connect(
    host="postgres",         # O el nombre del servicio en docker-compose, p. ej. "db"
    port="5432",
    database="mydatabase",    # Nombre de tu base de datos
    user="postgres",          # Usuario de PostgreSQL
    password="example"        # Contraseña de PostgreSQL
)

# Crear un cursor para ejecutar comandos SQL
cursor = connection.cursor()

# Ejemplo de consulta SELECT
query = "SELECT * FROM tabla_ejemplo;"  # Cambia 'tabla_ejemplo' por el nombre de tu tabla
cursor.execute(query)

# Obtener resultados
rows = cursor.fetchall()  # fetchall() devuelve todas las filas
for row in rows:
    print(row)  # Procesa cada fila (puedes personalizar el procesamiento)

# Cerrar el cursor y la conexión
cursor.close()
connection.close()



def main():
    
    filename = sys.argv[1] if len(sys.argv) > 1 else "palabras.txt"
    numero_intentos = 0

    with open(filename) as f:
        for palabra in f.readlines():
            palabra = palabra.strip()
            print("\n", palabra)
            ahorcado = Ahorcado(palabra)

            for letra in ABECEDARIO:
                if ahorcado.try_letter(letra):
                    if ahorcado.won():
                        numero_intentos += ahorcado.tries
                        break

            print(ahorcado)

    print(f"Intentos Totales: {numero_intentos}")

if __name__ == "__main__":
    main()