import time
import requests
from json import dumps
from confluent_kafka import Producer, KafkaError

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  # Dirección del servidor Kafka
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)

# Nombre del tópico
topic_kafka = 'cultivos'

# URL de la API
api_url = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/superficie-cultivada-cultivos/exports/json?lang=es&timezone=Europe%2FBerlin"

# Obtener datos de la API
try:
    response = requests.get(api_url)
    response.raise_for_status()  # Lanza un error si la respuesta no es exitosa (código 4xx o 5xx)

    data_list = response.json()  # Los datos se obtienen como una lista de JSONs
    print(f"Datos obtenidos de la API: {len(data_list)} registros")

    # Enviar cada JSON como un mensaje
    for index, data in enumerate(data_list):
        try:
            json_message = dumps(data)  # Convierte el diccionario en JSON
            key = str(index)  # Clave del mensaje
            producer.produce(topic=topic_kafka, value=json_message, key=key)  # Envía el mensaje
            print(f"Mensaje enviado: {json_message}")
            time.sleep(1)  # Pausa para evitar inundar el topic
        except Exception as e:
            print(f"Error al enviar el mensaje con índice {index}: {str(e)}")

    # Asegúrate de que todos los mensajes se envíen antes de salir
    producer.flush()

    print("Todos los mensajes han sido enviados.")

except requests.exceptions.RequestException as e:
    print(f"Error al obtener datos de la API: {str(e)}")
except Exception as e:
    print(f"Error inesperado: {str(e)}")
