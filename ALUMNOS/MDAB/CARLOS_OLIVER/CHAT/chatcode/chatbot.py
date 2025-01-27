import streamlit as st
from streamlit_chat import message
from datetime import datetime
from confluent_kafka import Producer, Consumer
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
import threading

# Kafka Configuration
KAFKA_BROKER = 'localhost:9092'
INPUT_TOPIC = 'chat_topic'
OUTPUT_TOPIC = 'monitored_messages'
PROCESSED_TOPIC = "processed_chat_messages"  # Topic to send censored messages
USER_WARNINGS = {}

# Offensive words
OFFENSIVE_WORDS = ["fuck", "FUCK", "idiota"]

# Producer for Kafka
producer = Producer({'bootstrap.servers': KAFKA_BROKER})

# Initialize Spark session
spark = SparkSession.builder \
    .appName("KafkaMessageMonitoring") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2") \
    .getOrCreate()
# Function to send messages to Kafka
def send_to_kafka(user, message_data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    producer.produce(INPUT_TOPIC, key=user, value=f"{timestamp}|{message_data}")
    producer.flush()

# Function to filter offensive words
def censor_message(message):
    for word in OFFENSIVE_WORDS:
        message = message.replace(word, '*' * len(word))
    return message

# UDF to apply censorship to messages
censor_udf = udf(censor_message, StringType())

# Function to process messages with Spark
def process_messages():
    df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", KAFKA_BROKER).option("subscribe", INPUT_TOPIC).load()
    df = df.selectExpr("CAST(key AS STRING) as user", "CAST(value AS STRING) as message")
    
    df = df.withColumn("censored_message", censor_udf(col("message")))
    
    def handle_warnings(batch_df, batch_id):
        global USER_WARNINGS
        rows = batch_df.collect()
        for row in rows:
            user = row['user']
            original_message = row['message']
            censored_message = row['censored_message']
            
            if original_message != censored_message:  # If the message was modified due to offensive language
                USER_WARNINGS[user] = USER_WARNINGS.get(user, 0) + 1
                
                # Warning message should also use the censored message
                warning_message = f"Warning {USER_WARNINGS[user]}: Offensive language detected. Your message: {censored_message}"
                producer.produce(OUTPUT_TOPIC, key=user, value=warning_message)
                producer.flush()

                if USER_WARNINGS[user] >= 3:
                    block_message = f"User {user} is blocked for repeated offensive language."
                    producer.produce(OUTPUT_TOPIC, key=user, value=block_message)
                    producer.flush()
                
                # Send censored message to the output topic
                producer.produce(PROCESSED_TOPIC, key=user, value=censored_message)
                producer.flush()
            else:
                # Send original message (if no offensive words detected)
                producer.produce(PROCESSED_TOPIC, key=user, value=original_message)
                producer.flush()

    query = df.writeStream.foreachBatch(handle_warnings).start()
    query.awaitTermination()
    
# Function to start the Spark consumer in a separate thread
def start_spark_consumer():
    threading.Thread(target=process_messages, daemon=True).start()

# Streamlit interface
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [{'author': 'bot', 'data': 'Welcome to the chat!', 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]

# Function to handle user input
def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.user_input = ""  # Clear input field
    send_to_kafka("User", user_input)

# Function to clear chat history
def on_btn_click():
    st.session_state.chat_history = []

# Start Spark consumer in the background
start_spark_consumer()

# UI for the chat
st.title("Kafka Chat")

chat_placeholder = st.empty()

with chat_placeholder.container():
    sorted_history = sorted(st.session_state.chat_history, key=lambda x: x['timestamp'])
    for i, message_data in enumerate(sorted_history):
        author = message_data['author']
        data = message_data['data']
        timestamp = message_data['timestamp']
        is_user = author == "User"
        message(f"{timestamp}: \n {data}", is_user=is_user, key=f"{i}_{author}", avatar_style='adventurer')

    st.button("Clear messages", on_click=on_btn_click)

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")