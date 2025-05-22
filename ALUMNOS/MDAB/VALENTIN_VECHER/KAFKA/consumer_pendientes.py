from confluent_kafka import Consumer, KafkaError
import json

consumer_config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'grupo_consumidor',
    'auto.offset.reset': 'earliest',    
}

# Crear el consumidor
consumer = Consumer(consumer_config)

# Tema que se va a consumir
topic = 'transferencias_bancarias'

# Suscribirse al tema
consumer.subscribe([topic])

# Diccionario para almacenar los montos totales por país de origen
suma_por_pais = {}

print(f"Consumiendo mensajes del tema: {topic}")

try:
    while True:
        # Leer el siguiente mensaje
        msg = consumer.poll(1.0)  # Esperar hasta 1 segundo por un mensaje

        if msg is None:
            continue  # No hay mensajes, seguir esperando
        if msg.error():
            # Verificar si hubo un error
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # Fin de la partición
                print(f"Fin de la partición {msg.partition()} en {msg.topic()}")
            else:
                # Otro error
                print(f"Error: {msg.error()}")
        else:
            # Procesar el mensaje
            mensaje = msg.value().decode('utf-8')
            try:
                # Convertir el mensaje a JSON
                transferencia = json.loads(mensaje)

                estado=transferencia.get("estado")

                if estado=="Pendiente":
                    print(f"Transferencia pendiente: {transferencia}") 

            except json.JSONDecodeError:
                print(f"Error al decodificar el mensaje: {mensaje}")
            except Exception as e:
                print(f"Error procesando el mensaje: {e}")

except KeyboardInterrupt:
    print("Consumo interrumpido por el usuario.")
finally:
    # Cerrar el consumidor
    consumer.close()
