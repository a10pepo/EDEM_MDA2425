FROM python:3.11-slim

RUN pip install pg8000

WORKDIR /app

COPY game.py /app

CMD [ "python3","game.py" ]