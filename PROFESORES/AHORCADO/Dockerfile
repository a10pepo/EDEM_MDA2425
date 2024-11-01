FROM python:latest

WORKDIR /app

COPY ahorcado.py .
COPY palabras.txt .

RUN pip3 install pg8000

CMD ["python", "ahorcado.py", "palabras.txt"]
