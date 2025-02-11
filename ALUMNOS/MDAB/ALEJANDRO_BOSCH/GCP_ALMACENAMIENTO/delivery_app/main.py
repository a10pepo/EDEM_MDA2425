import datetime
import logging
import time
import random
from utils.events_manager import EventsManager


def get_confirmed_orders(message):
    confirmed_orders = []
    try:
        if not isinstance(message, dict) or 'order_id' not in message:
            logger.warning(f"Invalid message format: {message}")
        confirmed_orders.append(message)
        logger.info(f"Storing confirmed order: {message}")
        return confirmed_orders
    except Exception as message_error:
        logger.error(f"Error processing message {message}: {message_error}")
        raise


def post_delivery_messages(publisher, messages):
    for message in messages:
        logging.info(f"Delivering order {message['order_id']}")
        publisher.send_message({
                    "delivery_status": "processing",
                    "order_id": message['order_id'],
                    "event_at": datetime.datetime.now().isoformat()
                })
        time.sleep(random.randint(2, 4))
        publisher.send_message({
            "delivery_status": "delivering",
            "order_id": message['order_id'],
            "event_at": datetime.datetime.now().isoformat()
        })
        time.sleep(random.randint(5, 10))
        publisher.send_message({
            "delivery_status": "delivered",
            "order_id": message['order_id'],
            "event_at": datetime.datetime.now().isoformat()
        })


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger()
    subscriber = EventsManager(subscription_name='order-events-sub')
    subscriber.create_subscriber()
    publisher = EventsManager(topic_name='delivery-events')
    publisher.create_publisher()
    while True:
        try:
            for message in subscriber.consume_messages():
                confirmed_orders = get_confirmed_orders(message)
                if confirmed_orders:
                    post_delivery_messages(publisher, confirmed_orders)
                else:
                    logger.info("No confirmed orders to process. Waiting...")
                    time.sleep(5)
        except KeyboardInterrupt:
            logger.info("Process stopped by user...")
            break
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            time.sleep(5)
