from confluent_kafka import Consumer, KafkaError

config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}

consumer = Consumer(config)


topic = 'transferencias'  
consumer.subscribe([topic])

# Loop infinito de consumo de mensajes del topic
try:
    while True:
        msg = consumer.poll(1.0)  

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            print('Nuevo mensaje: {}'.format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor al parar la Applicacion Python
    consumer.close()