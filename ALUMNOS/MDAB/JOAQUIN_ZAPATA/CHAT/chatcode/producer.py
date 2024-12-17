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

topic_kafka = 'chat'

for e in range(100):
    data = {'message': f'test message - {e}'}  # Define data as a dictionary with the message
    data_str = dumps(data)  # Serialize dictionary to a string
    data_bytes = data_str.encode('utf-8')  # Encode string to bytes
    key = str(e).encode('utf-8')
    producer.produce(topic=topic_kafka, value=data_bytes, key=key)  # Send bytes
    print(f"Sending data: {data} to topic {topic_kafka}")
    time.sleep(1)

# After your loop where you send messages:
producer.flush()

# Optionally, you can check if there are any messages that failed to be delivered:
if producer.flush() != 0:
    print("Some messages failed to be delivered")
