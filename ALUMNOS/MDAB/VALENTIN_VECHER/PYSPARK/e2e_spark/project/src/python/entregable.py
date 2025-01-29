from pyspark.sql import SparkSession
from pyspark.sql.functions import * 

spark= SparkSession.builder.appName("PySpark").getOrCreate()

def save_to_mysql(df, table_name, jdbc_url, user, password):
    df.write.format("jdbc")\
        .option("url", jdbc_url)\
        .option("driver", "com.mysql.cj.jdbc.Driver")\
        .option("dbtable", table_name)\
        .option("user", user)\
        .option("password", password)\
        .mode("overwrite").save()
    
jdbc_url = "jdbc:mysql://mysql:3306/pysparkdb"
mysql_user = "spark"
mysql_password = "password"

imdbDF= spark.read.option("header", "true").option("inferSchema", "true").csv("opt/project/resources/imdb.csv")
imdbDF.printSchema()
amazonDF= spark.read.option("header", "true").option("inferSchema", "true").csv("opt/project/resources/amazon.csv")
amazonDF.printSchema()
netflixDF= spark.read.option("header", "true").option("inferSchema", "true").csv("opt/project/resources/netflix.csv")
netflixDF.printSchema()

"ahora guardamos los dataframes en mysql"

save_to_mysql(imdbDF, "imdb_notes", jdbc_url, mysql_user, mysql_password)
save_to_mysql(amazonDF, "amazon_notes", jdbc_url, mysql_user, mysql_password)
save_to_mysql(netflixDF, "netflix_notes", jdbc_url, mysql_user, mysql_password)

'''
# Ahora vamos a hacer transformaciones y guardarlas en mysql
'''

# 1. Peliculas con mejor puntuacion en imdb

best_film_imdb = imdbDF.select(col("Series_Title").alias("Titulo de las peliculas"), col("IMDB_Rating").alias("Rating")).orderBy(col("Rating").desc())
best_film_imdb.show(15, False)
print("Estas son las 5 peliculas con mejor puntuacion en IMDB")
save_to_mysql(best_film_imdb, "best_film_imdb", jdbc_url, mysql_user, mysql_password)
# 2. Numero de peliculas por Genero en IMDB la media de puntuacion de cada genero

notes_genre_imdb = imdbDF.groupBy("Genre").agg(count("*").alias("Numero de peliculas"), round(avg("IMDB_Rating"), 2).alias("Media de puntuacion en IMDB")).orderBy(col("Media de puntuacion en IMDB").desc())
notes_genre_imdb.show(20, False)
print("Numero de peliculas por genero en IMDB y la media de puntuacion de cada genero")
save_to_mysql(notes_genre_imdb, "notes_genre_imdb", jdbc_url, mysql_user, mysql_password)

# 3. Peliculas con mayor duración en Amazon
best_films_amazon = amazonDF.where(col("type") == "Movie").select(col("title").alias("Pelicula"), col("duration").alias("Duracion")).orderBy(col("Duracion").desc())
best_films_amazon.show(15, False)
print("Estas son las peliculas con mayor duracion en Amazon")
print("Como vemos hay algunos erroes ya que parece que hay peliculas que duran 33 horas o que coincide con el año de estreno, esto se debe a errores en la base de datos")
save_to_mysql(best_films_amazon, "best_films_amazon", jdbc_url, mysql_user, mysql_password)

# 4. Peliculas con mayor duración en Netflix
best_films_netflix = netflixDF.where(col("type") == "Movie").select(col("title").alias("Pelicula"), col("duration").alias("Duracion")).orderBy(col("Duracion").desc())
best_films_netflix.show(15, False)
print("Estas son las peliculas con mayor duracion en Netflix")
save_to_mysql(best_films_netflix, "best_films_netflix", jdbc_url, mysql_user, mysql_password)

# 5. Peliculas que se encuentran en las dos plataformas
films_on_amazon_and_netflix = amazonDF.where(col("type") == "Movie").join(netflixDF, amazonDF.title == netflixDF.title, "inner").select(amazonDF.title).distinct()
print("Estas son las peliculas que se encuentran en Amazon y Netflix")
save_to_mysql(films_on_amazon_and_netflix, "films_on_amazon_and_netflix", jdbc_url, mysql_user, mysql_password)

# 6. Peliculas que se encuentran en las dos plataformas
films_on_amazon_and_netflix = films_on_amazon_and_netflix.count()
print(f'''
    ----------------------------------------------------------------------------------------------
      El numero de peliculas que se encuentran en Amazon y Netflix es de {films_on_amazon_and_netflix}
    ----------------------------------------------------------------------------------------------
''')

# 7. Peliculas que se encuentran en las tres plataformas

films_on_amazon_and_netflix_and_imdb = amazonDF.where(col("type") == "Movie").join(netflixDF, amazonDF.title == netflixDF.title, "inner").join(imdbDF, amazonDF.title == imdbDF.Series_Title, "inner").select(amazonDF.title).distinct()
films_on_amazon_and_netflix_and_imdb.show(15, False)
print("Estas son las peliculas que se encuentran en Amazon, Netflix e IMDB")
save_to_mysql(films_on_amazon_and_netflix_and_imdb, "films_on_amazon_and_netflix_and_imdb", jdbc_url, mysql_user, mysql_password)


# 8. Puntuacion media de las peliculas que se encuentran en amazon y en netflix
rating_all_films_all_platforms= imdbDF.join(amazonDF, imdbDF.Series_Title == amazonDF.title , "inner").join(netflixDF, imdbDF.Series_Title == netflixDF.title, "inner").select(imdbDF.Series_Title, imdbDF.IMDB_Rating).desc()
rating_all_films_all_platforms.show(15, False)
print("Estas son las peliculas que se encuentran en Amazon y Netflix y su puntuacion media en IMDB")
save_to_mysql(rating_all_films_all_platforms, "rating_all_films_all_platforms", jdbc_url, mysql_user, mysql_password)