import pandas as pd
from confluent_kafka import Producer
import json
import time

kafka_producer_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

producer = Producer(kafka_producer_config)

topic_kafka = 'imdb'

def cargar_dataset(ruta):
    df = pd.read_csv(ruta)
    df = df[['Series_Title', 'IMDB_Rating', 'Genre', 'Director', 'Star1', 'Star2', 'Star3', 'Star4']]
    return df

def enviar_datos_a_kafka(df):
    count = 0
    for _, row in df.iterrows():
        mensaje = {
            "titulo": row['Series_Title'],
            "rating": row['IMDB_Rating'],
            "genero": row['Genre'],
            "director": row['Director'],
            "actores": [row['Star1'], row['Star2'], row['Star3'], row['Star4']]
        }
        key = str(count)
        producer.produce(topic=topic_kafka, value=json.dumps(mensaje), key=key)
        print(f"Mensaje enviado: {mensaje}")
        count += 1
        time.sleep(0.1)
    
    # Asegurarse de que todos los mensajes se envíen antes de salir
    producer.flush()

    # Verificar si hay mensajes que no se enviaron correctamente
    if producer.flush() != 0:
        print("Algunos mensajes no se pudieron entregar")

# Flujo principal para el Productor
def flujo_productor(ruta_dataset):
    print("Cargando dataset...")
    df = cargar_dataset(ruta_dataset)
    print("Enviando datos a Kafka...")
    enviar_datos_a_kafka(df)

if __name__ == "__main__":
    ruta_dataset = "imdb_top_1000.csv"  # Ruta del archivo proporcionado
    flujo_productor(ruta_dataset)
