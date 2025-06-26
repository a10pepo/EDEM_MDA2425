FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo requirements.txt
COPY requirements.txt /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Install curl
RUN apt-get update && apt-get install -y curl

# Now download the script and make it executable
RUN curl -o /wait-for-it.sh https://github.com/vishnubob/wait-for-it/raw/master/wait-for-it.sh && chmod +x /wait-for-it.sh

# Copiar el resto de los archivos de la aplicación
COPY . /app/

# Comando para ejecutar la aplicación
CMD ["python", "game.py"]

