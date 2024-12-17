from confluent_kafka import Producer

def create_producer():
    config = {
        'bootstrap.servers': 'localhost:9092', 
        'client.id': 'python-producer'
    }
    return Producer(config)

def send_message(producer, topic, key, value):
    producer.produce(topic=topic, value=value, key=key)
    producer.flush()  
