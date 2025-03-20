import time
import requests
from json import dumps
from confluent_kafka import Producer, KafkaError


config = {
    'bootstrap.servers': 'localhost:9092', 
    'client.id': 'python-producer'
}


producer = Producer(config)


topic_kafka = 'cultivos'


api_url = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/superficie-cultivada-cultivos/exports/json?lang=es&timezone=Europe%2FBerlin"


try:
    response = requests.get(api_url)
    response.raise_for_status()  

    data_list = response.json()  
    print(f"Datos obtenidos de la API: {len(data_list)} registros")


    for index, data in enumerate(data_list):
        try:
            json_message = dumps(data)  
            key = str(index) 
            producer.produce(topic=topic_kafka, value=json_message, key=key)  
            print(f"Mensaje enviado: {json_message}")
            time.sleep(1)  
        except Exception as e:
            print(f"Error al enviar el mensaje con índice {index}: {str(e)}")


    producer.flush()

    print("Todos los mensajes han sido enviados.")

except requests.exceptions.RequestException as e:
    print(f"Error al obtener datos de la API: {str(e)}")
except Exception as e:
    print(f"Error inesperado: {str(e)}")
