# Usa una imagen base de Python 3.11 en su versión "slim"
FROM python:3.11-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY pysum.py .

# Lanza pysum.py
ENTRYPOINT [ "python3", "pysum.py"] 