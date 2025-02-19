from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# Import sql functions
from pyspark.sql.functions import *

exampleDF = spark.read.options(header='True', inferSchema='True').csv("/opt/project/resources/example.csv")

exampleDF.show()