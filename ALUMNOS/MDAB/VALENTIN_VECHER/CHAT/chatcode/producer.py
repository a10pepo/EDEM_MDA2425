from kafka import KafkaProducer
import time
import json

# Configuración del producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Cambiar si usas otro host o puerto
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialización de mensajes en JSON
)

# Tópico al que enviar los mensajes
topic_name = 'chat'

# Enviar mensajes automáticamente cada 5 segundos
try:
    while True:
        message = {"mensaje": "hola", 
                   "autor": "Valentino",
                   "timestamp": time.time()}  # Mensaje de ejemplo
        producer.send(topic_name, message)
        print(f"Mensaje enviado: {message}")
        time.sleep(20)  # Intervalo de 5 segundos
except KeyboardInterrupt:
    print("Producer detenido.")
finally:
    producer.close()
