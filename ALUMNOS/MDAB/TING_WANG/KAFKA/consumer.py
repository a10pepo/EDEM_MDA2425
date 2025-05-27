from confluent_kafka import Consumer, Producer, KafkaError
import json
import time

consumer_config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_config)

topic = 'movies'
consumer.subscribe([topic])

producer_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}
producer = Producer(producer_config)
topic_processed = 'movies_rating'

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
            movie_data = json.loads(msg.value().decode('utf-8'))

            # Filtrar las películas con rating > 8
            if float(movie_data['Average Rating']) > 8:
                print(f"Movie {movie_data['Title']} has a rating above 8, sending to 'movies_rating'.")
                
                producer.produce(topic=topic_processed, value=json.dumps(movie_data).encode('utf-8'))
                producer.flush()

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
