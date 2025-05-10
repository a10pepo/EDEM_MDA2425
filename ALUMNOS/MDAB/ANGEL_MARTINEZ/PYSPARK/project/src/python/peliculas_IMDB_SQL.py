from pyspark.sql import SparkSession
from pyspark.sql.functions import *

'Configuración Spark'
spark = SparkSession.builder.appName("PySpark Transformations").config("spark.jars", "/opt/project/jar/mysql-connector-j-8.0.33.jar").getOrCreate()

# Función para guardar los DF en MySQL
def save_to_mysql(df, table_name, jdbc_url, user,password):
    df.write.format("jdbc") \
        .option("url", jdbc_url) \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .option("dbtable", table_name) \
        .option("user", user) \
        .option("password", password) \
        .mode("overwrite") \
        .save()
    
'Conexión MySQL'
jdbc_url = "jdbc:mysql://mysql:3306/pysparkdb"
mysql_user = "EDEM2425"
mysql_password = "EDEM2425"


# Cargar el archivo IMDB
imdbDF = spark.read.option("header", "true").option("inferSchema", "true").csv("/opt/project/resources/IMDB.csv")
imdbDF = imdbDF.withColumn("Gross", regexp_replace("Gross", ",", "").cast("double"))

# Análisis: Top 10 películas mejor calificadas
topRatedDF = imdbDF.select("Series_Title", "IMDB_Rating").orderBy(col("IMDB_Rating").desc()).limit(10)
topRatedDF.show()
save_to_mysql(topRatedDF, "top_rated_movies", jdbc_url, mysql_user, mysql_password)

# Análisis: Top 10 películas con mayor recaudación
topGrossingDF = imdbDF.select("Series_Title", "Gross").orderBy(col("Gross").desc()).limit(10)
topGrossingDF.show()
save_to_mysql(topGrossingDF, "top_grossing_movies", jdbc_url, mysql_user, mysql_password)

# Análisis: Top 10 películas con más votos
topVotedDF = imdbDF.select("Series_Title", "No_of_Votes").orderBy(col("No_of_Votes").desc()).limit(10)
topVotedDF.show()
save_to_mysql(topVotedDF, "top_voted_movies", jdbc_url, mysql_user, mysql_password)

# Análisis: Géneros más comunes
genreCountsDF = imdbDF.select(explode(split(col("Genre"), ", ")).alias("Genre")).groupBy("Genre").count().orderBy(col("count").desc()).limit(10)
genreCountsDF.show()
save_to_mysql(genreCountsDF, "genre_counts", jdbc_url, mysql_user, mysql_password)

# Análisis: Mejores calificaciones por género
genreRatingsDF = imdbDF.select(explode(split(col("Genre"), ", ")).alias("Genre"), "IMDB_Rating").groupBy("Genre").avg("IMDB_Rating").orderBy(col("avg(IMDB_Rating)").desc()).limit(10)
genreRatingsDF.show()
save_to_mysql(genreRatingsDF, "genre_ratings", jdbc_url, mysql_user, mysql_password)

# Análisis: Calificación media por década
imdbDF = imdbDF.withColumn("Decade", (col("Released_Year") / 10).cast("int") * 10)
decadeRatingsDF = imdbDF.groupBy("Decade").avg("IMDB_Rating").orderBy("Decade")
decadeRatingsDF.show()
save_to_mysql(decadeRatingsDF, "decade_ratings", jdbc_url, mysql_user, mysql_password)

# Análisis: Recaudación media por década
decadeGrossDF = imdbDF.groupBy("Decade").avg("Gross").orderBy("Decade")
decadeGrossDF.show()
save_to_mysql(decadeGrossDF, "decade_gross", jdbc_url, mysql_user, mysql_password)

# Análisis: Directores con más películas
directorCountsDF = imdbDF.groupBy("Director").count().orderBy(col("count").desc()).limit(10)
directorCountsDF.show()
save_to_mysql(directorCountsDF, "director_counts", jdbc_url, mysql_user, mysql_password)