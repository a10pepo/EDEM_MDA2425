from confluent_kafka import Producer
import json

class KafkaMessageConsumer:
    def __init__(self, topic, server="localhost:9092"):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=server,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            auto_offset_reset="earliest",
            group_id="chat-group",
        )

    def consume_messages(self):
        for message in self.consumer:
            yield message.value

# Ejemplo de uso:
# consumer = KafkaMessageConsumer(topic="chat_topic")
# for msg in consumer.consume_messages():
#     print(msg)