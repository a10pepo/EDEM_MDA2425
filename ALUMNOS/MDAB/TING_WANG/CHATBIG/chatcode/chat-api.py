from shiny.express import ui
import time
import threading
import random
import asyncio
import requests

API_URL = 'http://localhost:5000/send_message'
FILTERED_API_URL = 'http://localhost:5000/get_filtered_messages'

ui.page_opts(
    title="Hello EDEM Chat",
    fillable=True,
    fillable_mobile=True,
)

# Create a chat instance and display it
chat = ui.Chat(id="chat")  
chat.ui()  

# Define a callback to run when the user submits a message
@chat.on_user_submit  
async def _():  
    # Simply echo the user's input back to them
    # STEP 1 Enviar
    user_message = chat.user_input()
    await chat.append_message("Message received") 

    response = requests.post(API_URL, json={"message": user_message})

    if response.status_code == 200:
        await chat.append_message("Message successfully sent!")
    else:
        await chat.append_message("Error sending message to API.")
    
    # STEP 2 filtered message
    filtered_message = None
    for i in range(5):
        filtered_response = requests.get(FILTERED_API_URL, timeout=5.0)

        if filtered_response.status_code == 200:
            filtered_message = filtered_response.json().get("message", "")
            if filtered_message:
                break
        await asyncio.sleep(5)

    if filtered_message:
        await chat.append_message(f"You said: {filtered_message}")
    else:
        await chat.append_message("Error fetching filtered message or no message available.")

    # filtered_response = requests.get(FILTERED_API_URL)
    # filtered_message = filtered_response.json().get("message","")

    # if filtered_response.status_code == 200:
    #     await chat.append_message(f"You said:{filtered_message}")
    # else:
    #     await chat.append_message("Error fetching filtered message.")

async def add_kafka_messages():
    messages = [
        "Hello, how can I help you?",
        "What can I do for you today?",
        "Here is a random fact: The Eiffel Tower can be 15 cm taller during the summer.",
        "Did you know? Honey never spoils.",
        "Random message incoming!"
    ]
    while True:
        await asyncio.sleep(7)
        # STEP 1 Recibir
        random_message = random.choice(messages)
        await chat.append_message(f"Bot: {random_message}")

def run_asyncio_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(add_kafka_messages())

# Start the background thread
thread = threading.Thread(target=run_asyncio_loop, daemon=True)
thread.start()
