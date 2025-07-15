from confluent_kafka import Consumer, Producer
import json


TOPIC_ORIGEN = "signos_vitales_raw"
TOPIC_DESTINO = "signos_vitales_procesados"
BROKER = "localhost:9092"
GROUP_ID = "procesador-signos-vitales"


consumer = Consumer({
    'bootstrap.servers': BROKER,
    'group.id': GROUP_ID,
    'auto.offset.reset': 'earliest'
})

producer = Producer({'bootstrap.servers': BROKER})

def es_riesgo_alto(data):
    return (
        data.get("frecuencia_cardiaca", 0) > 100 or
        data.get("presion_sistolica", 0) > 140 or
        data.get("oxigeno_sangre", 100) < 90
    )


consumer.subscribe([TOPIC_ORIGEN])
print("Escuchando datos de signos vitales...")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue

        if msg.error():
            print("Error:", msg.error())
        else:
            data = json.loads(msg.value().decode('utf-8'))
            riesgo = "ALTO" if es_riesgo_alto(data) else "NORMAL"
            data["riesgo"] = riesgo

            
            producer.produce(
                TOPIC_DESTINO,
                value=json.dumps(data),
                callback=lambda err, msg: print(f"Procesado y reenviado: {data['id']} - Riesgo: {riesgo}")
            )
            producer.flush()
except KeyboardInterrupt:
    print("Cancelado por el usuario.")
finally:
    consumer.close()
