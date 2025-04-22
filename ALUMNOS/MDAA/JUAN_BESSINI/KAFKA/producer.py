from kafka import KafkaProducer
import pandas as pd
import json
import logging
import time
import os

class Producer:
    def __init__(self, path_csv, topic, freq):
        self.topic=topic
        if isinstance(freq, int):
            self.freq=freq
        else:
            int(freq)
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092',
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        self.df = pd.read_csv(path_csv)

    def start_write(self):
        for index, value in self.df.iterrows():
            dict_data=dict(value)
            self.producer.send(self.topic, value=dict_data)
            logging.info(f"Mensaje {index+1}: {dict_data}")
            time.sleep(self.freq)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, 'olympic_medals.csv')
    producer = Producer(csv_path, 'olympics.raw', 2)
    try:
        producer.start_write()
    except KeyboardInterrupt:
        logging.info("Proceso interrumpido")
import pandas as pd
import json
import logging
import time
import os

class Producer:
    def __init__(self, path_csv, topic, freq):
        self.topic = topic
        if isinstance(freq, int):
            self.freq = freq
        else:
            self.freq = int(freq)

        # Configurar el producer para Kafka local
        self.producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

        if not os.path.exists(path_csv):
            raise FileNotFoundError(f"No se encontró el archivo CSV en: {path_csv}")

        # Cargar CSV
        self.df = pd.read_csv(path_csv)

    def start_write(self):
        for index, value in self.df.iterrows():
            dict_data = dict(value)
            # Aseguramos tipos
            dict_data['olympic_year'] = int(dict_data['olympic_year'])
            self.producer.send(self.topic, value=dict_data)
            logging.info(f"Mensaje {index + 1}: {dict_data}")
            time.sleep(self.freq)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, 'olympic_medals.csv')
    producer = Producer(csv_path, 'olympics.raw', 2)
    try:
        producer.start_write()
    except KeyboardInterrupt:
        logging.info("Proceso interrumpido por el usuario.")
