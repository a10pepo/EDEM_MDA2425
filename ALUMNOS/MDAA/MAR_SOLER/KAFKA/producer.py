import time
from json import dumps
from confluent_kafka import Producer
import re

config = {
    'bootstrap.servers': 'localhost:9092',  
    'client.id': 'python-producer'
}

producer = Producer(config)

topic_kafka = "recetas"

file1 = open("recetas.txt",encoding="utf8")
Lines = file1.readlines()
 
count = 0

for line in Lines:
    time.sleep(2)
    print( line.strip() + "\n")
    words = re.findall(r"[\w']+|[.,!?;]", line)
    for word in words:
        data_bytes = word  
        key = str(count)
        producer.produce(topic=topic_kafka, value=data_bytes, key=key)
        producer.flush()
      
if producer.flush() != 0:
    print("Error en el envío de algunos mensajes.")