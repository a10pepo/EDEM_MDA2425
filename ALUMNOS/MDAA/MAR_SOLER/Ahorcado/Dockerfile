FROM python:3.14.0a2-alpine3.20
RUN pip install pg8000
WORKDIR /Ahorcado
COPY ahorcado.py /Ahorcado
COPY palabras.txt /Ahorcado
ENTRYPOINT ["python", "ahorcado.py","palabras.txt"]