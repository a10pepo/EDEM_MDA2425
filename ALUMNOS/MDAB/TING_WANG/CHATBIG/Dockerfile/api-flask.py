from flask import Flask, request, jsonify
from datetime import datetime
import json
from confluent_kafka import Producer, Consumer, KafkaError

app = Flask(__name__)

config = {
    'bootstrap.servers': 'kafka:9092',
    'client.id': 'python-producer'
}
producer = Producer(config)

topic_in = 'chat'
topic_out = 'chat_controlled'

config_c = {
    'bootstrap.servers': 'kafka:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}
consumer = Consumer(config_c)
consumer.subscribe([topic_out])

## POST
@app.route('/send_message', methods=['POST'])
def send_message():
    username = "user_1"
    message_data = request.get_json()
    user_message = message_data.get('message')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message_data = {
        "author" : username,
        "message": user_message,
        "timestamp": timestamp
    }
    producer.produce(topic=topic_in, key=username, value=json.dumps(message_data).encode('utf-8'))
    producer.flush()
    return 'Message sent to Kafka', 200

## GET
@app.route('/get_filtered_messages', methods=['GET'])
def get_filtered_messages():
    msg = consumer.poll(1.0)

    if msg is None:
        return jsonify({"message": "No messages available"}), 200
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            return jsonify({"message": "End of partition reached"}), 200
        else:
            return jsonify({"error": str(msg.error())}), 400
        
    message = json.loads(msg.value().decode('utf-8'))
    filtered_message = message.get("message","")

    if filtered_message:
        return jsonify({"message": filtered_message}), 200
    else:
        return jsonify({"message": "No messages available"}), 200


if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    finally:
        consumer.close()
