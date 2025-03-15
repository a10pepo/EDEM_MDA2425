from confluent_kafka import Consumer, Producer, KafkaError
import time
from json import dumps

with open('transferencias.txt', 'r') as fichero:
    transferencia_json = fichero.read()

# PRODUCTOR

config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

producer = Producer(config)


topic_kafka = 'transferencias'

for e in range(100):
    data = transferencia_json
    data_str = dumps(data)
    data_bytes = data_str.encode('utf-8')
    key = str(e).encode('utf-8')
    producer.produce(topic=topic_kafka, value=data_bytes, key=key)
    print("Sending data: {} to topic {}".format(data, topic_kafka))
    time.sleep(1)


producer.flush() ## asegurar que todos los mensajes se han enviado. "Que no se espere a nada y se envíe de inmediato"

if producer.flush() != 0:
    print("Some messages failed to be delivered") ## si algún mensaje se ha quedado "atascado"




