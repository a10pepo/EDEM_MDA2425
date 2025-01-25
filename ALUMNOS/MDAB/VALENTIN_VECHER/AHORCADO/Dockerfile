FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY entrypoint.sh entrypoint.sh

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x entrypoint.sh

CMD ["/bin/sh", "/app/entrypoint.sh"]