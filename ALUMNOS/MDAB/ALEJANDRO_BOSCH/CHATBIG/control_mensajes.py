from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
from confluent_kafka import Producer
import json


KAFKA_BROKER = "kafka:29092"
KAFKA_INPUT_TOPIC = "chat"
KAFKA_OUTPUT_TOPIC = "chat_controlled"

BAD_WORDS = ["tonto", "gilipollas", "culo", "mierda", "capullo"]

user_warnings = {}

#Funcion para censurar

def censor_message(message):
    words = message.split()
    censored = ["*" * len(words) if words.lower() in BAD_WORDS else word for word in words]
    return " ".join(censored)

#Aplicamos Funcion UDF
censor_message_udf = udf(censor_message, StringType())

def handle_warnings(author, message):
    if any(word.lower() in BAD_WORDS for word in message.split()):
        user_warnings[author] = user_warnings.get(author, 0) + 1
        if user_warnings[author] >= 3:
            return True  #Bloquea al usuario
    return False

# Función para enviar mensajes al topic `chat_controlled`
def send_to_kafka(payload):
    producer_conf = {
        'bootstrap.servers': KAFKA_BROKER,
        'client.id': 'spark-producer',
        'security.protocol': 'PLAINTEXT'
    }
    producer = Producer(producer_conf)
    producer.produce(
        KAFKA_OUTPUT_TOPIC,
        value=json.dumps(payload).encode('utf-8')
    )
    producer.flush()

# Configuración de Spark
spark = SparkSession.builder.appName("MessageControl").master("local[*]").getOrCreate()

# Leer mensajes de Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BROKER) \
    .option("subscribe", KAFKA_INPUT_TOPIC) \
    .load()

# Procesar mensajes
messages = df.selectExpr("CAST(value AS STRING)").withColumn("value", col("value"))

def process_batch(batch_df, batch_id):
    rows = batch_df.collect()
    for row in rows:
        try:
            # Decodificar el mensaje
            data = json.loads(row.value)
            author = data.get("author", "unknown")
            message = data.get("data", "")
            timestamp = data.get("timestamp", "")

            # Manejar avisos y censurar el mensaje
            is_blocked = handle_warnings(author, message)
            censored_message = censor_message(message) if not is_blocked else "Mensaje bloqueado"

            # Crear mensaje de salida
            output_payload = {
                "author": author,
                "data": censored_message,
                "timestamp": timestamp,
                "blocked": is_blocked
            }

            # Enviar mensaje al topic `chat_controlled`
            send_to_kafka(output_payload)
        except Exception as e:
            print(f"Error al procesar el mensaje: {e}")

# Procesar cada batch
messages.writeStream.foreachBatch(process_batch).start().awaitTermination()