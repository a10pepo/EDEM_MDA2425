from confluent_kafka import Consumer, KafkaError

# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092', #server q ens apuntem
    'group.id': 'python-consumer-group', #nombre de la etiqueta para enlazarlo a las diff maquinas y dividir el peso del trabajo
    'auto.offset.reset': 'earliest'   #Para poder reprocesar todos los datos desde el principio
}

# Crear un consumidor
consumer = Consumer(config)

# Suscribirse a un tópico
topic = 'chat'  # El nombre del tópico
consumer.subscribe([topic])

# Loop infinito de consumo de mensajes del topic
try:
    while True:
        msg = consumer.poll(1.0)  # Lee nuevos mensajes cada 1 segundo
        
        if msg is None: #si no hay mensage, siguiente (vuelve a empezar el while)
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            # Procesar el mensaje recibido. Aqui solo lo mostramos por pantall. En una App real se pueden hacer cualquier
            # cosa con un mensaje. Ejmplos: Filtrarlo, modificarlo, guardarlo en una base de datos, 
            #enviarlo a otra applicación, etc.
            print('Nuevo mensaje: {}'.format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor al parar la Applicacion Python
    consumer.close()