from confluent_kafka import Consumer, Producer, KafkaException, KafkaError
import json
from datetime import datetime

# Configure the Kafka Consumer
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'food_delivery_group',
    'auto.offset.reset': 'earliest'
})

# Configure the Kafka Producer to send transformed data
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# Subscribe to the raw_orders topic
consumer.subscribe(['raw_orders'])

# Consume the messages and transform them
def consume_and_process():
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
                order = json.loads(msg.value().decode('utf-8'))
                # Enrich the order data
                order['status'] = 'Out for Delivery'
                order['updated_time'] = datetime.utcnow().isoformat()
                order['driver'] = 'John Doe'

                # Send the enriched data to the processed_orders topic
                producer.produce('processed_orders', key=str(order['order_id']), value=json.dumps(order))
                producer.flush()
                print(f"Processed order: {order}")

    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        consumer.close()

# Run the consumer to process messages
consume_and_process()