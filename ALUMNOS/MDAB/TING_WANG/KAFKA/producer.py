import csv
import time
from json import dumps
from confluent_kafka import Producer

config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}
producer = Producer(config)

topic_kafka = 'movies'


with open('IMDB_Movies_Dataset.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        try:
            row['Average Rating'] = float(row['Average Rating']) if row['Average Rating'] else None
        except ValueError:
            row['Average Rating'] = None
        try:
            row['Metascore'] = float(row['Metascore']) if row['Metascore'] else None
        except ValueError:
            row['Metascore'] = None
        try:
            row['Budget'] = float(row['Budget'].replace('$', '').replace(',', '').strip()) if row['Budget'] else None
        except ValueError:
            row['Budget'] = None
        try:
            row['Worldwide Gross'] = float(row['Worldwide Gross'].replace('$', '').replace(',', '').strip()) if row['Worldwide Gross'] else None
        except ValueError:
            row['Worldwide Gross'] = None
        if row['Runtime']:
            runtime_parts = row['Runtime'].split(' ')
            if len(runtime_parts) == 4:
                hours = int(runtime_parts[0])
                minutes = int(runtime_parts[2])
                row['Runtime'] = hours * 60 + minutes
            elif len(runtime_parts) == 2:
                row['Runtime'] = int(runtime_parts[0])
            else:
                row['Runtime'] = None
        else:
            row['Runtime'] = None
        data_str = dumps(row)
        data_bytes = data_str.encode('utf-8')
        key = str(row['Title']).encode('utf-8')
        print(f"Enviando al productor Kafka: {data_str}")

        producer.produce(topic=topic_kafka, value=data_bytes, key=key)
        print("Sending data: {} to topic {}".format(data_str, topic_kafka))
        time.sleep(3)
        producer.flush()

producer.flush()
if producer.flush() != 0:
    print("Some messages failed to be delivered")

