from confluent_kafka import Consumer, KafkaError

# Configuración del consumidor
def create_consumer():
    config = {
        'bootstrap.servers': 'localhost:9092', 
        'group.id': 'python-consumer-group', 
        'auto.offset.reset': 'earliest'   
    }
    return Consumer(config)

# Crear un consumidor
consumer = create_consumer()

# Suscribirse a un tópico
topic = 'censura'  # El nombre del tópico
consumer.subscribe([topic])

# Loop infinito de consumo de mensajes del topic
try:
    while True:
        msg_consumer = consumer.poll(1.0) 
        
        if msg_consumer is None:
            continue
        if msg_consumer.error():
            if msg_consumer.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print("Error al recibir mensaje: {}".format(msg_consumer.error()))
        else:
            print('Nuevo mensaje: {}'.format(msg_consumer.value().decode('utf-8')))

except KeyboardInterrupt:
    pass
finally:
    consumer.close()