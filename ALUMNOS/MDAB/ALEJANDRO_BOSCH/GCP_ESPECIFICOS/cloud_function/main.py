""" 
Script: Cloud Run Functions

Description: Cloud Run function that executes in response to a new message 
    in a PubSub topic and sends the notification to the device.

EDEM. Master Big Data & Cloud 2024/2025
Professor: Javi Briones
"""

""" Import Libraries """

import json
import base64
import logging
import functions_framework

# Set Logs
logging.getLogger().setLevel(logging.INFO)

""" Code: Entry point """
# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def get_pubsub_message(cloud_event):

    """
    Simulates receiving a PubSub message and processes it to send data to Firebase.

    Parameters:
        cloud_event (dict): The Cloud Event message containing the PubSub payload.

    Returns:
        dict: A message containing the processed message data that would be sent to Firebase.
    """
    
    # Dealing with the Pubsub message
    pubsub_msg = base64.b64decode(cloud_event.data["message"]["data"])
    msg = json.loads(pubsub_msg)

    # Find the nearest Supercharger (optional)
    # ToDo

    # Notification content
    content = f"""
        {msg['message']}
    """

    # Print out the message to simulate a call to Firebase
    logging.info(content)