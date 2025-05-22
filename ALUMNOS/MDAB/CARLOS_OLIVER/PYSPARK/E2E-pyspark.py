#pip install pyspark
#!pip install kagglehub

import pyspark
from pyspark.sql import SparkSession
import kagglehub
from pyspark.sql.functions import col, monotonically_increasing_id, when, lit, regexp_replace, udf
from pyspark.sql.types import FloatType, IntegerType
import random


spark = SparkSession.builder.appName('spark-E2E').getOrCreate()

spark

import kagglehub

# Download latest version
path = kagglehub.dataset_download("ramjasmaurya/top-1000-social-media-channels")

print("Path to dataset files:", path)

df_youtube_sep = spark.read.option('header', 'true').csv('/Users/carlosoliver/.cache/kagglehub/datasets/ramjasmaurya/top-1000-social-media-channels/versions/13/social media influencers - Youtube sep-2022.csv')
df_youtube_jun = spark.read.option('header', 'true').csv('/Users/carlosoliver/.cache/kagglehub/datasets/ramjasmaurya/top-1000-social-media-channels/versions/13/social media influencers-youtube june 2022 - june 2022.csv')
df_youtube_nov = spark.read.option('header', 'true').csv('/Users/carlosoliver/.cache/kagglehub/datasets/ramjasmaurya/top-1000-social-media-channels/versions/13/social media influencers-youtube - --nov 2022.csv')
df_youtube_dic = spark.read.option('header', 'true').csv('/Users/carlosoliver/.cache/kagglehub/datasets/ramjasmaurya/top-1000-social-media-channels/versions/13/social media influencers-YOUTUBE - --DEC 2022.csv')

df_youtube_sep.show()
df_youtube_nov.show()

df_youtube_jun.printSchema()
df_youtube_sep.printSchema()
df_youtube_nov.printSchema()
df_youtube_dic.printSchema()


print(f"Filas: {df_youtube_dic.count()}, Columnas: {len(df_youtube_dic.columns)}")
print(f"Filas: {df_youtube_jun.count()}, Columnas: {len(df_youtube_jun.columns)}")

# Eliminar las columnas 'Comments avg.' y 'Likes avg'
df_youtube_jun = df_youtube_jun.drop("Comments avg.", "Likes avg", "Category_2")
df_youtube_sep = df_youtube_sep.drop("S.No")
df_youtube_nov = df_youtube_nov.drop("s.No")
df_youtube_dic = df_youtube_dic.drop("s.no")


df_youtube_jun.printSchema()
df_youtube_sep.printSchema()
df_youtube_nov.printSchema()
df_youtube_dic.printSchema()

df_youtube_jun = df_youtube_jun.withColumnRenamed("channel name","Channel_name_jun") \
       .withColumnRenamed("Views avg.", "Views_avg_jun")\
       .withColumnRenamed("youTuber", "Youtuber_name_jun")\
       .withColumnRenamed("Category", "Category_jun")\
       .withColumnRenamed("Subscribers count", "Subscribers_jun")\
       .withColumnRenamed("Country", "Country_jun")

df_youtube_jun.printSchema()

df_youtube_sep = df_youtube_sep.withColumnRenamed("Name","Channel_name_sep") \
       .withColumnRenamed("Avg. views", "Views_avg_sep")\
       .withColumnRenamed("Youtuber", "Youtuber_name_sep")\
       .withColumnRenamed("Category_2", "Category_sep")\
       .withColumnRenamed(" Subscribers", "Subscribers_sep")\
       .withColumnRenamed("Country", "Country_sep")

df_youtube_sep.printSchema()

df_youtube_nov = df_youtube_nov.withColumnRenamed("Youtube channel","Channel_name_nov") \
       .withColumnRenamed('Views_avg_sep', "Views_avg_nov")\
       .withColumnRenamed("youtuber name", "Youtuber_name_nov")\
       .withColumnRenamed("Category", "Category_nov")\
       .withColumnRenamed("Followers", "Subscribers_nov")\
       .withColumnRenamed("Country", "Country_nov")

df_youtube_nov.printSchema()

df_youtube_dic = df_youtube_dic.withColumnRenamed("Youtube channel","Channel_name_dic") \
       .withColumnRenamed('"', "Views_avg_dic")\
       .withColumnRenamed("youtuber name", "Youtuber_name_dic")\
       .withColumnRenamed("Category", "Category_dic")\
       .withColumnRenamed("Followers", "Subscribers_dic")\
       .withColumnRenamed("Country", "Country_dic")

df_youtube_dic.printSchema()

# from pyspark.sql.functions import col, udf
# from pyspark.sql.types import IntegerType
# import random

# # Función para generar un número aleatorio en el rango dado
# def random_value():
#     return random.randint(900000, 50000000)

# # Registrar la función como UDF
# random_udf = udf(random_value, IntegerType())

# # Reemplazar las columnas con valores aleatorios
# df_youtube_jun = (
#     df_youtube_jun.withColumn("Subscribers_jun", random_udf())
#       .withColumn("Views_avg_jun", random_udf())
# )

# # Reemplazar las columnas con valores aleatorios
# df_youtube_sep = (
#     df_youtube_sep.withColumn("Subscribers_sep", random_udf())
#       .withColumn("Views_avg_sep", random_udf())
# )

# # Reemplazar las columnas con valores aleatorios
# df_youtube_nov = (
#     df_youtube_nov.withColumn("Subscribers_nov", random_udf())
#       .withColumn("Views_avg_nov", random_udf())
# )

# # Reemplazar las columnas con valores aleatorios
# df_youtube_dic = (
#     df_youtube_dic.withColumn("Subscribers_dic", random_udf())
#       .withColumn("Views_avg_dic", random_udf())
# )

# June

df_youtube_jun.show()

df_youtube_sep.show()   

df_youtube_nov.show()

df_youtube_dic.show()

df_youtube_jun.printSchema()
df_youtube_sep.printSchema()
df_youtube_nov.printSchema()
df_youtube_dic.printSchema()

df_jun = df_youtube_jun.select(
    "Channel_name_jun", "Youtuber_name_jun", "Subscribers_jun", "Views_avg_jun"
)

df_sep = df_youtube_sep.select(
    "Channel_name_sep", "Youtuber_name_sep", "Subscribers_sep", "Views_avg_sep"
)

df_nov = df_youtube_nov.select(
    "Channel_name_nov", "Youtuber_name_nov", "Subscribers_nov", "Views_avg_nov"
)

df_dic = df_youtube_dic.select(
    "Channel_name_dic", "Youtuber_name_dic", "Subscribers_dic", "Views_avg_dic"
)

df_jun.show()

df_jun = df_jun.withColumnRenamed("Channel_name_jun", "Channel_name") \
               .withColumnRenamed("Youtuber_name_jun", "Youtuber_name") \
               .withColumnRenamed("Subscribers_jun", "Subscribers_jun") \
               .withColumnRenamed("Views_avg_jun", "Views_avg_jun")

df_sep = df_sep.withColumnRenamed("Channel_name_sep", "Channel_name") \
               .withColumnRenamed("Youtuber_name_sep", "Youtuber_name") \
               .withColumnRenamed("Subscribers_sep", "Subscribers_sep") \
               .withColumnRenamed("Views_avg_sep", "Views_avg_sep")

df_nov = df_nov.withColumnRenamed("Channel_name_nov", "Channel_name") \
               .withColumnRenamed("Youtuber_name_nov", "Youtuber_name") \
               .withColumnRenamed("Subscribers_nov", "Subscribers_nov") \
               .withColumnRenamed("Views_avg_nov", "Views_avg_nov")

df_dic = df_dic.withColumnRenamed("Channel_name_dic", "Channel_name") \
               .withColumnRenamed("Youtuber_name_dic", "Youtuber_name") \
               .withColumnRenamed("Subscribers_dic", "Subscribers_dic") \
               .withColumnRenamed("Views_avg_dic", "Views_avg_dic")

df_combined = df_jun.join(df_sep, on=["Channel_name", "Youtuber_name"], how="outer") \
                   .join(df_nov, on=["Channel_name", "Youtuber_name"], how="outer") \
                   .join(df_dic, on=["Channel_name", "Youtuber_name"], how="outer")

df_combined.show()

# Crecimiento en Subscribers entre junio y septiembre
df_combined = df_combined.withColumn("growth_subscribers_jun_sep", 
                                     (col("Subscribers_sep") - col("Subscribers_jun")) / col("Subscribers_jun") * 100)

# Crecimiento en Views_avg entre junio y septiembre
df_combined = df_combined.withColumn("growth_views_jun_sep", 
                                     (col("Views_avg_sep") - col("Views_avg_jun")) / col("Views_avg_jun") * 100)

# Crecimiento en Subscribers entre septiembre y noviembre
df_combined = df_combined.withColumn("growth_subscribers_sep_nov", 
                                     (col("Subscribers_nov") - col("Subscribers_sep")) / col("Subscribers_sep") * 100)

# Crecimiento en Views_avg entre septiembre y noviembre
df_combined = df_combined.withColumn("growth_views_sep_nov", 
                                     (col("Views_avg_nov") - col("Views_avg_sep")) / col("Views_avg_sep") * 100)

# Crecimiento en Subscribers entre noviembre y diciembre
df_combined = df_combined.withColumn("growth_subscribers_nov_dic", 
                                     (col("Subscribers_dic") - col("Subscribers_nov")) / col("Subscribers_nov") * 100)

# Crecimiento en Views_avg entre noviembre y diciembre
df_combined = df_combined.withColumn("growth_views_nov_dic", 
                                     (col("Views_avg_dic") - col("Views_avg_nov")) / col("Views_avg_nov") * 100)

df_combined = df_combined.fillna(0, subset=["growth_subscribers_jun_sep", "growth_views_jun_sep",
                                            "growth_subscribers_sep_nov", "growth_views_sep_nov",
                                            "growth_subscribers_nov_dic", "growth_views_nov_dic"])

df_combined.show(truncate=False)


# Calcular el crecimiento promedio de Subscribers entre los meses
df_combined = df_combined.withColumn(
    "growth_subscribers_total",
    (col("growth_subscribers_jun_sep") + col("growth_subscribers_sep_nov") + col("growth_subscribers_nov_dic")) / 3
)

# Calcular el crecimiento promedio de Views_avg entre los meses
df_combined = df_combined.withColumn(
    "growth_views_total",
    (col("growth_views_jun_sep") + col("growth_views_sep_nov") + col("growth_views_nov_dic")) / 3
)

# Calcular el crecimiento total combinado, ponderando igual entre Subscribers y Views_avg
df_combined = df_combined.withColumn(
    "growth_total",
    (col("growth_subscribers_total") + col("growth_views_total")) / 2
)

# Ordenar por el crecimiento total y seleccionar el top 10
df_top_10 = df_combined.orderBy(col("growth_total").desc()).limit(10)

df_top_10.select("Channel_name", "Youtuber_name", "growth_total").show(truncate=False)

# Crecimiento porcentual de Subscribers entre los meses
df_combined = df_combined.withColumn(
    "growth_subscribers_jun_sep",
    ((col("Subscribers_sep") - col("Subscribers_jun")) / col("Subscribers_jun")) * 100
)

df_combined = df_combined.withColumn(
    "growth_subscribers_sep_nov",
    ((col("Subscribers_nov") - col("Subscribers_sep")) / col("Subscribers_sep")) * 100
)

df_combined = df_combined.withColumn(
    "growth_subscribers_nov_dic",
    ((col("Subscribers_dic") - col("Subscribers_nov")) / col("Subscribers_nov")) * 100
)

# Crecimiento porcentual de Views_avg entre los meses
df_combined = df_combined.withColumn(
    "growth_views_jun_sep",
    ((col("Views_avg_sep") - col("Views_avg_jun")) / col("Views_avg_jun")) * 100
)

df_combined = df_combined.withColumn(
    "growth_views_sep_nov",
    ((col("Views_avg_nov") - col("Views_avg_sep")) / col("Views_avg_sep")) * 100
)

df_combined = df_combined.withColumn(
    "growth_views_nov_dic",
    ((col("Views_avg_dic") - col("Views_avg_nov")) / col("Views_avg_nov")) * 100
)

# Promedio del crecimiento porcentual de Subscribers
df_combined = df_combined.withColumn(
    "growth_subscribers_total",
    (col("growth_subscribers_jun_sep") + col("growth_subscribers_sep_nov") + col("growth_subscribers_nov_dic")) / 3
)

# Promedio del crecimiento porcentual de Views_avg
df_combined = df_combined.withColumn(
    "growth_views_total",
    (col("growth_views_jun_sep") + col("growth_views_sep_nov") + col("growth_views_nov_dic")) / 3
)

# Crecimiento porcentual total combinado
df_combined = df_combined.withColumn(
    "growth_total",
    (col("growth_subscribers_total") + col("growth_views_total")) / 2
)

# Ordenar por el crecimiento total y seleccionar el top 10
df_top_10 = df_combined.orderBy(col("growth_total").desc()).limit(10)

# Mostrar el resultado
df_top_10.select("Channel_name", "Youtuber_name", "growth_total", "growth_views_total").show(truncate=False)

