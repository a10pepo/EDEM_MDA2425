from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("spark_exercise").getOrCreate()
print(spark)

#Funcion para guardar en mysql
def save_to_mysql(df, table_name, jdbc_url, user, password):
    df.write.format("jdbc") \
        .option("url", jdbc_url) \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .option("dbtable", table_name) \
        .option("user", user) \
        .option("password", password) \
        .mode("overwrite") \
        .save()

#Conexión con MySQL   
jdbc_url = "jdbc:mysql://mysql:3306/pysparkdb"
mysql_user = "spark"
mysql_password = "password"

#Indicamos las rutas de los archivos
buses_path = "/opt/project/resources/buses.csv"
routes_path = "/opt/project/resources/routes.csv"

#Carga de datos a pyspark
buses_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(buses_path)

routes_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(routes_path)

#Se guardan los DF en MySQL
save_to_mysql(buses_df, "buses", jdbc_url, mysql_user, mysql_password)
save_to_mysql(routes_df, "routes", jdbc_url, mysql_user, mysql_password)

#Autobuses con capacidad mayor a 50
filtered_buses = buses_df.filter(col("capacity") > 50)
filtered_buses.show()
save_to_mysql(filtered_buses, "filtered_buses", jdbc_url, mysql_user, mysql_password)

#Columna añadida indicando si el autobús está "Operativo" o "No Operativo"
updated_buses = buses_df.withColumn(
    "operational_status",
    when(col("status") == "Cancelled", "No Operativo").otherwise("Operativo")
)
updated_buses.show()
save_to_mysql(updated_buses, "updated_buses", jdbc_url, mysql_user, mysql_password)

#Join autobuses y rutas
joined_df = buses_df.join(routes_df, on="route_id", how="inner")
joined_df.show()
save_to_mysql(joined_df, "buses_with_routes", jdbc_url, mysql_user, mysql_password)


#Agrupar por "route_name" y calcular el promedio de capacidad
average_capacity_by_route = joined_df.groupBy("route_name").agg(
    avg("capacity").alias("average_capacity")
)
average_capacity_by_route.show()
save_to_mysql(average_capacity_by_route, "average_capacity_by_route", jdbc_url, mysql_user, mysql_password)


#Filtrar por rutas y contar autobuses
san_diego_routes = routes_df.filter(col("start_point") == "San Diego, CA")
san_diego_buses = joined_df.join(san_diego_routes, on="route_id", how="inner")
count_by_status = san_diego_buses.groupBy("status").agg(count("bus_id").alias("bus_count"))
count_by_status.show()
save_to_mysql(count_by_status, "count_by_status", jdbc_url, mysql_user, mysql_password)


spark.stop()
