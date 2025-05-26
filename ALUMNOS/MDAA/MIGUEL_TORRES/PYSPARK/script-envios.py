from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, to_date, lit
from pyspark.sql.types import DoubleType

# Crear sesión Spark
spark = SparkSession.builder \
    .appName("ETL Envios Logistica") \
    .getOrCreate()

# Leer CSV
df = spark.read.option("header", True).csv("envios.csv")

# Mostrar datos originales
print("Datos originales:")
df.show()

# ===== TRANSFORMACIONES =====

# 1. Normalizar fecha: convertir strings en formato correcto a tipo fecha
df = df.withColumn("fecha_envio", to_date("fecha_envio", "yyyy-MM-dd"))

# 2. Convertir peso a Double y eliminar envíos con peso negativo o nulo
df = df.withColumn("peso_kg", col("peso_kg").cast(DoubleType()))
df = df.filter((col("peso_kg") > 0) & (col("peso_kg").isNotNull()))

# 3. Eliminar registros sin fecha válida
df = df.filter(col("fecha_envio").isNotNull())

# 4. Añadir columna de "urgencia" en función del tipo de envío
df = df.withColumn(
    "urgencia",
    when(col("tipo_envio") == "express", "alta")
    .when(col("tipo_envio") == "estandar", "baja")
    .otherwise("desconocida")
)

# 5. Enriquecer con campo de "región destino"
regiones = {
    "Madrid": "Centro", "Valencia": "Este", "Barcelona": "Noreste",
    "Sevilla": "Sur", "Bilbao": "Norte", "Granada": "Sur"
}
region_udf = spark.createDataFrame(
    [(k, v) for k, v in regiones.items()],
    ["ciudad", "region"]
)
df = df.join(region_udf, df.destino == region_udf.ciudad, how="left").drop("ciudad")

# Mostrar datos transformados
print("Datos transformados:")
df.show()

# ===== CARGA =====
# Guardamos como parquet particionado por estado
df.write.mode("overwrite").partitionBy("estado").parquet("output/envios_limpios")

spark.stop()
