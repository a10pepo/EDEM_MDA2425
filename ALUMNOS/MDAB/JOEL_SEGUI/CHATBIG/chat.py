from shiny.express import ui
from datetime import datetime
import threading
import random
import asyncio
import json #Para serializar los msg en formato diccionario

#Mi script
from producer import create_producer, send_message

producer = create_producer()
topic = "chat"
user_key = "Joel S.F."
bot_key = "Kafka_bot"


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
    msg = chat.user_input()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg_clean = {
    'author': user_key,
    "data": msg,
    'timestamp': timestamp
}
    await chat.append_message(f"You said: {msg_clean}") 
    send_message(producer, topic, key=user_key, value=json.dumps(msg_clean)) #Usamos el json.dumps porq hay que serializar le código (no se puede "meter" un diccionario en kafka si no se serializa)

async def add_kafka_messages():
    messages = [
        "Hello, how can I help you?",
        "What can I do for you today?",
        "Here is a random fact: The Eiffel Tower can be 15 cm taller during the summer.",
        "Did you know? Honey never spoils.",
        "Random message incoming!"
    ]
    while True:
        await asyncio.sleep(20)
        # STEP 1 Recibir
        random_message = random.choice(messages)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        await chat.append_message({
            'author': bot_key,
            'content': random_message,
            'timestamp': timestamp
        })
        send_message(producer, topic, key = bot_key, value = json.dumps(random_message))

def run_asyncio_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(add_kafka_messages())

# Start the background thread
thread = threading.Thread(target=run_asyncio_loop, daemon=True)
thread.start()