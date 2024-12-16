from kafka import KafkaProducer
import json

class KafkaMessageProducer:
    def __init__(self, topic, server="localhost:9092"):
        self.producer = KafkaProducer(
            bootstrap_servers=server,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        self.topic = topic

    def send_message(self, message):
        self.producer.send(self.topic, message)
        self.producer.flush()

# Ejemplo de uso:
# producer = KafkaMessageProducer(topic="chat_topic")
# producer.send_message({"user": "Carlos", "message": "¡Hola a todos!"})