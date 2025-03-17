from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'final_orders',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

if __name__ == "__main__":
    for message in consumer:
        order = message.value
        print(f"Final Order: {order}")
