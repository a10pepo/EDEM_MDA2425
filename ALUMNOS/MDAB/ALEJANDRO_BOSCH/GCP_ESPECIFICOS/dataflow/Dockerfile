FROM gcr.io/dataflow-templates-base/python310-template-launcher-base:latest

WORKDIR /pipeline

# Copiar archivos necesarios
COPY requirements.txt .
COPY edem_dataflow_pipeline.py .

# Definir variables de entorno para Flex Templates
ENV FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE=/pipeline/requirements.txt
ENV FLEX_TEMPLATE_PYTHON_PY_FILE=/pipeline/edem_dataflow_pipeline.py

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Punto de entrada: se ejecutará el archivo Python definido
ENTRYPOINT ["python", "/pipeline/edem_dataflow_pipeline.py"]
