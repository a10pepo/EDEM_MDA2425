from confluent_kafka import Producer, Consumer, KafkaError
import json
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("KafkaChatControl").getOrCreate()

topic_in = 'chat'
topic_out = 'chat_controlled'

bad_words = ['asshole', 'bitch', 'cunt', 'jerk']  

kafka_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", topic_in) \
    .load()

kafka_stream = kafka_stream.selectExpr("CAST(value AS STRING) as message")

for word in bad_words:
    censored = "*" * len(word)
    kafka_stream = kafka_stream.withColumn("message", 
                                           regexp_replace(col("message"), word, censored))

output_stream = kafka_stream.selectExpr("CAST(message AS STRING) as value")

query = output_stream \
    .writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("topic", topic_out) \
    .option("checkpointLocation", "/checkpoint_dir/kafka_chat_control") \
    .start()

query.awaitTermination()
