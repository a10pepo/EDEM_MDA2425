import time
from json import dumps
from confluent_kafka import Producer
import re

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)

topic_kafka = 'transferencias'

file1 = open('exercise7/transferencias.txt',encoding="utf8")
Lines = file1.readlines()

count = 0
for line in Lines:
    time.sleep(2)
    print( line.strip() + "\n")
    words = re.findall(r"[\w']+|[.,!?;]", line)
    for word in words:
        transfer_data = {
        "id_transferencia": words[0],   
        "fecha": words[1],               
        "cuenta_origen": words[2],       
        "pais_origen": words[3],         
        "cuenta_destino": words[4],      
        "pais_destino": words[5],        
        "monto": words[6],        
        "moneda": words[7],              
        "concepto": words[8],            
        "estado": words[9]               
        }
        message_json = dumps(transfer_data)

        key = str(count)
        producer.produce(topic=topic_kafka, value=message_json.encode('utf-8'), key=key)  # Send bytes
        # After your loop where you send messages:
        producer.flush()


# Optionally, you can check if there are any messages that failed to be delivered:
if producer.flush() != 0:
    print("Some messages failed to be delivered")