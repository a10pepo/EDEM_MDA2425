import streamlit as st
from streamlit_chat import message
from datetime import datetime
import threading
import json
from confluent_kafka import Producer, Consumer, KafkaError

USER = 'joaquin'

# Kafka Configuration
KAFKA_BROKER = '172.28.182.142:8502'  # Ensure this matches your Kafka setup
TOPIC = 'chat'

# Initialize Kafka Producer
producer = Producer({'bootstrap.servers': KAFKA_BROKER})

# Initialize Kafka Consumer
consumer = Consumer({
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': 'streamlit-consumer-group',
    'auto.offset.reset': 'earliest'
})
consumer.subscribe([TOPIC])

# Initialize chat history in session state if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [
        {'author': 'bot', 'data': 'Welcome to the chat!', 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    ]

# Function to send message to Kafka
def send_message_to_kafka(user_message):
    if not user_message.strip():  # Don't send empty messages
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message_data = {'author': USER, 'data': user_message, 'timestamp': timestamp}
    producer.produce(TOPIC, value=json.dumps(message_data))  # Serialize as JSON
    producer.flush()


# Function to consume messages from Kafka
def consume_messages():
    while True:
        try:
            msg = consumer.poll(0.1)  # Poll messages with a 100ms timeout
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Error: {msg.error()}")
                    break
            # Process received message
            message_data = json.loads(msg.value().decode('utf-8'))  # Deserialize JSON message
            if message_data not in st.session_state.chat_history:
                st.session_state.chat_history.append(message_data)
                st.experimental_rerun()  # Force a refresh
        except Exception as e:
            print(f"Error consuming messages: {e}")

# Start consumer thread only if it hasn't been started already
if 'consumer_thread_started' not in st.session_state:
    st.session_state['consumer_thread_started'] = True
    threading.Thread(target=consume_messages, daemon=True).start()

# Streamlit UI
def on_input_change():
    user_input = st.session_state.user_input
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_message = {'author': USER, 'data': user_input, 'timestamp': timestamp}
    st.session_state.chat_history.append(user_message)  # Add to chat history
    send_message_to_kafka(user_input)
    st.session_state.user_input = ''  # Clear the input after sending

def on_btn_click():
    del st.session_state['chat_history'][:]  # Clear chat history
    st.experimental_rerun()  # Force a refresh after clearing

st.title("Chat")

chat_placeholder = st.empty()

with chat_placeholder.container():
    sorted_history = sorted(st.session_state['chat_history'], key=lambda x: x['timestamp'])
    for i, message_data in enumerate(sorted_history):
        author = message_data['author']
        data = message_data['data']
        timestamp = message_data['timestamp']
        is_user = author == USER
        message(f"{timestamp}: \n {data}", is_user=is_user, key=f"{i}_{author}")

    st.button("Clear messages", on_click=on_btn_click)

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")
