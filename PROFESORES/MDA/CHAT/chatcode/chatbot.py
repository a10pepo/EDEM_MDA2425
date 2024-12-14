import streamlit as st
from streamlit_chat import message
from datetime import datetime

def on_input_change():
    user_input = st.session_state.user_input
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.chat_history.append({'author': 'user', 'data': user_input, 'timestamp': timestamp})

def on_btn_click():
    del st.session_state.chat_history[:]

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
        is_user = author == 'user'
        message(f"{timestamp}: \n {data}", is_user=is_user, key=f"{i}_{author}")

    st.button("Clear message", on_click=on_btn_click)

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")