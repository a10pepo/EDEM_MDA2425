from kafka import KafkaConsumer, KafkaProducer
import json
import logging

class Consumer:
    def __init__(self, topic, output_topic):
        self.topic = topic
        self.output_topic = output_topic
        self._consumer = KafkaConsumer(
            topic,
            bootstrap_servers='localhost:9092',
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True
        )

        self.producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.data = []

    @property
    def consumer(self):
        return self._consumer

    @consumer.setter
    def consumer(self, value):
        if isinstance(value, KafkaConsumer):
            self._consumer = value

    def start_read(self):
        self.receive_message()

    def receive_message(self):
        message_count = 0
        for message in self._consumer:
            message = message.value

            # Añadimos campo "alert" si la medalla es de oro
            if message.get("medal", "").strip().lower() == "gold":
                message["alert"] = "GOLD_MEDAL"
            else:
                message["alert"] = None

            logging.info(f"Mensaje {message_count}: {message}")
            self.data.append(message)
            self._send_to_topic(message)
            message_count += 1

    def _send_to_topic(self, message):
        self.producer.send(self.output_topic, value=message)
        logging.info(f"Mensaje enviado a {self.output_topic}: {message}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    consumer = Consumer('olympics.raw', 'olympics.proc')
    try:
        consumer.start_read()
    except KeyboardInterrupt:
        logging.info("Proceso interrumpido por el usuario.")
