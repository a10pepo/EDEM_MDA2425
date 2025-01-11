from confluent_kafka import Producer, Consumer, KafkaError
import json
from datetime import datetime
import requests

## Suscription to Kafka (direct flow, not through API)
config_c = {
    'bootstrap.servers': 'kafka:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}
consumer = Consumer(config_c)
topic_in = 'chat'
consumer.subscribe([topic_in])

config_p = {
    'bootstrap.servers': 'kafka:9092',
    'client.id': 'python-producer'
}
producer = Producer(config_p)
topic_out = "chat_controlled"

## samples of bad words
bad_words = ['asshole', 'bitch', 'cunt', 'jerk']  


def replace_bad_words(message, bad_words):
    filtered_message = message
    for word in bad_words:
        filtered_message = filtered_message.replace(word, '*' * len(word))
    return filtered_message

def produce_filtered_message(filtered_message):
    message_data = {
        "author": "user_1",
        "message": filtered_message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    producer.produce(topic=topic_out, key="user_1", value=json.dumps(message_data).encode('utf-8'))
    producer.flush()
    print("Mensaje filtrado enviado a Kafka.")


try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print(f"Error al recibir mensaje: {msg.error()}")
            continue

        message_data = json.loads(msg.value().decode('utf-8'))
        original_message = message_data.get("message", "")

        filtered_message = replace_bad_words(original_message, bad_words)
        produce_filtered_message(filtered_message)

except KeyboardInterrupt:
    print("Consumer stopped.")
finally:
    consumer.close()
