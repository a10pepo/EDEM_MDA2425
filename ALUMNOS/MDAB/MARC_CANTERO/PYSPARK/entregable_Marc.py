from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# Import sql functions
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()

# Creamos los DF
themesDF = spark.read.options(header='True', inferSchema='True').csv("/opt/project/resources/themes.csv")
colorsDF = spark.read.options(header='True', inferSchema='True').csv("/opt/project/resources/colors.csv")
inventoriesDF = spark.read.options(header='True', inferSchema='True').csv("/opt/project/resources/inventories.csv")
inventory_partsDF = spark.read.options(header='True', inferSchema='True').csv("/opt/project/resources/inventory_parts.csv")
inventory_setsDF = spark.read.options(header='True', inferSchema='True').csv("/opt/project/resources/inventory_sets.csv")
part_categoriesDF = spark.read.options(header='True', inferSchema='True').csv("/opt/project/resources/part_categories.csv")
partsDF = spark.read.options(header='True', inferSchema='True').csv("/opt/project/resources/parts.csv")
setsDF = spark.read.options(header='True', inferSchema='True').csv("/opt/project/resources/sets.csv")

# Filtrar y quitar repuestos
inventory_partsDF = inventory_partsDF.filter(col("is_spare") == 0)

# Unir con sets para obtener los nombres de los sets
sets_inventoryDF = inventory_partsDF.join(inventoriesDF, "inventory_id").join(setsDF, "set_num")

# Unir con themes para obtener los nombres de los temas
sets_themesDF = sets_inventoryDF.join(themesDF, setsDF.theme_id == themesDF.id, "inner")

# Agrupar por tema y contar piezas distintas
theme_parts_countDF = sets_themesDF.groupBy("themes.name").agg(countDistinct("part_num").alias("distinct_parts"))

# Ordenar de mayor a menor y mostrar el Top 5
theme_parts_countDF.orderBy(col("distinct_parts").desc()).show(5)



# Agregar una columna para categorizar los sets según su número de piezas
setsDF = setsDF.withColumn(
    "set_category",
    when(col("num_parts") < 100, "Pequeño")
    .when((col("num_parts") >= 100) & (col("num_parts") <= 500), "Mediano")
    .otherwise("Grande")
)

# Traer el nombre del tema de cada set
fullSetsDF = setsDF.select(setsDF["*"], themesDF["name"].alias("theme_name"))

# Agrupar por categoría de set y contar cuántos hay en cada una
categoryCountsDF = fullSetsDF.groupBy("set_category").count()

# Mostrar resultados
categoryCountsDF.show()