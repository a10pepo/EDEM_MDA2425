FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3

WORKDIR /app

COPY script.py /app/script.py

ENTRYPOINT [ "python3","script.py" ]
