from confluent_kafka import Producer
import json
import time

# Configure the Kafka Producer
def delivery_report(err, msg):
    """Called once for each message produced to indicate delivery result"""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

producer = Producer({'bootstrap.servers': 'localhost:9092'})

# Sample order data to simulate food delivery events
orders = [
    {
        "order_id": "12345",
        "customer_id": "67890",
        "restaurant": "Pizza Palace",
        "order_time": "2025-01-09T14:30:00Z",
        "status": "Order Received"
    }
]

# Send the order data to the Kafka topic
for order in orders:
    producer.produce('raw_orders', key=str(order['order_id']), value=json.dumps(order), callback=delivery_report)
    producer.flush()  # Ensure the message is sent before continuing
    time.sleep(1)  # Simulate real-time ingestion