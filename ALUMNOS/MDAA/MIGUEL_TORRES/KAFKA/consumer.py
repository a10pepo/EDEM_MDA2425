from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'temperaturas',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='grupo-temperaturas',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Esperando mensajes...\n")
for message in consumer:
    print(f"Recibido: {message.value}")
