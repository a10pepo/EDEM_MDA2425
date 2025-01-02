from shiny.express import ui
import threading
import asyncio
import requests
from producer import send_message

API_URL = "http://localhost:5000"
user = "Alejandro"

# Función para enviar mensajes a Kafka a través de la API REST
def send_message_to_api(author, message):
    # Primero enviamos a través de la API
    response = requests.post(
        f"{API_URL}/send",
        json={"author": author, "message": message}
    )
    if response.status_code == 200:
        # Si la API responde correctamente, también enviamos directamente a Kafka
        try:
            send_message(message, author)
        except Exception as e:
            print(f"Error al enviar mensaje a Kafka directamente: {e}")
        return response.json()
    else:
        raise Exception(f"Error al enviar mensaje: {response.text}")

ui.page_opts(
    title="Hello EDEM Chat",
    fillable=True,
    fillable_mobile=True,
)

chat = ui.Chat(id="chat")  
chat.ui()  

@chat.on_user_submit  
async def _():  
    user_message = chat.user_input()
    try:
        send_message_to_api(user, user_message)
        await chat.append_message(f"You said: {user_message}")
    except Exception as e:
        await chat.append_message(f"Error: {e}")

async def receive_kafka_messages():
    while True:
        try:
            response = requests.get(f"{API_URL}/receive")
            if response.status_code == 200:
                messages = response.json().get("messages", [])
                for msg in messages:
                    author = msg.get("author", "unknown")
                    content = msg.get("data", "")
                    await chat.append_message(f"{author}: {content}")
            else:
                print(f"Error al recibir mensajes: {response.status_code}")
        except Exception as e:
            print(f"Error al conectar con el API: {e}")
        await asyncio.sleep(5)  

def run_asyncio_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(receive_kafka_messages())

thread = threading.Thread(target=run_asyncio_loop, daemon=True)
thread.start()