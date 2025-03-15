import csv
import time
from json import dumps
from confluent_kafka import Producer
from datetime import datetime

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}
producer = Producer(config)
topic_kafka = 'netflix'

def clean_data(row):
    # Manejar valores nulos
    row['director'] = row['director'] if row['director'] else "Unknown"
    row['cast'] = row['cast'] if row['cast'] else "Unknown"
    row['country'] = row['country'] if row['country'] else "Unknown"
    row['date_added'] = row['date_added'] if row['date_added'] else None
    row['rating'] = row['rating'] if row['rating'] else "Unrated"
    
    # Normalizar fecha
    if row['date_added']:
        try:
            row['date_added'] = datetime.strptime(row['date_added'], "%B %d, %Y").isoformat()
        except ValueError:
            row['date_added'] = None

    # Procesar la duración
    if row['duration']:
        if "min" in row['duration']:
            row['duration'] = int(row['duration'].replace('min', '').strip())  # Duración en minutos
            row['content_type'] = "Movie"  # Inferido como película
        elif "Season" in row['duration']:
            row['duration'] = int(row['duration'].split()[0])  # Número de temporadas
            row['content_type'] = "TV Show"  # Inferido como serie
        else:
            row['duration'] = None
            row['content_type'] = "Unknown"
    else:
        row['duration'] = None
        row['content_type'] = "Unknown"

    return row

with open('netflix_titles.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        # Limpiar y normalizar datos
        row = clean_data(row)
        message = dumps(row)
        try:
            producer.produce(topic_kafka, value=message)
            print(f"Mensaje enviado: {message}")
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")
        time.sleep(0.6)

producer.flush()
if producer.flush() != 0:
    print("Algunos mensajes no se entregaron correctamente.")
