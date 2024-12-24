from confluent_kafka import Consumer, KafkaError, Producer

#ESTE ES CONSUMIDOR Y PRODUCTOR A LA VEZ

# Configuración del consumidor
config_consum = {
    'bootstrap.servers': 'localhost:9092', 
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'   
}

consumer = Consumer(config_consum)

topic_consumer = 'Estados_Presion'  
consumer.subscribe([topic_consumer])

# Configuración del productor 
config_prod = {
    'bootstrap.servers': 'localhost:9092',  
    'client.id': 'python-producer'
}

topic_productor = 'Alertas-IMP'
producer = Producer(config_prod)

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
            message_value = msg.value().decode('utf-8')
            key = msg.key().decode('utf-8')

            if "Error" in message_value or "Advertencia" in message_value:
                    
                    producer.produce(topic=topic_productor, value=message_value, key=key) 
                    print(f"¡Problema detectado!{message_value} en {key}")
            else:
                continue

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor al parar la Applicacion Python
    consumer.close()
