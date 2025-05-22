import time
from json import dumps, loads  # Para manejar JSON
from confluent_kafka import Producer

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092', 
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)

topic = 'transferencias'

route = "transferencias.txt"


with open(route, encoding="utf8") as file:
    Lines = file.readlines()

count = 0

# Iterar sobre las líneas del archivo
for line in Lines:
    time.sleep(2)  
    print(f"Procesando línea: {line.strip()}\n")

    try:

        data = loads(line.strip())

        data_bytes = dumps(data)

        key = data["id_transferencia"]

        producer.produce(topic=topic, value=data_bytes, key=key)
        count += 1  

    except Exception as e:
        print(f"Error procesando la línea: {e}")

producer.flush()

print(f"Se enviaron {count} mensajes a Kafka.")