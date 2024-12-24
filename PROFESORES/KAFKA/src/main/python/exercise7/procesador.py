from confluent_kafka import Consumer, Producer, KafkaError
import time
from json import dumps

## CONSUMER

consumer_config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}

consumer = Consumer(consumer_config)

topic = 'transferencias'
consumer.subscribe([topic])

## PRODUCER

producer_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

producer = Producer(producer_config)
topic_riesgo = 'transferencias_de_riesgo'

# Loop infinito de consumo de mensajes del topic
try:
    while True:
        msg = consumer.poll(1.0)
        
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            transferencia = msg.value().decode('utf-8')
            # print(transferencia)
            if 'Islas Caiman' in transferencia:
                print('Transferencia de RIESGO:{}'.format(msg.value().decode('utf-8')))
                data_str = dumps(transferencia)
                data_bytes = data_str.encode('utf-8')
                key = str('key').encode('utf-8')
                producer.produce(topic=topic_riesgo, value=data_bytes, key=key)
                print("Sending data: {} to topic {}".format(transferencia, topic_riesgo))
                producer.flush()
            
            
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
