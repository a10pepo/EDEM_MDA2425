from confluent_kafka import Consumer, KafkaException, KafkaError
import json

# Configure the Kafka Consumer for processed_orders
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'food_delivery_group',
    'auto.offset.reset': 'earliest'  # Start reading from the earliest message
})

# Subscribe to the processed_orders topic
consumer.subscribe(['processed_orders'])

# Function to consume and print messages from processed_orders
def consume_processed_orders():
    try:
        while True:
            msg = consumer.poll(1.0)  # Wait for a message (timeout: 1 second)
            if msg is None:  # No new message
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"End of partition reached {msg.topic()} [{msg.partition()}] @ {msg.offset()}")
                else:
                    raise KafkaException(msg.error())
            else:
                # Deserialize the message value and print it
                order = json.loads(msg.value().decode('utf-8'))
                print(f"Processed Order: {order}")
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        consumer.close()

# Run the consumer to print messages from processed_orders
consume_processed_orders()