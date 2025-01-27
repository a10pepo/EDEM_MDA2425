import os
import streamlit as st
from streamlit_chat import message
from datetime import datetime
from kafka import KafkaConsumer, KafkaProducer
import threading
import json
import queue

# Configuración basada en variables de entorno (ideal para Docker)
USER = os.getenv('USER', 'nickname')
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'chat')
KAFKA_SERVER = os.getenv('KAFKA_SERVER', 'kafka:29092')  # Kafka en Docker

# Cola para recibir mensajes desde Kafka
message_queue = queue.Queue()

# Configuración inicial del historial de chat
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Configuración del Producer de Kafka
try:
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialización JSON
    )
except Exception as e:
    st.error(f"Error connecting to Kafka producer: {e}")

# Función para procesar la entrada del usuario y enviar mensaje a Kafka
def on_input_change():
    user_input = st.session_state.get("user_input", "").strip()
    if not user_input:
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Agregar el mensaje al historial de chat
    st.session_state.chat_history.append({'author': USER, 'data': user_input, 'timestamp': timestamp})
    # Crear mensaje para Kafka
    kafka_message = {"mensaje": user_input, "autor": USER, "timestamp": timestamp}
    # Enviar mensaje a Kafka
    try:
        producer.send(KAFKA_TOPIC, kafka_message)
    except Exception as e:
        st.error(f"Error sending message to Kafka: {e}")
    # Limpiar entrada
    st.session_state.user_input = ""

# Función para limpiar el historial de chat
def on_btn_click():
    st.session_state.chat_history = []

# Función para consumir mensajes desde Kafka
def consume_messages():
    try:
        consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=KAFKA_SERVER,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='streamlit-chat-group',
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )
        for message in consumer:
            data = message.value
            message_queue.put({
                'author': data['autor'], 
                'data': data['mensaje'], 
                'timestamp': data['timestamp']
            })
    except Exception as e:
        st.error(f"Error connecting to Kafka consumer: {e}")

# Iniciar el consumidor en un hilo separado para evitar bloquear la interfaz de Streamlit
consumer_thread = threading.Thread(target=consume_messages, daemon=True)
consumer_thread.start()

# Título de la aplicación
st.title("Chat Kafka Interface")

# Placeholder para el chat
chat_placeholder = st.empty()

# Mostrar historial de chat y recibir nuevos mensajes desde Kafka
with chat_placeholder.container():
    # Agregar mensajes desde Kafka a la sesión de Streamlit
    while not message_queue.empty():
        msg = message_queue.get()
        # Evitar agregar mensajes duplicados al historial
        if msg not in st.session_state.chat_history:
            st.session_state.chat_history.append(msg)

    # Ordenar y mostrar mensajes
    sorted_history = sorted(
        st.session_state.chat_history, 
        key=lambda x: datetime.strptime(x['timestamp'], "%Y-%m-%d %H:%M:%S")
    )
    for i, message_data in enumerate(sorted_history):
        author = message_data['author']
        data = message_data['data']
        timestamp = message_data['timestamp']
        
        # Mostrar el mensaje
        is_user = author == USER
        message(f"{timestamp}: \n {data}", is_user=is_user, key=f"{i}_{author}")

    # Botón para limpiar mensajes
    st.button("Clear messages", on_click=on_btn_click)

# Contenedor para entrada del usuario
with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")