from kafka import KafkaProducer
import pandas as pd
import json
import logging
import time

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
    producer = Producer('data/filmaffinity.csv', 'films', 5)
    try:
        producer.start_write()
    except KeyboardInterrupt:
        logging.info("Proceso interrumpido")
