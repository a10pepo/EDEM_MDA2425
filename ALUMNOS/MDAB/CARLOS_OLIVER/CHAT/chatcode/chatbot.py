import streamlit as st
from streamlit_chat import message
from datetime import datetime
import threading
import time
import random
import queue

USER='nickname'

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

