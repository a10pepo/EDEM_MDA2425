from confluent_kafka import Consumer, KafkaError
import json

def consume_messages():
    """
    Consume mensajes de ambos topics
    """
    # Configuración del consumidor
    config = {
        'bootstrap.servers': 'kafka:29092',
        'group.id': 'python-consumer-group-chat',
        'auto.offset.reset': 'earliest'
    }
    
    # Crear un consumidor
    consumer = Consumer(config)
    
    # Suscribirse a ambos topics
    consumer.subscribe(['chat', 'chat_controlled'])
    
    try:
        while True:
            msg = consumer.poll(1.0)
            
            if msg is None:
                continue
                
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print("No hay más mensajes en esta partición.")
                else:
                    print(f"Error al recibir mensaje: {msg.error()}")
            else:
                # Identificar el topic y procesar el mensaje
                topic = msg.topic()
                try:
                    data = json.loads(msg.value().decode('utf-8'))
                    print(f"\nNuevo mensaje del topic {topic}:")
                    print(f"Autor: {data['author']}")
                    print(f"Mensaje: {data['message']}")
                    print(f"Timestamp: {data['timestamp']}")
                except json.JSONDecodeError:
                    print(f"Error al decodificar el mensaje del topic {topic}")
                    
    except KeyboardInterrupt:
        print("\nDeteniendo el consumidor...")
    finally:
        consumer.close()

if __name__ == "__main__":
    print("Iniciando consumidor... (Presiona Ctrl+C para detener)")
    try:
        consume_messages()
    except KeyboardInterrupt:
        print("\nConsumidor finalizado")