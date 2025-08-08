from kafka import KafkaConsumer
import json

# Configuración del Consumer
consumer = KafkaConsumer(
    'chat',  # Nombre del tópico que estás consumiendo
    bootstrap_servers='localhost:9092',  # Servidor de Kafka
    auto_offset_reset='earliest',  # Leer mensajes desde el inicio del tópico
    enable_auto_commit=True,  # Confirma automáticamente los mensajes procesados
    group_id='chat-group',  # Grupo de consumidores
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))  # Deserializar JSON a Python dict
)

print("Esperando mensajes del tópico 'chat'...\n")

# Leer mensajes en un bucle
try:
    for message in consumer:
        # Procesar el mensaje recibido
        data = message.value
        print(f"Mensaje recibido:")
        print(f"  Autor: {data['autor']}")
        print(f"  Mensaje: {data['mensaje']}")
        print(f"  Timestamp: {data['timestamp']}\n")
except KeyboardInterrupt:
    print("Consumer detenido.")
finally:
    print("Cerrando consumer...")
    consumer.close()
