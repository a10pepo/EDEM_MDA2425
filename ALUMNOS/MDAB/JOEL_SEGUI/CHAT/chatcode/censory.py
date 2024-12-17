from confluent_kafka import Consumer, Producer, KafkaError

# Configuración del consumidor
consumer_config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',    
    'auto.offset.reset': 'earliest'         
}

# Configuración del productor
producer_config = {
    'bootstrap.servers': 'localhost:9092'  
}

# Crear el consumidor y productor
consumer = Consumer(consumer_config)
producer = Producer(producer_config)

# Tópicos
input_topic = 'chat'      
output_topic = 'censura'   


insultos = [
    "gilipollas", "cabrón", "puta", "mierda", "imbécil", "pendejo", "mamón", 
    "caraculo", "subnormal", "tarado", "payaso", "cabronazo", "perdedor", 
    "capullo", "mierdoso", "baboso", "tocahuevos", "pelotudo", "chupapollas", 
    "desgraciado", "puto", "estúpido", "zopenco", "lameculos", "malparido", 
    "joder", "patan", "bastardo", "retardado"
]

def censurar_mensaje(mensaje, insultos):
    for insulto in insultos:
        mensaje = mensaje.replace(insulto, "*****").replace(insulto.capitalize(), "*****")
    return mensaje

try:
    consumer.subscribe([input_topic])
    print(f"Escuchando mensajes del tópico '{input_topic}'...")

    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print(f"Error al recibir mensaje: {msg.error()}")
            continue

        # Procesamos el mensaje
        try:
            user_key = msg.key().decode('utf-8') if msg.key() else "Unknown" #para el autor
            mensaje_original = msg.value().decode('utf-8')
            print(f"Mensaje recibido de '{user_key}': {mensaje_original}")

            # Censuramos el mensaje
            mensaje_censurado = censurar_mensaje(mensaje_original, insultos)

            # Enviamos el mensaje censurado
            producer.produce(output_topic, key=user_key, value=mensaje_censurado)
            producer.flush() 

            print(f"Mensaje procesado y enviado a '{output_topic}': {mensaje_censurado} (USER: {user_key})")

        except Exception as e:
            print(f"Error al procesar el mensaje: {e}")

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor al parar la Applicacion Python
    consumer.close()
