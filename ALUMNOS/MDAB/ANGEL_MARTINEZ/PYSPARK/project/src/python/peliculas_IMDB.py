from pyspark.sql import SparkSession
from pyspark.sql.functions import *

'Configuración Spark'
spark = SparkSession.builder.appName("IMDB Analysis").getOrCreate()

# Cargar el archivo IMDB
imdbDF = spark.read.option("header", "true").option("inferSchema", "true").csv("/opt/project/resources/IMDB.csv")
imdbDF = imdbDF.withColumn("Gross", regexp_replace("Gross", ",", "").cast("double"))

# Análisis: Top 10 películas mejor calificadas
topRatedDF = imdbDF.select("Series_Title", "IMDB_Rating").orderBy(col("IMDB_Rating").desc()).limit(10)
topRatedDF.show()

# Análisis: Top 10 películas con mayor recaudación
topGrossingDF = imdbDF.select("Series_Title", "Gross").orderBy(col("Gross").desc()).limit(10)
topGrossingDF.show()

# Análisis: Top 10 películas con más votos
topVotedDF = imdbDF.select("Series_Title", "No_of_Votes").orderBy(col("No_of_Votes").desc()).limit(10)
topVotedDF.show()

# Análisis: Géneros más comunes
genreCountsDF = imdbDF.select(explode(split(col("Genre"), ", ")).alias("Genre")).groupBy("Genre").count().orderBy(col("count").desc()).limit(10)
genreCountsDF.show()

# Análisis: Mejores calificaciones por género
genreRatingsDF = imdbDF.select(explode(split(col("Genre"), ", ")).alias("Genre"), "IMDB_Rating").groupBy("Genre").avg("IMDB_Rating").orderBy(col("avg(IMDB_Rating)").desc()).limit(10)
genreRatingsDF.show()

# Análisis: Calificación media por década
imdbDF = imdbDF.withColumn("Decade", (col("Released_Year") / 10).cast("int") * 10)
decadeRatingsDF = imdbDF.groupBy("Decade").avg("IMDB_Rating").orderBy("Decade")
decadeRatingsDF.show()

# Análisis: Recaudación media por década
decadeGrossDF = imdbDF.groupBy("Decade").avg("Gross").orderBy("Decade")
decadeGrossDF.show()

# Análisis: Directores con más películas
directorCountsDF = imdbDF.groupBy("Director").count().orderBy(col("count").desc()).limit(10)
directorCountsDF.show()
