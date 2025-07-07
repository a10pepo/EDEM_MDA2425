from confluent_kafka import Consumer, KafkaError
import json

config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'retail-consumer-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(config)
topic = 'retail'
consumer.subscribe([topic])

try:
    print("▶️  Listening to topic 'retail'...")
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print("Error receiving message:", msg.error())
        else:
            data = json.loads(msg.value().decode('utf-8'))
            print(f" New message: {data}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
    print("🛑 Consumer closed.")
