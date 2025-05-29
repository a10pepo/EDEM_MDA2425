from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:29092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

locations = ["Valencia", "Madrid", "Barcelona"]

print("Starting producer... Press Ctrl+C to stop")

while True:
    try:
        data = {
            "sensor_id": f"sensor_{random.randint(100, 999)}",
            "location": random.choice(locations),
            "temperature": round(random.uniform(-10, 45), 2),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        }
        
        producer.send("raw_temperatures", data)
        print(f"Produced: {data}")
        time.sleep(2)
        
    except KeyboardInterrupt:
        print("\nStopping producer...")
        break
    except Exception as e:
        print(f"Error: {e}")
        break

producer.close()