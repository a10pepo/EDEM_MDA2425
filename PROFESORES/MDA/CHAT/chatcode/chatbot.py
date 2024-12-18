import streamlit as st
from streamlit_chat import message
from datetime import datetime
import threading
import time
import random
import queue
from confluent_kafka import Consumer, KafkaError
from confluent_kafka import Producer, KafkaError
from pyspark.sql import SparkSession



USER='Alejandro Bosch'

# Initialize chat history in session state if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [
        {'author': 'bot', 'data': 'plan text with line break', 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
        {'author': 'bot', 'data': 'Line 1 \n Line 2 \n Line 3', 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    ]

def on_input_change():
    user_input = st.session_state.user_input
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.chat_history.append({'author': USER, 'data': user_input, 'timestamp': timestamp})

def on_btn_click():
    del st.session_state.chat_history[:]

def generate_random_message():
    messages = [
        "Hello, how can I help you?",
        "What can I do for you today?",
        "Here is a random fact: The Eiffel Tower can be 15 cm taller during the summer.",
        "Did you know? Honey never spoils.",
        "Random message incoming!"
    ]    
    random_message = random.choice(messages)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.chat_history.append({'author': USER, 'data': random_message, 'timestamp': timestamp})



st.session_state.setdefault(
    'chat_history', 
    [
        {'author': 'bot', 'data': 'plan text with line break', 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
        {'author': 'bot', 'data': 'Line 1 \n Line 2 \n Line 3', 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    ]
)

st.title("Chat placeholder")

chat_placeholder = st.empty()

with chat_placeholder.container():
    sorted_history = sorted(st.session_state.chat_history, key=lambda x: x['timestamp'])
    for i, message_data in enumerate(sorted_history):
        author = message_data['author']
        data = message_data['data']
        timestamp = message_data['timestamp']
        is_user = author == USER
        message(f"{timestamp}: \n {data}", is_user=is_user, key=f"{i}_{author}", avatar_style='adventurer')

    st.button("Clear message", on_click=on_btn_click)
    

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")

 # Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer-pedro'
}

# Crear un productor
producer = Producer(config)


# Send 100 messages where the key is the index and the message to send is "test message - index"
# the topic name ismyTopic

topic_kafka = ['chat', 'censura']
key = "mensaje"
for topic in topic_kafka:
    producer.produce(topic=topic, value=data, key=key)  # Send bytes


# Optionally, you can check if there are any messages that failed to be delivered:
if producer.flush() != 0:
    print("Some messages failed to be delivered")

# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}

# Crear un consumidor
consumer = Consumer(config)

# Suscribirse a un tópico
topic = 'chat'  # El nombre del tópico
consumer.subscribe(['chat', 'censura'])

# Leer mensajes de los tópicos
try:
    while True:
        msg = consumer.poll(1.0)  # Tiempo de espera para recibir mensajes
        
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print(f"Error al recibir mensaje: {msg.error()}")
        else:
            # Identificar el tópico del mensaje
            topic = msg.topic()
            data = msg.value().decode('utf-8')
            print(f"Nuevo mensaje del tópico {topic}: {data}")

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor
    consumer.close()



