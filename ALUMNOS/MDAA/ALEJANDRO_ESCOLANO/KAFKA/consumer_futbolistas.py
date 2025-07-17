from confluent_kafka import Consumer, KafkaError

def configurar_consumer():
    return Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'grupo-futbolistas',
        'auto.offset.reset': 'earliest'
    })

def consumir_mensajes(consumer, topico):
    consumer.subscribe([topico])
    print(f"Escuchando mensajes en el tópico '{topico}'...")
    try:
        while True:
            mensaje = consumer.poll(1.0)
            if mensaje is None:
                continue
            if mensaje.error():
                if mensaje.error().code() == KafkaError._PARTITION_EOF:
                    print("Fin de partición alcanzado.")
                else:
                    print(f"Error: {mensaje.error()}")
            else:
                print(f"Recibido: {mensaje.value().decode('utf-8')}")
    except KeyboardInterrupt:
        print("\nConsumo interrumpido por el usuario.")
    finally:
        consumer.close()

def main():
    consumer = configurar_consumer()
    consumir_mensajes(consumer, 'futbolistas')

if __name__ == "__main__":
    main() 