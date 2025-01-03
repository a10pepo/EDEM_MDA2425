FROM python:3.12-slim

# Instalar dependencias
RUN pip install flask confluent-kafka

# Copiar los archivos al contenedor
WORKDIR /app
COPY . /app

# Exponer el puerto para la API
EXPOSE 5000

# Comando para iniciar la API
CMD ["python", "app.py"]
