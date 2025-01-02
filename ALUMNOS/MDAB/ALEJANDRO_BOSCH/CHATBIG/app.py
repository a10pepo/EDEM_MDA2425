from flask import Flask, request, jsonify
from confluent_kafka import Producer, Consumer, KafkaException
import json
import time

app = Flask(__name__)

#Configuración de kafka
KAFKA_BROKER = "kafka:29092" #como estamos usando la api en un docker, se ejecuta fuera del pc, por tanto ya no es localhost.
KAFKA_INPUT_TOPIC = "chat"
KAFKA_OUTPUT_TOPIC = "chat_controlled"
KAFKA_GROUP = "python-consumer-group"

#Configuracion del productor
producer_conf = {
    'bootstrap.servers': KAFKA_BROKER,
    'client.id': 'flask-producer'
}
producer = Producer(producer_conf)

# Configuración del consumidor
consumer_conf = {
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': KAFKA_GROUP,
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_conf)
consumer.subscribe([KAFKA_OUTPUT_TOPIC])


# Endpoint para enviar mensajes a Kafka
@app.route('/send', methods=['POST'])
def send_message():
    try:
        data = request.json
        author = data.get('author', 'unknown')
        message = data.get('message', '')

        # Estructura del mensaje
        payload = {
            "author": author,
            "data": message,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        # Enviar a Kafka
        producer.produce(
            KAFKA_INPUT_TOPIC,
            key=author.encode('utf-8'),
            value=json.dumps(payload).encode('utf-8')
        )
        producer.flush()
        return jsonify({"status": "success", "message": "Message sent"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Endpoint para recibir mensajes de Kafka
@app.route('/receive', methods=['GET'])
def receive_messages():
    """
    Endpoint para recibir mensajes validados de Kafka (topic 'chat_controlled').
    """
    messages = []
    try:
        while True:
            msg = consumer.poll(1.0)  # Esperar 1 segundo para recibir mensajes
            if msg is None:
                break
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    break
                else:
                    raise KafkaException(msg.error())
            else:
                data = json.loads(msg.value().decode('utf-8'))
                messages.append(data)

        return jsonify({"status": "success", "messages": messages}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)