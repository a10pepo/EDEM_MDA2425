""" 
Script: Pubsub Class

Description: Class to group all methods for performing operations in Google PubSub.

EDEM. Master Big Data & Cloud 2024/2025
Professor: Javi Briones
"""

""" Import Libraries """

# A. Python Libraries
import logging
import json

# B. Google Cloud Libraries
from google.cloud import pubsub_v1

""" Code """

class PubSubMessages:

    """ Publish Messages in our PubSub Topic """

    def __init__(self, project_id: str):

        """
        Initialize the PubSubMessages class.

        Params:
            project_id(str): Google Cloud Project ID.

        Returns: 
            -
        """

        self.publisher = pubsub_v1.PublisherClient()
        self.project_id = project_id

        logging.info("PubSub Client initialized.")

    def publishMessages(self, payload: dict, topic_name: str):

        """
        Publishes the desired message to the specified topic.

        Params:
            payload(dict): Vehicle Telemetry Data Payload.
            topic_name(str): Google PubSub Topic Name.

        Returns: 
            -

        """

        json_str = json.dumps(payload).encode("utf-8")

        topic_path = self.publisher.topic_path(self.project_id, topic_name)
        self.publisher.publish(topic_path, json_str)

    def __exit__(self):
        
        self.publisher.transport.close()

        logging.info("PubSub Client closed.")