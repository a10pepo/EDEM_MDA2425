from confluent_kafka import Consumer, Producer, KafkaError
import json
from collections import defaultdict
import time
from datetime import datetime

config_c = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}
consumer = Consumer(config_c)

topic_kafka = 'chat'
consumer.subscribe([topic_kafka])

config_p = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}
producer = Producer(config_p)
topic_kafka_out = 'filtered_chat'

bad_words = ['asshole', 'bitch', 'cunt', 'jerk']  

def contains_bad_word(message, bad_words):
    return any(bad_word in message for bad_word in bad_words)

def replace_bad_words(message, bad_words):
    for word in bad_words:
        message = message.replace(word, '*' * len(word))
    return message

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
            message_data = json.loads(msg.value().decode('utf-8'))

            if 'message' in message_data and contains_bad_word(message_data['message'], bad_words):
                    print(f"This message contains a bad word: {message_data['message']}")

                    filtered_message = replace_bad_words(message_data['message'], bad_words)
                    message_data['message'] = filtered_message
                    print(f"Filtered message: {filtered_message}")

                    producer.produce(topic=topic_kafka_out, value=json.dumps(message_data).encode('utf-8'))
                    producer.flush()

except KeyboardInterrupt:
    pass
finally:
    consumer.close()


