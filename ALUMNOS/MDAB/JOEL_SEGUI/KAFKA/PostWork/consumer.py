from confluent_kafka import Consumer, KafkaError

# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092', 
    'group.id': 'python-consumer-group', 
    'auto.offset.reset': 'earliest'  
}

# Crear un consumidor
consumer = Consumer(config)

# Suscribirse a un tópico
topic = 'Alertas-IMP'  
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
    consumer.close()
