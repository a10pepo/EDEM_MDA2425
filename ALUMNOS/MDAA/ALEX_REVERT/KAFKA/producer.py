import time
from confluent_kafka import Producer

BROKER = 'localhost:9092'
TOPIC = 'transferencias-internacionales'

def entrega_exitosa(err, msg):
    if err is not None:
        print(f"❌ Error al enviar mensaje: {err}")
    else:
        print(f"✅ Mensaje entregado en {msg.topic()} [Partición {msg.partition()}] Offset {msg.offset()}")

def main():
    producer = Producer({'bootstrap.servers': BROKER})

    try:
        with open('movimientos.txt', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print("❌ ERROR: No se encontró el archivo movimientos.txt")
        return

    print(f"🟣 Enviando {len(lineas)} transferencias al tópico '{TOPIC}'...")

    for idx, linea in enumerate(lineas):
        mensaje = linea.strip()
        if not mensaje:
            continue
        producer.produce(
            topic=TOPIC,
            key=str(idx),
            value=mensaje.encode('utf-8'),
            callback=entrega_exitosa
        )
        print(f"📤 Enviado: {mensaje}")
        producer.poll(0)
        time.sleep(0.5)

    producer.flush()
    print("🚀 Todas las transferencias fueron enviadas.")

if __name__ == '__main__':
    main()
