from confluent_kafka import Producer

def send_message_ui(producer, topic, value, key):
    producer.produce(topic=topic, value=value, key=key)
    producer.flush()

def create_pruductor():
    config = {
    'bootstrap.servers': '172.28.183.140:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
        }
    return Producer(config)


