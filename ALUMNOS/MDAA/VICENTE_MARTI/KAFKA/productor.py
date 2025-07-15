from confluent_kafka import Producer
import json
import time


TOPIC = "signos_vitales_raw"
BROKER = "localhost:9092"

producer = Producer({'bootstrap.servers': BROKER})

def delivery_report(err, msg):
    if err:
        print(f"Error al enviar mensaje: {err}")
    else:
        print(f"Mensaje enviado: {msg.value().decode('utf-8')}")


with open("lecturas_vitales.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)  
            producer.produce(
                TOPIC,
                value=json.dumps(data),
                callback=delivery_report
            )
            producer.flush()
            time.sleep(0.2) 
        except json.JSONDecodeError:
            print(f"JSON inválido: {line}")
