from confluent_kafka import Producer
import json
import time

def delivery_report(err, msg):
    """ Callback que confirma la entrega del mensaje """
    if err is not None:
        print(f"Error al enviar mensaje: {err}")
    else:
        print(f"Mensaje enviado a {msg.topic()} [{msg.partition()}]")

producer_config = {
    'bootstrap.servers': 'localhost:9092',  
}

producer = Producer(producer_config)

# Leer las transferencias bancarias desde el archivo JSON
input_file = 'transferencias.json' 
topic = 'transferencias_bancarias'

try:
    with open(input_file, 'r') as file:
        transferencias = json.load(file)

    for transferencia in transferencias:
        message = json.dumps(transferencia)
        producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
        print(f"Mensaje enviado: {message}")
        producer.flush() 
        time.sleep(5)  
except FileNotFoundError:
    print(f"Archivo {input_file} no encontrado.")
except Exception as e:
    print(f"Error: {e}")

producer.flush()  
