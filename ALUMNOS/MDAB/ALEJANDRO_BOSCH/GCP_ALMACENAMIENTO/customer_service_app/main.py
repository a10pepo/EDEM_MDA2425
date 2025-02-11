import datetime
import logging
import time
import random
import requests
from utils.events_manager import EventsManager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger()

FAKESTORE_API_USERS = "https://fakestoreapi.com/users"

REQUEST_TYPES = {
    "processing": "Order Processing Delay",
    "delivering": "Order in Transit Issue",
    "delivered": "Order Received Issue",
}


def get_fake_customer():
    """Obtiene un cliente real desde FakeStoreAPI."""
    try:
        response = requests.get(FAKESTORE_API_USERS)
        if response.status_code == 200:
            users = response.json()
            user = random.choice(users) 
            return {
                "customer_id": user["id"],
                "customer_name": f"{user['name']['firstname']} {user['name']['lastname']}",
                "email": user["email"]
            }
    except Exception as e:
        logger.error(f"Error obteniendo cliente de FakeStoreAPI: {e}")
    return None


def get_delivery_events(message):
    """Filtra los eventos de entrega para generar solicitudes de soporte."""
    try:
        if not isinstance(message, dict) or 'order_id' not in message or 'delivery_status' not in message:
            logger.warning(f"Formato de mensaje inválido: {message}")
            return None

        logger.info(f"Procesando evento de entrega: {message}")
        return message  

    except Exception as error:
        logger.error(f"Error procesando mensaje {message}: {error}")
        return None


def post_customer_service_messages(publisher, messages):
    """Genera solicitudes de servicio basadas en eventos de entrega y las publica en `customer-service-events`."""
    for message in messages:
        order_id = message["order_id"]
        delivery_status = message["delivery_status"]

        customer = get_fake_customer()
        if not customer:
            logger.warning("No se pudo obtener un cliente de la API. Usando valores genéricos.")
            customer = {
                "customer_id": random.randint(1, 500),
                "customer_name": f"User{random.randint(1, 500)}",
                "email": f"user{random.randint(1,500)}@example.com"
            }

        service_request = {
            "request_id": random.randint(10000, 99999),
            "order_id": order_id,
            "customer_id": customer["customer_id"],
            "customer_name": customer["customer_name"],
            "email": customer["email"],
            "request_type": REQUEST_TYPES.get(delivery_status, "General Inquiry"),
            "created_at": datetime.datetime.utcnow().isoformat(),
            "status": "open"
        }

        publisher.send_message(service_request)
        logger.info(f"Solicitud de servicio generada y enviada: {service_request}")
        time.sleep(random.randint(2, 5))  


if __name__ == "__main__":
    logger.info("Iniciando Customer Service...")

    subscriber = EventsManager(subscription_name="delivery-events-sub")
    subscriber.create_subscriber()

    publisher = EventsManager(topic_name="customer-service-events")
    publisher.create_publisher()

    while True:
        try:
            for message in subscriber.consume_messages():
                delivery_event = get_delivery_events(message)
                if delivery_event:
                    post_customer_service_messages(publisher, [delivery_event])
                else:
                    logger.info("No hay eventos de entrega para procesar. Esperando...")
                    time.sleep(5)

        except KeyboardInterrupt:
            logger.info("Proceso detenido por el usuario...")
            break
        except Exception as e:
            logger.error(f"Error inesperado: {e}")
            time.sleep(5)
