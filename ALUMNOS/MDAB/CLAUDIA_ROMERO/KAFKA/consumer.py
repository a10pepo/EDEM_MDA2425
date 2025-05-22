from confluent_kafka import Consumer, Producer, KafkaError
import json


consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'pokemon-consumer-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_config)

topic = 'pokemon'
consumer.subscribe([topic])

producer_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'pokemon-processor'
}
producer = Producer(producer_config)
topic_processed = 'legendary_alerts'

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print("⚠️ Error al recibir mensaje:", msg.error())
            continue

        pokemon_data = json.loads(msg.value().decode('utf-8'))

        if pokemon_data['legendary']:
            print(f"⚡ ¡Pokémon legendario detectado!: {pokemon_data['pokemon']} ⚡")
            
            producer.produce(topic=topic_processed, value=json.dumps(pokemon_data).encode('utf-8'))
            producer.flush() 

except KeyboardInterrupt:
    pass
finally:
    consumer.close()



