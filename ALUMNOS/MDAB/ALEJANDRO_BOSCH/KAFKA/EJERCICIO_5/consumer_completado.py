from confluent_kafka import Consumer, KafkaError
from json import loads



# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}

# Crear un consumidor
consumer = Consumer(config)

# Suscribirse a un tópico
topic = 'transferencias'  # El nombre del tópico
consumer.subscribe([topic])


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
            try:
                # Procesar el mensaje recibido
                data = loads(msg.value().decode('utf-8'))  # Decodificar el mensaje JSON

                estado = data.get("estado", "")
                if estado == "Completada":
                    print(f"Transferencia completada: {data}")

            except Exception as e:
                print(f"Error procesando el mensaje: {e}")
                
except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor al parar la Applicacion Python
    consumer.close()
