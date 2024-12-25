import time
from json import dumps
from confluent_kafka import Producer

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)


# Send 100 messages where the key is the index and the message to send is "test message - index"
# the topic name is myTopic

topic_kafka = 'ventas'

for e in range(100):
    data = {'Nueva Venta - ': e*4}
    data_str = dumps(data)  # Serialize dictionary to a string ((json))
    data_bytes = data_str.encode('utf-8')  # Encode string to bytes // transformar el mensaje "data"
    key = str(e).encode('utf-8')
    producer.produce(topic=topic_kafka, value=data_bytes, key=key)  # Send bytes // produce() => producir mensaje
    print("Sending data: {} to topic {}".format(data, topic_kafka))
    time.sleep(1) ## la velocidad en la que envía (1 sec)

# After your loop where you send messages:
producer.flush() ## asegurar que todos los mensajes se han enviado. "Que no se espere a nada y se envíe de inmediato"

# Optionally, you can check if there are any messages that failed to be delivered:
if producer.flush() != 0:
    print("Some messages failed to be delivered") ## si algún mensaje se ha quedado "atascado"

