from shiny.express import ui
import threading
import random
import asyncio
import requests

ui.page_opts(
    title="Hello EDEM Chat",
    fillable=True,
    fillable_mobile=True,
)

API_URL = "http://localhost:5000"  # Cambiar si la API Flask está en otro host
user = "Alejandro"

chat = ui.Chat(id="chat")
chat.ui()

@chat.on_user_submit
async def _():
    user_message = chat.user_input()
    user_name = user  # Cambiar según la implementación

    # Enviar mensaje a través de la API REST
    try:
        response = requests.post(
            f"{API_URL}/send",
            json={"message": user_message, "author": user_name}
        )
        if response.status_code == 200:
            await chat.append_message(f"You said: {user_message}")
        else:
            await chat.append_message("Error sending message to API")
    except Exception as e:
        await chat.append_message(f"Error: {str(e)}")

async def add_kafka_messages():
    random_messages = [
        "Hello, how can I help you?",
        "What can I do for you today?",
        "Here is a random fact: The Eiffel Tower can be 15 cm taller during the summer.",
        "Did you know? Honey never spoils.",
        "Random message incoming!"
    ]
    
    while True:
        await asyncio.sleep(5)

        # Obtener mensajes desde la API
        try:
            response = requests.get(f"{API_URL}/messages")
            if response.status_code == 200:
                kafka_messages = response.json()
                for msg in kafka_messages:
                    await chat.append_message(f"{msg['author']}: {msg['message']}")
        except Exception as e:
            await chat.append_message(f"Error fetching messages: {str(e)}")

        # Enviar mensaje aleatorio
        random_message = random.choice(random_messages)
        await chat.append_message(f"Bot: {random_message}")

def run_asyncio_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(add_kafka_messages())

# Iniciar el hilo en segundo plano
thread = threading.Thread(target=run_asyncio_loop, daemon=True)
thread.start()
