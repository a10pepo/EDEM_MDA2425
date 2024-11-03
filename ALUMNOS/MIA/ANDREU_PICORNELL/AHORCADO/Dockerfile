# Usa una imagen base de Python 3.11 en su versión "slim"
FROM python:3.11-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY ahorcado.py .
COPY palabras.txt .
COPY requirements.txt .

# Instala las dependencias de Python del proyecto (incluyendo psycopg2)
RUN pip install -r requirements.txt

# Lanza ahorcado.py
CMD [ "python3", "ahorcado.py"] 