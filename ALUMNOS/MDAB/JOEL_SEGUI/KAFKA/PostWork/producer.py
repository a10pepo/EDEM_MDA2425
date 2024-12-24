import time
from confluent_kafka import Producer
from datetime import datetime

from simulador_regadio import generate_msg, generate_place

# Configuración del productor

#CREACION VARIABLE
config = {
    'bootstrap.servers': 'localhost:9092',  
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)

topic_kafka = 'Estados_Presion'

for e in range(10):
    msg = generate_msg()
    data = f"{msg} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    key = generate_place()
    producer.produce(topic=topic_kafka, value=data, key=key)  
    print("Sending data: {} [{}] to topic {}".format(data, key, topic_kafka))
    time.sleep(20)


producer.flush() #Para liberar memoria ram

# Optionally, you can check if there are any messages that failed to be delivered:
if producer.flush() != 0:
    print("Some messages failed to be delivered")
