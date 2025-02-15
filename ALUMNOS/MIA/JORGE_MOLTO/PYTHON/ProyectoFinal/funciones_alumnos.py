import pandas as pd

# Ruta al archivo CSV
CSV_FILE = "alumnos_es.csv"

# Función para cargar alumnos desde el CSV
def cargar_alumnos():
    try:
        # Cargar el CSV directamente en un DataFrame
        df = pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        # Si no existe el archivo, retornamos un DataFrame vacío
        df = pd.DataFrame(columns=["NIF", "Nombre", "Apellidos", "Teléfono", "Email", "Aprobado"])
    return df

# Función para guardar alumnos en el CSV
def guardar_alumnos(df):
    # Guardar el DataFrame en el archivo CSV
    df.to_csv(CSV_FILE, index=False)

def añadir_alumno(df, nuevo_alumno):
    # Convertir el diccionario de nuevo_alumno en un DataFrame de una sola fila
    nuevo_alumno_df = pd.DataFrame([nuevo_alumno])  # Convertir el diccionario en DataFrame de una sola fila
    df = pd.concat([df, nuevo_alumno_df], ignore_index=True)  # Concatenar el nuevo DataFrame al original
    guardar_alumnos(df)  # Guardar el DataFrame actualizado
    return df


# Función para eliminar un alumno por NIF
def eliminar_alumno(df, nif):
    # Eliminar la fila cuyo NIF coincida con el proporcionado
    df = df[df["NIF"] != nif]
    guardar_alumnos(df)

# Función para actualizar los datos de un alumno por NIF
def actualizar_alumno(df, nif, nuevos_datos):
    # Buscar el índice del alumno por NIF y actualizar los datos
    df.loc[df["NIF"] == nif, list(nuevos_datos.keys())] = list(nuevos_datos.values())
    guardar_alumnos(df)
    return df

# Función para buscar un alumno por NIF
def buscar_alumno_por_nif(df, nif):
    # Buscar el alumno por NIF
    alumno = df[df["NIF"] == nif]
    if not alumno.empty:
        return alumno.iloc[0]  # Devolver el primer registro encontrado
    else:
        return None  # Si no se encuentra, devolver None


# Función para buscar un alumno por Email
def buscar_alumno_por_email(df, email):
    # Buscar el alumno por Email
    alumno = df[df["Email"] == email]
    return alumno.iloc[0] if not alumno.empty else None

# Función para listar todos los alumnos
def listar_alumnos(df):
    # Devolver el DataFrame completo
    return df

# Función para cambiar el estado de aprobado por NIF
def cambiar_estado_aprobado(df, nif, aprobado):
    # Cambiar el valor de "Aprobado" para el alumno con el NIF correspondiente
    df.loc[df["NIF"] == nif, "Aprobado"] = aprobado
    guardar_alumnos(df)
    return df

# Función para listar alumnos aprobados o suspensos
def listar_alumnos_por_estado(df, aprobado):
    # Filtrar los alumnos según el estado de "Aprobado"
    return df[df["Aprobado"] == aprobado]
