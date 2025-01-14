from confluent_kafka import Consumer, KafkaError

# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  # Comienza desde el inicio si no hay offset guardado
}

# Crear un consumidor
consumer = Consumer(config)

# Suscribirse al tópico
topic = 'cultivos'
consumer.subscribe([topic])

# Consumir mensajes
try:
    while True:
        msg = consumer.poll(1.0)  # Esperar 1 segundo por mensajes

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print(f"Error al recibir mensaje: {msg.error()}")
        else:
            # Procesar el mensaje recibido
            json_message = msg.value().decode('utf-8')
            print(f"Mensaje recibido: {json_message}")

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
    print("Consumidor cerrado.")
