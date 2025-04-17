from json import loads
from collections import defaultdict
from confluent_kafka import Consumer, KafkaError

# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}

# Crear un consumidor
consumer = Consumer(config)

# Suscribirse a un tópico
topic = "transferencias"  # El nombre del tópico
consumer.subscribe([topic])

# Diccionario para agrupar montos por país
suma_por_pais = defaultdict(float)

# Loop infinito de consumo de mensajes del topic
try:
    while True:
        msg = consumer.poll(1.0)  # Lee nuevos mensajes cada 1 segundo
        
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            try:
                # Procesar el mensaje recibido
                data = loads(msg.value().decode('utf-8'))  # Decodificar el mensaje JSON
                pais_origen = data.get("pais_origen", "")
                monto = data.get("monto", 0.0)

                # Acumular el monto por país de origen
                suma_por_pais[pais_origen] += monto
                
                # Mostrar resultados parciales
                print(f"Suma total por país (parcial): {dict(suma_por_pais)}")

            except Exception as e:
                print(f"Error procesando el mensaje: {e}")

except KeyboardInterrupt:
    pass
finally:
    # Mostrar resultados finales
    print(f"Suma total por país (final): {dict(suma_por_pais)}")
    # Cerrar el consumidor al parar la Aplicación Python
    consumer.close()
