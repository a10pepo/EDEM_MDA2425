from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.appName('Depression').getOrCreate()

student_df = spark.read.csv("C:/Users/Joel/Desktop/MDATA/EDEM_MDA2425/ALUMNOS/MDAB/JOEL_SEGUI/PYSPARK/e2e_spark/project/resources/student_depression.csv", header=True, inferSchema=True)
therapy_df = spark.read.csv("C:/Users/Joel/Desktop/MDATA/EDEM_MDA2425/ALUMNOS/MDAB/JOEL_SEGUI/PYSPARK/e2e_spark/project/resources/therapy.csv", header=True, inferSchema=True, sep=";")

# Convertimos el id a integer (estaba como bool y no podía hacer el join correctamente)
therapy_df = therapy_df.withColumn("id", col("id").cast(IntegerType()))  

# Eliminamos duplicados
therapy_df = therapy_df.dropDuplicates(["id"])

# Realizamos el left join y eliminamos filas con NA
joined_df = student_df.join(therapy_df, on="id", how="left")
cleaned_df = joined_df.dropna()

# Filtramos solo las filas de las personas que tienen depresión (es decir, = 1)
processed = cleaned_df.filter(col("depression") == 1)

# Seleccionamos las columnas de interés
processed = processed.select("id", "Gender", "Age", "City", "success")

# Agrupar por 'City' (país) y contar los estudiantes con depresión
# Aquí hacemos dos cosas: 
# 1. Contamos los id's (todos los estudiantes con depresión)
# 2. Contamos cuántos 'success' son 'Yes'
country_depression_count = processed.groupBy("City") \
    .agg(
        count("id").alias("depression_count"), 
        count(when(col("success") == "Yes", 1)).alias("success_count") 
    )

country_depression_count_sorted = country_depression_count.orderBy("depression_count", ascending=False)

# Aquí tenemos un dataset que nos muestra el número de personas que han tenido depresion y cuantos de ellos han logrado salir de ella.
country_depression_count_sorted.show()
