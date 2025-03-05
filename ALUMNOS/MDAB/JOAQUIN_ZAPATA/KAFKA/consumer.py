from kafka import KafkaConsumer, KafkaProducer
import json

print("Starting consumer...")

consumer = KafkaConsumer(
    "raw_temperatures",
    bootstrap_servers="localhost:29092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id="temperature_processor"
)

producer = KafkaProducer(
    bootstrap_servers="localhost:29092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Consumer connected. Waiting for messages...")

try:
    for message in consumer:
        print("Received message:", message.value)
        data = message.value
        
        if -50 <= data["temperature"] <= 50:
            data["status"] = "valid"
            producer.send("processed_temperatures", data)
            print(f"Processed: {data}")
        else:
            print(f"Invalid temperature value: {data['temperature']}")

except KeyboardInterrupt:
    print("\nStopping consumer...")
except Exception as e:
    print(f"Error: {e}")
finally:
    consumer.close()
    producer.close()