FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3

WORKDIR /app

COPY suma.py /app/suma.py

ENTRYPOINT ["python3", "suma.py" ]