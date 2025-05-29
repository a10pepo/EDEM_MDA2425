from pyspark.sql import SparkSession
from pyspark.sql.functions import *

'Configuración Spark'
spark = SparkSession.builder.appName("Football Analysis").config("spark.jars", "/spark/jars/mysql-connector-j-8.0.33.jar").getOrCreate()

def save_to_mysql(df, table_name, jdbc_url, user, password):
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
mysql_user = "spark"
mysql_password = "password"

footballDF = spark.read.option("header", "true").option("inferSchema", "true").csv("/opt/project/resources/Football.csv")

#Top 10 equipos con más goles a favor
topScoringTeamsDF = footballDF.groupBy("home_team").agg(sum(col("home_score").cast("int")).alias("Total_Goals")).orderBy(col("Total_Goals").desc()).limit(10)
topScoringTeamsDF.show()
save_to_mysql(topScoringTeamsDF, "top_scoring_teams", jdbc_url, mysql_user, mysql_password)

#Top 10 equipos con más goles en contra
topConcedingTeamsDF = footballDF.groupBy("away_team").agg(sum(col("away_score").cast("int")).alias("Goals_Conceded")).orderBy(col("Goals_Conceded").desc()).limit(10)
topConcedingTeamsDF.show()
save_to_mysql(topConcedingTeamsDF, "top_conceding_teams", jdbc_url, mysql_user, mysql_password)
