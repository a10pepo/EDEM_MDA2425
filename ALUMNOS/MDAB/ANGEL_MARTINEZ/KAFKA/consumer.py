from confluent_kafka import Consumer, Producer, KafkaError
import json
import time

consumer_config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_config)

topic = 'netflix'
consumer.subscribe([topic])

producer_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}
producer = Producer(producer_config)
topic_peliculas = 'movies'
topic_series = 'tv_shows'

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            netflix = json.loads(msg.value().decode('utf-8'))

            # Filtrar y enviar a los topics correspondientes
            if netflix['type'] == "Movie":
                print(f"The title {netflix['title']} is a movie, sending to 'movies'.")
                producer.produce(topic=topic_peliculas, value=json.dumps(netflix).encode('utf-8'))
            elif netflix['type'] == "TV Show":
                print(f"The title {netflix['title']} is a TV show, sending to 'tv_shows'.")
                producer.produce(topic=topic_series, value=json.dumps(netflix).encode('utf-8'))
            producer.flush()

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
