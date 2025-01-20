import time
from json import dumps, loads  # Para manejar JSON
from confluent_kafka import Producer
import re

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)

# Definir el topic de Kafka
topic_transferencias = 'transferencias'
topic_paraisos_fiscales = 'paraisos_fiscales'

# Ruta del archivo con los datos JSON
ruta = "transferencias.txt"

# Abrir y leer el archivo línea por línea (suponiendo que hay múltiples JSON en líneas separadas)
with open(ruta, encoding="utf8") as file:
    Lines = file.readlines()

count = 0

# Iterar sobre las líneas del archivo
for line in Lines:
    time.sleep(2)  # Simular retardo entre mensajes
    print(f"Procesando línea: {line.strip()}\n")

    try:
        # Convertir la línea JSON en un diccionario
        data = loads(line.strip())

        # Convertir el diccionario a JSON string para Kafka
        data_bytes = dumps(data)

        pais_origen = data.get("pais_origen", "")
        pais_destino = data.get("pais_destino", "")


        if pais_origen in ["Singapur", "Islas Caimán"] or pais_destino in ["Singapur", "Islas Caimán"]:
            topic = topic_paraisos_fiscales
        else:
            topic = topic_transferencias

        # Usar el ID como clave para Kafka
        key = data["id_transferencia"]

        # Enviar el mensaje a Kafka
        producer.produce(topic=topic, value=data_bytes, key=key)
        count += 1  # Incrementar el contador

    except Exception as e:
        print(f"Error procesando la línea: {e}")

# Asegurarse de que todos los mensajes se envíen
producer.flush()

# Mensaje de confirmación
print(f"Se enviaron {count} mensajes a Kafka.")
