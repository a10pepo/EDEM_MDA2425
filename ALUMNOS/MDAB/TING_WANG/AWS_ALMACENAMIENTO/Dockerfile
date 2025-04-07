FROM python:3.11-slim

COPY app_jacinto /app/app_jacinto

WORKDIR /app/app_jacinto

RUN apt-get update && apt-get install -y gcc python3-dev libpq-dev libsnappy-dev libzstd-dev
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "main"]