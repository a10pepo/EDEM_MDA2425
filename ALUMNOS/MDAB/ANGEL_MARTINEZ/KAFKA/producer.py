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
    row['director'] = row['director'] if row['director'] else "NA"
    row['cast'] = row['cast'] if row['cast'] else "NA"
    row['country'] = row['country'] if row['country'] else "NA"
    row['date_added'] = row['date_added'] if row['date_added'] else None
    row['rating'] = row['rating'] if row['rating'] else "NA"
    
    if row['date_added']:
        try:
            row['date_added'] = datetime.strptime(row['date_added'], "%B %d, %Y").isoformat()
        except ValueError:
            row['date_added'] = None

    if row['duration']:
        if "min" in row['duration']:
            row['duration'] = int(row['duration'].replace('min', '').strip())  
            row['content_type'] = "Movie"  
        elif "Season" in row['duration']:
            row['duration'] = int(row['duration'].split()[0])  
            row['content_type'] = "TV Show" 
        else:
            row['duration'] = None
            row['content_type'] = "NA"
    else:
        row['duration'] = None
        row['content_type'] = "NA"

    return row

with open('netflix_titles.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
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
