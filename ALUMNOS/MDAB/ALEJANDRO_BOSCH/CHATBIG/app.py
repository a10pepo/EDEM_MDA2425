from flask import Flask, request, jsonify
from confluent_kafka import Producer, Consumer, KafkaError
import json
import time

app = Flask(__name__)

# Configuración de Kafka
KAFKA_SERVERS = 'kafka:29092'
TOPICS = ['chat', 'chat_controlled']

# Configuración del productor
producer_config = {
    'bootstrap.servers': KAFKA_SERVERS,
    'client.id': 'flask-producer-chat'
}

# Configuración del consumidor
consumer_config = {
    'bootstrap.servers': KAFKA_SERVERS,
    'group.id': 'flask-consumer-group-chat',
    'auto.offset.reset': 'earliest'
}

# Endpoint para enviar mensajes a Kafka
@app.route('/send', methods=['POST'])
def send_message():
    try:
        data = request.json
        message = data.get("message")
        author = data.get("author")

        if not message or not author:
            return jsonify({"status": "error", "message": "Faltan campos obligatorios"}), 400

        producer = Producer(producer_config)
        kafka_message = {
            "author": author,
            "message": message,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        message_bytes = json.dumps(kafka_message).encode('utf-8')

        for topic in TOPICS:
            producer.produce(topic=topic, value=message_bytes, key=author.encode('utf-8'))

        producer.flush()
        return jsonify({"status": "success", "message": "Mensaje enviado a Kafka"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Endpoint para recibir mensajes de Kafka
@app.route('/receive', methods=['GET'])
def receive_messages():
    try:
        consumer = Consumer(consumer_config)
        consumer.subscribe(TOPICS)
        messages = []

        for _ in range(10):  # Limitar la cantidad de mensajes recibidos
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                if msg.error().code() != KafkaError._PARTITION_EOF:
                    raise Exception(msg.error())
            else:
                kafka_message = json.loads(msg.value().decode('utf-8'))
                messages.append({
                    "topic": msg.topic(),
                    "author": kafka_message['author'],
                    "message": kafka_message['message'],
                    "timestamp": kafka_message['timestamp']
                })

        consumer.close()
        return jsonify(messages), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
