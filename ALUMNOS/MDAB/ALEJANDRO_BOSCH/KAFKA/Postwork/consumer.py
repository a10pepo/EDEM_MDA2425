from confluent_kafka import Consumer, KafkaError

config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'imdb-consumer-group',
    'auto.offset.reset': 'earliest'
}


consumer = Consumer(config)

topic = 'imdb'  
consumer.subscribe([topic])

# Loop infinito de consumo de mensajes del topic
try:
    while True:
        msg = consumer.poll(1.0)  # Lee nuevos mensajes cada 1 segundo

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            # Procesar el mensaje recibido. Aquí solo lo mostramos por pantalla.
            print('Nuevo mensaje: {}'.format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor al parar la aplicación Python
    consumer.close()
