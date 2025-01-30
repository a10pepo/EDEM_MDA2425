from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("spark_exercise").getOrCreate()
print(spark)

buses_path = "/opt/project/resources/buses.csv"
routes_path = "/opt/project/resources/routes.csv"

buses_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(buses_path)

routes_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(routes_path)

#Autobuses con capacidad mayor a 50
filtered_buses = buses_df.filter(col("capacity") > 50)
filtered_buses.show()

#Columna añadida indicando si el autobús está "Operativo" o "No Operativo"
updated_buses = buses_df.withColumn(
    "operational_status",
    when(col("status") == "Cancelled", "No Operativo").otherwise("Operativo")
)
updated_buses.show()

#Join autobuses y rutas
joined_df = buses_df.join(routes_df, on="route_id", how="inner")
joined_df.show()

#Agrupar por "route_name" y calcular el promedio de capacidad
average_capacity_by_route = joined_df.groupBy("route_name").agg(
    avg("capacity").alias("average_capacity")
)
average_capacity_by_route.show()

#Filtrar por rutas y contar autobuses
san_diego_routes = routes_df.filter(col("start_point") == "San Diego, CA")
san_diego_buses = joined_df.join(san_diego_routes, on="route_id", how="inner")
count_by_status = san_diego_buses.groupBy("status").agg(count("bus_id").alias("bus_count"))
count_by_status.show()

spark.stop()
