FROM python:3.9-alpine

RUN pip install pg8000
COPY ahorcado.py /ahorcado.py
COPY palabras.txt /palabras.txt


WORKDIR /

CMD ["python", "ahorcado.py", "palabras.txt"]