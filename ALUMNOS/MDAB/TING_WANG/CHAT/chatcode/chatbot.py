import streamlit as st
from streamlit_chat import message
from datetime import datetime
import time
import random
import queue
from json import dumps
import json
from confluent_kafka import Producer, KafkaError


config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}
producer = Producer(config)

topic_kafka = 'chat'


USER = 'Elena'

# Inicializar historial de chat en el estado de sesión
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {'author': 'bot', 'data': 'Bienvenid@ al chat', 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
    ]

# Función para manejar la entrada del usuario
def on_input_change():
    user_input = st.session_state.user_input
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.chat_history.append({'author': USER, 'data': user_input, 'timestamp': timestamp})
    message_data = {
        "USER": USER,
        "message": user_input,
        "timestamp": timestamp
    }
    producer.produce(topic=topic_kafka, key=USER, value=json.dumps(message_data).encode('utf-8'))
    producer.flush()

# Función para borrar el historial
def on_btn_click():
    del st.session_state.chat_history[:]

# def generate_random_message():
#     messages = [
#         "Hello, how can I help you?",
#         "What can I do for you today?",
#         "Here is a random fact: The Eiffel Tower can be 15 cm taller during the summer.",
#         "Did you know? Honey never spoils.",
#         "Random message incoming!"
#     ]    
#     random_message = random.choice(messages)
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     st.session_state.chat_history.append({'author': USER, 'data': random_message, 'timestamp': timestamp})

# Título de la aplicación
st.title("Chat placeholder")

chat_placeholder = st.empty()

# Mostrar los mensajes del chat
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
