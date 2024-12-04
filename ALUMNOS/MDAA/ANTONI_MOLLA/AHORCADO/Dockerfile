FROM python:3.10-alpine

RUN pip install pg8000

WORKDIR /
COPY ahorcado.py /ahorcado.py
COPY palabras.txt /palabras.txt


CMD [ "python3","ahorcado.py","palabras.txt" ]
