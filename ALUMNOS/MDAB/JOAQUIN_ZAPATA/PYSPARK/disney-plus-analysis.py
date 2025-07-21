#!/usr/bin/env python3
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Configuración Spark
spark = SparkSession.builder.appName("Disney Plus Analysis").getOrCreate()

# Función para guardar resultados como CSV
def save_to_csv(df, filename):
    df.coalesce(1).write.mode("overwrite").option("header", "true").csv(f"/opt/project/results/{filename}")
    print(f"✅ Guardado: {filename}")

# Cargar dataset Disney+
disneyDF = spark.read.option("header", "true").option("inferSchema", "true").csv("/opt/project/Data/disney_plus_titles.csv")

print("🎬 Dataset Disney+ cargado:")
print(f"Total de títulos: {disneyDF.count()}")
disneyDF.printSchema()

# 1. Distribución de contenido por tipo (Movie vs TV Show)
contentTypeDF = disneyDF.groupBy("type").count().orderBy(col("count").desc())
print("\n📊 Distribución por tipo de contenido:")
contentTypeDF.show()
save_to_csv(contentTypeDF, "content_by_type")

# 2. Top 10 géneros más populares
genresDF = disneyDF.withColumn("genre", split(col("listed_in"), ", ")[0]) \
    .groupBy("genre").count() \
    .orderBy(col("count").desc()).limit(10)
print("\n🎭 Top 10 géneros más populares:")
genresDF.show(truncate=False)
save_to_csv(genresDF, "top_genres")

# 3. Contenido por década de lanzamiento
decadesDF = disneyDF.withColumn("decade", (col("release_year") / 10).cast("int") * 10) \
    .groupBy("decade").count() \
    .orderBy("decade")
print("\n📅 Contenido por década:")
decadesDF.show()
save_to_csv(decadesDF, "content_by_decade")

# 4. Top 10 países con más contenido
countriesDF = disneyDF.filter(col("country").isNotNull()) \
    .withColumn("main_country", split(col("country"), ", ")[0]) \
    .groupBy("main_country").count() \
    .orderBy(col("count").desc()).limit(10)
print("\n🌍 Top 10 países productores:")
countriesDF.show(truncate=False)
save_to_csv(countriesDF, "top_countries")

# 5. Análisis de duración de películas
moviesDF = disneyDF.filter(col("type") == "Movie") \
    .withColumn("duration_minutes", regexp_extract(col("duration"), r"(\d+)", 1).cast("int"))

durationStatsDF = moviesDF.select(
    avg("duration_minutes").alias("avg_duration"),
    min("duration_minutes").alias("min_duration"), 
    max("duration_minutes").alias("max_duration")
)
print("\n🎬 Estadísticas de duración de películas:")
durationStatsDF.show()
save_to_csv(durationStatsDF, "movie_duration_stats")

# 6. Top 10 directores con más contenido
directorsDF = disneyDF.filter(col("director").isNotNull() & (col("director") != "")) \
    .withColumn("main_director", split(col("director"), ", ")[0]) \
    .groupBy("main_director").count() \
    .orderBy(col("count").desc()).limit(10)
print("\n🎯 Top 10 directores:")
directorsDF.show(truncate=False)
save_to_csv(directorsDF, "top_directors")

# 7. Clasificación por audiencia (rating)
ratingDF = disneyDF.withColumn("audience", 
    when(col("rating").isin("G", "TV-G", "TV-Y"), "Kids")
    .when(col("rating").isin("PG", "TV-PG"), "Family")
    .when(col("rating").isin("PG-13", "TV-14"), "Teen")
    .otherwise("Other")
).groupBy("audience").count().orderBy(col("count").desc())
print("\n👨‍👩‍👧‍👦 Contenido por audiencia:")
ratingDF.show()
save_to_csv(ratingDF, "content_by_audience")

print("\n🎉 Análisis completado! Resultados guardados en /opt/project/results/")
spark.stop()