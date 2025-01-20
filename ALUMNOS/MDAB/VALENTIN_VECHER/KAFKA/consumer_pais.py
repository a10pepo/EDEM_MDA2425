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

# Países considerados de alto riesgo
paises_filtro = ['Islas Caimán', 'Singapur']

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
            mensaje = msg.value().decode('utf-8')  # Decodificar mensaje
            try:
                # Convertir el mensaje a un diccionario JSON
                transferencia = json.loads(mensaje)

                # Verificar si el país de origen o destino está en la lista de riesgo
                pais_origen = transferencia.get("pais_origen", "")
                pais_destino = transferencia.get("pais_destino", "")

                if pais_origen in paises_filtro or pais_destino in paises_filtro:
                    print(f"Transferencia sospechosa detectada: {transferencia}")
                else:
                    id_transferencia=transferencia.get("id_transferencia")
                    print(f"Transferencia con id: {id_transferencia} sin ningun peligro.")

            except json.JSONDecodeError:
                print(f"Error al decodificar el mensaje: {mensaje}")

except KeyboardInterrupt:
    print("Consumo interrumpido por el usuario.")
finally:
    # Cerrar el consumidor
    consumer.close()
