from kafka import KafkaProducer
import json
import time
import random

def generate_order():
    products = ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse']
    order = {
        "order_id": random.randint(1000, 9999),
        "product": random.choice(products),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(50, 500), 2),
        "timestamp": time.time()
    }
    return order

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

if __name__ == "__main__":
    topic = "raw_orders"
    while True:
        order = generate_order()
        print(f"Sending: {order}")
        producer.send(topic, value=order)
        time.sleep(1)  # Envía un pedido cada segundo
