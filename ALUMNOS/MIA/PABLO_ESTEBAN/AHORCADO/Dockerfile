FROM python:latest

# Definir una variable de construcción
ARG PALABRAS_FILE_ARG=palabras.txt

# Establecer una variable de entorno usando el argumento
ENV PALABRAS_FILE=$PALABRAS_FILE_ARG

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY ahorcado.py .
COPY jugar.py .
COPY $PALABRAS_FILE .

# Ejecutar el archivo principal
CMD ["python", "jugar.py"]

# docker build -t ahorcado .
# docker run ahorcado