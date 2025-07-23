FROM python:3.7

WORKDIR /app

COPY main.py /app

RUN pip install pymongo pg8000

CMD ["python3", "main.py"]