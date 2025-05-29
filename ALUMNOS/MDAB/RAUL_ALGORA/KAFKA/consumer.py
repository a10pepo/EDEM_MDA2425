from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer(
    'raw_orders',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

if __name__ == "__main__":
    for message in consumer:
        order = message.value
        # Transformar: solo procesar pedidos con cantidad > 2
        if order['quantity'] > 2:
            order['status'] = 'processed'
            print(f"Processed: {order}")
            producer.send('processed_orders', value=order)
