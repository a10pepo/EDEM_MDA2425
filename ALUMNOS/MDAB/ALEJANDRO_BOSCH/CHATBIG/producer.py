from confluent_kafka import Producer
import json
import time

def send_kafka_message(message, author):
    """
    Envía mensajes a ambos topics de Kafka
    """
    # Configuración del productor
    config = {
        'bootstrap.servers': 'kafka:29092',
        'client.id': 'python-producer-chat'
    }
    
    # Crear un productor
    producer = Producer(config)
    
    # Preparar el mensaje
    data = {
        "author": author,
        "message": message,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Convertir el mensaje a JSON y luego a bytes
    data_bytes = json.dumps(data).encode('utf-8')
    
    # Lista de topics
    topics = ['chat', 'chat_controlled']
    
    # Enviar el mensaje a ambos topics
    for topic in topics:
        producer.produce(topic=topic, value=data_bytes, key=author.encode('utf-8'))
    
    # Verificar si hay mensajes que fallaron en enviarse
    if producer.flush() != 0:
        print("Algunos mensajes no pudieron ser entregados")

if __name__ == "__main__":
    # Ejemplo de envío de mensaje
    while True:
        try:
            mensaje = input("Escribe tu mensaje (o 'salir' para terminar): ")
            if mensaje.lower() == 'salir':
                break
            autor = input("Tu nombre: ")
            send_kafka_message(mensaje, autor)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")
    
    print("Productor finalizado")