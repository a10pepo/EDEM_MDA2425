import csv
import random
from faker import Faker
import string

# Inicializamos Faker con configuración para español
fake = Faker('es_ES')

# Ruta del archivo CSV
csv_file = "alumnos_es.csv"

# Función para generar un NIF válido
def generar_nif():
    numeros = f"{random.randint(10000000, 99999999)}"# 8 dígitos
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"  # Secuencia de letras para cálculo del dígito de control
    letra = letras[int(numeros) % 23]
    return f"{numeros}{letra}"

# Función para generar un teléfono móvil español
def generar_telefono():
    prefijo = random.choice(['6', '7'])  # Prefijos para móviles en España
    return f"{prefijo}{str(random.randint(100000000, 999999999))[1:]}"

# Generar 30 alumnos con datos aleatorios
alumnos = []
for _ in range(30):
    nif = generar_nif()
    nombre = fake.first_name()
    apellidos = f"{fake.last_name()} {fake.last_name()}"
    telefono = generar_telefono()
    email = fake.email()
    aprobado = random.choice([True, False])
    alumnos.append([nif, nombre, apellidos, telefono, email, aprobado])

# Escribir los datos en el archivo CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Escribir la cabecera
    writer.writerow(["NIF", "Nombre", "Apellidos", "Teléfono", "Email", "Aprobado"])
    # Escribir los datos
    writer.writerows(alumnos)

print(f"Archivo {csv_file} generado con 30 ejemplos adaptados a España.")
