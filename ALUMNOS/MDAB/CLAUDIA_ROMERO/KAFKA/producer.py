import csv
import time
from json import dumps
from confluent_kafka import Producer

config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}
producer = Producer(config)
topic_kafka = 'pokemon'

with open("pokemon_data.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        message = {
            "pokemon": row["Name"],
            "type_1": row["Type 1"],
            "type_2": row["Type 2"] if row["Type 2"] else None,
            "hp": int(row["HP"]),
            "attack": int(row["Attack"]),
            "defense": int(row["Defense"]),
            "speed": int(row["Speed"]),
            "generation": int(row["Generation"]),
            "legendary": row["Legendary"] == "TRUE"
        }

        producer.produce(topic_kafka, key=row["Name"], value=dumps(message))
        print(f"Mensaje enviado: {message}")
        time.sleep(0.3)

if producer.flush() == 0:
    print("✅ Todos los mensajes fueron enviados correctamente")
else:
    print("❌ Algunos mensajes no pudieron ser enviados correctamente")