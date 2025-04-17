""" 
Script: Cloud Run Job

Description: Cloud Run Job to execute data dumps from Firestore to BigQuery.

EDEM. Master Big Data & Cloud 2024/2025
Professor: Javi Briones
"""

""" Import Libraries """

from google.cloud import firestore
from google.cloud import bigquery
import logging
import json
import os

# Configure clients
firestore_client = firestore.Client()
bigquery_client = bigquery.Client()

# Environment Variables
FIRESTORE_COLLECTION = os.getenv('FIRESTORE_COLLECTION')
BIGQUERY_DATASET = os.getenv('BIGQUERY_DATASET')
BIGQUERY_TABLE = os.getenv('BIGQUERY_TABLE')

""" Code """

def get_all_documents_with_subcollections(collection_name: str):

    """
    Retrieves all documents from a Firestore collection along with their nested subcollections.
    
    Parameters:
        collection_name (str): The name of the Firestore collection to retrieve documents from.

    Returns:
        list: A list of dictionaries containing document data including vehicle_id, event name,
            timestamp, and payload (JSON string format).
    """

    collection_ref = firestore_client.collection(collection_name)
    documents = collection_ref.list_documents()
    
    data = []

    for doc in documents:
        vehicle_id = doc.id  

        # Retrieve subcollections
        subcollections = doc.collections()
        for subcollection in subcollections:
            subcollection_name = subcollection.id 
            sub_docs = subcollection.stream()

            for sub_doc in sub_docs:
                doc_dict = {} 
                sub_doc_dict = sub_doc.to_dict()

                # Build the output format
                doc_dict["vehicle_id"] = vehicle_id
                doc_dict["event"] = subcollection_name
                doc_dict["timestamp"] = sub_doc.id
                doc_dict["payload"] = json.dumps(sub_doc_dict) 

                # Add row to dataset
                data.append(doc_dict)
    
    return data

def upload_to_bigquery(data: list):

    """
    Uploads the data to BigQuery in JSON format.
    
    Parameters:
        data (list): A list of dictionaries containing the data to be uploaded to BigQuery.
    
    Returns:
        None
    """

    table_ref = bigquery_client.dataset(BIGQUERY_DATASET).table(BIGQUERY_TABLE)

    errors = bigquery_client.insert_rows_json(table_ref, data)

    if errors:
        logging.error(" Error inserting into BigQuery:", errors)
    else:
        logging.info("Data successfully inserted into BigQuery.")

if __name__ == "__main__":

    # Set Logs
    logging.getLogger().setLevel(logging.INFO)
    
    # Retrieve data from Firestore
    documents = get_all_documents_with_subcollections(FIRESTORE_COLLECTION)

    if documents:
        # Upload to BigQuery
        upload_to_bigquery(documents)
    else:
        logging.warning("No data available to upload to BigQuery.")