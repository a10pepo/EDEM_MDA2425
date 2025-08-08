FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3
RUN pip install pymongo psycopg2-binary

WORKDIR /app
COPY script.py /app

ENTRYPOINT ["python3", "script.py"]