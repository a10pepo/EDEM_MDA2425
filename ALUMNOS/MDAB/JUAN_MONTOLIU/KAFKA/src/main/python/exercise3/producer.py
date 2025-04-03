from json import dumps
from confluent_kafka import Producer
import time


def read_ccloud_config(config_file):
    conf = {}
    with open(config_file) as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split('=', 1)
                conf[parameter] = value.strip()
    return conf


# Configurar el productor de Kafka
producer = Producer(read_ccloud_config("client.properties"))

# Nombre del tema en Kafka
topic_kafka = 'newtopic'

# Enviar 100 mensajes con el JSON definido
for e in range(100):
    # JSON a enviar
    data = {"name": "John", "age": 26}
    
    # Serializar el JSON a string y codificar en bytes
    data_str = dumps(data)
    data_bytes = data_str.encode('utf-8')
    
    # Clave del mensaje
    key = str(e).encode('utf-8')
    
    # Enviar mensaje a Kafka
    producer.produce(topic=topic_kafka, value=data_bytes, key=key)
    print(f"Enviando JSON: {data} con clave: {key.decode('utf-8')} al tema {topic_kafka}")
    
    # Esperar 3 segundos antes de enviar el siguiente mensaje
    time.sleep(3)

# Asegurarse de que todos los mensajes sean enviados antes de salir
producer.flush()

# Comprobar si hubo fallos en la entrega
if producer.flush() != 0:
    print("Algunos mensajes no se entregaron correctamente.")
