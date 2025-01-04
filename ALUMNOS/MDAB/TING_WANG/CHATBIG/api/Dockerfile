FROM python:latest
WORKDIR /app
COPY api-flask.py .
RUN pip install --no-cache -r requirements.txt
EXPOSE 5000
CMD ["python", "api-flask.py"]
