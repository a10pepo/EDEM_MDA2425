FROM python:latest
WORKDIR /app
COPY api-flask.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "api-flask.py"]
