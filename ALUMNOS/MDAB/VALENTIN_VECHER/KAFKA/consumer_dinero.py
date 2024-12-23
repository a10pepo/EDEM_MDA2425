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

                # Obtener el país de origen y el monto de la transferencia
                pais_origen = transferencia.get("pais_origen", "Desconocido")
                monto = transferencia.get("monto", 0)

                # Validar que el monto sea numérico
                if isinstance(monto, (int, float)):
                    # Sumar el monto al país correspondiente
                    suma_por_pais[pais_origen] = suma_por_pais.get(pais_origen, 0) + monto

                # Mostrar la suma total acumulada por país
                print(f"Totales acumulados por país: {suma_por_pais}")
            except json.JSONDecodeError:
                print(f"Error al decodificar el mensaje: {mensaje}")
            except Exception as e:
                print(f"Error procesando el mensaje: {e}")

except KeyboardInterrupt:
    print("Consumo interrumpido por el usuario.")
finally:
    # Cerrar el consumidor
    consumer.close()
