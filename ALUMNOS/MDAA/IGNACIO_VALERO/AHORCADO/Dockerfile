FROM python:3.10.15-alpine3.20
RUN pip install pg8000
WORKDIR /ETE
COPY palabras.txt /ETE
COPY ahorcado.py /ETE
CMD ["python", "ahorcado.py","palabras.txt"]
#ENTRYPOINT ["python", "ahorcado.py"]