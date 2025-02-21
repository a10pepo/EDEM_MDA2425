from confluent_kafka import Consumer, KafkaError


config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}


consumer = Consumer(config)


topic = 'cultivos'
consumer.subscribe([topic])


try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print(f"Error al recibir mensaje: {msg.error()}")
        else:

            json_message = msg.value().decode('utf-8')
            print(f"Mensaje recibido: {json_message}")

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
    print("Consumidor cerrado.")
