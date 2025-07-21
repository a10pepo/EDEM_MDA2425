# Usa una imagen base oficial con Python
FROM python:3.11-slim

# Evita que Python guarde archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV USERNAME=andreu


# Instala dependencias necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Crea un directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY metaflow_trainingflow.py ./

# Instala las dependencias de Python
RUN pip install --no-cache-dir metaflow scikit-learn joblib

# Comando por defecto para ejecutar el flujo
CMD ["python", "metaflow_trainingflow.py", "run"]
