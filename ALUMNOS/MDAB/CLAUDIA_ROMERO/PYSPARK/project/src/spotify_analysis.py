from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, avg, count, max, sum

spark = SparkSession.builder \
    .appName("SpotifyWrappedAnalysisExtended") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

tracks_df = spark.read.csv("/opt/project/resources/spotify_tracks.csv", header=True, inferSchema=True)
genres_df = spark.read.csv("/opt/project/resources/genres.csv", header=True, inferSchema=True)

# Canciones populares (popularidad > 50) (FILTER)
popular_tracks = tracks_df.filter(col("popularity") > 50)

# Clasificación del nivel de éxito (WITHCOLUMN)
enriched_tracks = popular_tracks.withColumn(
    "nivel_exito",
    when(col("popularity") > 80, "super hit")
    .when(col("popularity") > 60, "hit")
    .otherwise("conocida")
)

# Unión con dataset de genres (JOIN)
joined_df = enriched_tracks.join(genres_df, on="track_genre", how="left")

# Popularidad media por grupo general (GROUPBY)
popularidad_generos = joined_df.groupBy("grupo_general").agg(
    avg("popularity").alias("popularidad_media")
)
popularidad_generos.show()

# Número de canciones por nivel de éxito (GROUPBY)
nivel_exito_summary = enriched_tracks.groupBy("nivel_exito").agg(
    count("*").alias("total_canciones")
)
nivel_exito_summary.show()

# Canciones más populares (SELECT + ORDERBY)
top_canciones = tracks_df.select("track_name", "artists", "popularity")\
    .orderBy(col("popularity").desc())\
    .limit(10)
top_canciones.show()

# Artistas más populares en el dataset (GROUPBY)
top_artistas = tracks_df.groupBy("artists").agg(
    count("*").alias("total_canciones")
).orderBy(col("total_canciones").desc()).limit(10)
top_artistas.show()

# Total de minutos de música disponibles
total_duracion = tracks_df.select(sum(col("duration_ms")) / 60000).withColumnRenamed("(sum(duration_ms) / 60000)", "minutos_totales")
total_duracion.show()

def save_to_mysql(df, table_name):
    df.write.format("jdbc").options(
        url="jdbc:mysql://mysql:3306/pysparkdb",
        driver="com.mysql.cj.jdbc.Driver",
        dbtable=table_name,
        user="spark",
        password="password"
    ).mode("overwrite").save()

save_to_mysql(popularidad_generos, "popularidad_generos")
save_to_mysql(nivel_exito_summary, "nivel_exito_summary")
save_to_mysql(top_canciones, "top_canciones")
save_to_mysql(top_artistas, "top_artistas")
save_to_mysql(total_duracion, "total_duracion")
