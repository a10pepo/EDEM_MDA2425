FROM python:3.10.15-alpine3.20

RUN pip install pg8000

WORKDIR /WORKSPACE

COPY ahorcado.py /WORKSPACE
COPY palabras.txt /WORKSPACE

CMD ["python", "ahorcado.py", "palabras.txt"]