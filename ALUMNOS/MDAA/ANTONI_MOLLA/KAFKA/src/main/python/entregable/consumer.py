#SIMPLE

from confluent_kafka import Consumer, KafkaError
import json

# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}

# Crear un consumidor
consumer = Consumer(config)

# Suscribirse a un tópico
topic = 'barcelona'  # El nombre del tópico
consumer.subscribe([topic])

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
            # Procesar el mensaje recibido. Aqui solo lo mostramos por pantall. En una App real se pueden hacer cualquier
            # cosa con un mensaje. Ejmplos: Filtrarlo, modificarlo, guardarlo en una base de datos, 
            #enviarlo a otra applicación, etc.
            print('Nuevo jugador: {}'.format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor al parar la Applicacion Python
    consumer.close()




# #Transferencas completadas o pendientes

# from confluent_kafka import Consumer, KafkaError
# import json

# # Configuración del consumidor
# config = {
#     'bootstrap.servers': 'localhost:9092',  
#     'group.id': 'python-consumer-group',
#     'auto.offset.reset': 'earliest'  
# }

# # Crear un consumidor
# consumer = Consumer(config)

# # Suscribirse a un tópico
# topic = 'transferencias2'  # El nombre del tópico
# consumer.subscribe([topic])

# # Loop infinito de consumo de mensajes del topic
# try:
#     while True:
#         msg = consumer.poll(1.0)  # Lee nuevos mensajes cada 1 segundo

#         if msg is None:
#             continue
#         if msg.error():
#             if msg.error().code() == KafkaError._PARTITION_EOF:
#                 print("No hay más mensajes en esta partición.")
#             else:
#                 print("Error al recibir mensaje: {}".format(msg.error()))
#         else:
#             # Decodificar el mensaje y parsearlo como JSON
#             try:
#                 data = json.loads(msg.value().decode('utf-8'))

#                 # Filtrar las transferencias con estado "Completada"
#                 estado = data.get('estado', '').lower()  # Convertir a minúsculas para evitar problemas con mayúsculas/minúsculas
#                 if estado == "pendiente":
#                     print('Transferencia pendiente: {}'.format(json.dumps(data, ensure_ascii=False)))

#             except json.JSONDecodeError:
#                 print("Error al decodificar el mensaje como JSON: {}".format(msg.value().decode('utf-8')))

# except KeyboardInterrupt:
#     pass
# finally:
#     # Cerrar el consumidor al parar la Aplicación Python
#     consumer.close()
