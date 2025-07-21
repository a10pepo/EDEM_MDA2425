import polars as pl
from confluent_kafka import Producer
import json
import time

kafka_producer_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'retail-producer'
}

producer = Producer(kafka_producer_config)
kafka_topic = 'retail'

def load_dataset(path: str) -> pl.DataFrame:
    df = pl.read_csv(path, encoding='latin1', schema_overrides={'InvoiceNo': pl.Utf8, 'CustomerID': pl.Utf8})
    return df.select([
        'InvoiceNo', 'StockCode', 'Description',
        'Quantity', 'InvoiceDate',
        'UnitPrice', 'CustomerID', 'Country'
    ])

def send_data_to_kafka(df: pl.DataFrame):
    for row in df.to_dicts():
        message = {
            "invoice_no":   str(row['InvoiceNo']),
            "stock_code":   row['StockCode'],
            "description":  row.get('Description', ''),
            "quantity":     int(row['Quantity']),
            "invoice_date": row['InvoiceDate'],
            "unit_price":   float(row['UnitPrice']),
            "customer_id":  str(row['CustomerID']) if row['CustomerID'] is not None else None,
            "country":      row['Country']
        }
        key = str(row['InvoiceNo'])
        producer.produce(topic=kafka_topic, key=key, value=json.dumps(message))
        print(f"► Sent: {message}")
        time.sleep(0.01)  

    producer.flush()
    print("✅ All messages have been sent.")

if __name__ == "__main__":
    dataset_path = "data.csv"
    df = load_dataset(dataset_path)
    send_data_to_kafka(df)
