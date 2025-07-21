import json
from confluent_kafka import Consumer, KafkaError

BROKER = 'localhost:9092'
TOPIC = 'transferencias-internacionales'
GROUP_ID = 'grupo-transferencias-consumer'

consumer = Consumer({
    'bootstrap.servers': BROKER,
    'group.id': GROUP_ID,
    'auto.offset.reset': 'earliest'
})

consumer.subscribe([TOPIC])

print(f"🟢 Consumidor escuchando el tópico '{TOPIC}'...")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f"❌ Error en el mensaje: {msg.error()}")
        else:
            texto_json = msg.value().decode('utf-8')
            try:
                datos = json.loads(texto_json)
                print("\n✅ Transferencia recibida:")
                print(f"  ID: {datos.get('id_transferencia')}")
                print(f"  Fecha: {datos.get('fecha')}")
                print(f"  Origen: {datos.get('pais_origen')} ({datos.get('cuenta_origen')})")
                print(f"  Destino: {datos.get('pais_destino')} ({datos.get('cuenta_destino')})")
                print(f"  Monto: {datos.get('monto')} {datos.get('moneda')}")
                print(f"  Concepto: {datos.get('concepto')}")
                print(f"  Estado: {datos.get('estado')}")
                print("-" * 50)
            except json.JSONDecodeError:
                print(f"⚠️ No se pudo decodificar JSON: {texto_json}")

except KeyboardInterrupt:
    print("\n⏹️ Consumidor detenido.")
finally:
    consumer.close()
