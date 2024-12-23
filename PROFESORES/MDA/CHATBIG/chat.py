from shiny.express import ui
import time
import threading
import random
import asyncio

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
    await chat.append_message(f"You said: {chat.user_input()}") 

async def add_kafka_messages():
    messages = [
        "Hello, how can I help you?",
        "What can I do for you today?",
        "Here is a random fact: The Eiffel Tower can be 15 cm taller during the summer.",
        "Did you know? Honey never spoils.",
        "Random message incoming!"
    ]
    while True:
        await asyncio.sleep(5)
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