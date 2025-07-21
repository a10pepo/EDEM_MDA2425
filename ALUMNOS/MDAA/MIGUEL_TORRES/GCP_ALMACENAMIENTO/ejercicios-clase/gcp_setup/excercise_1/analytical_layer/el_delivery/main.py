import logging
import os
from datetime import datetime

from utils.db_manager_utils import DbManager
from utils.events_manager import EventsManager


def get_delivery_messages(message):
    delivery_messages = []
    try:
        if not isinstance(message, dict) or 'order_id' not in message:
            logger.warning(f"Invalid message format: {message}")
        delivery_messages.append(message)
        logger.info(f"Storing delivery message: {message}")
        return delivery_messages
    except Exception as message_error:
        logger.error(f"Error processing message {message}: {message_error}")
        raise


def syncronize_delivery_events(db_conn_manager, data):
    delivery_events_value = ", ".join(
                f"""({row['order_id']}, '{row['delivery_status']}',
                    '{datetime.strptime(row['event_at'], '%Y-%m-%dT%H:%M:%S.%f').
                      strftime('%Y-%m-%d %H:%M:%S')}')""" for row in data)
    db_conn_manager.write_events_to_analytical_db(data, 'delivery_events',
                                                  delivery_events_value)


if __name__ == "__main__":
    logging.basicConfig(
                        level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.StreamHandler()
                        ]
    )
    logger = logging.getLogger()
    delivery_message_consumer = EventsManager(subscription_name='delivery-events-sub')
    delivery_message_consumer.create_subscriber()
    all_events = []
    OLAP_DB_CONFIG = {
        "host": os.getenv('HOST_IP'),
        "port": 9001,
        "database": "analytics_db",
        "user": "user",
        "password": "password",
        "send_receive_timeout": 10
    }
    logging.info("Starting syncronization.")
    db_conn_manager = DbManager({}, OLAP_DB_CONFIG)
    try:
        for message in delivery_message_consumer.consume_messages():
            delivery_event = get_delivery_messages(message)
            all_events.append(delivery_event[0])
            if len(all_events) == 150:
                syncronize_delivery_events(db_conn_manager, all_events)
                all_events = []
    except Exception as e:
        logging.error(f"Error in main execution: {e}")
    finally:
        if all_events:
            logging.info(f"Processing remaining {len(all_events)} events.")
            syncronize_delivery_events(db_conn_manager, all_events)
        logging.info("All messages consumed. Exiting.")
