from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count, avg

spark = SparkSession.builder \
    .appName("spark_exercise_users_orders") \
    .getOrCreate()
print(spark)

def save_to_mysql(df, table_name, jdbc_url, user, password):
    df.write.format("jdbc") \
        .option("url", jdbc_url) \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .option("dbtable", table_name) \
        .option("user", user) \
        .option("password", password) \
        .mode("overwrite") \
        .save()

jdbc_url       = "jdbc:mysql://mysql:3306/pysparkdb"
mysql_user     = "spark"
mysql_password = "password"

users_path  = "/mnt/data/users.csv"
orders_path = "/mnt/data/orders.csv"

users_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(users_path)

orders_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(orders_path)

save_to_mysql(users_df,  "users",  jdbc_url, mysql_user, mysql_password)
save_to_mysql(orders_df, "orders", jdbc_url, mysql_user, mysql_password)

filtered_users = users_df.filter(col("country") == "USA")
filtered_users.show()
save_to_mysql(filtered_users, "filtered_users_usa", jdbc_url, mysql_user, mysql_password)

high_value_orders = orders_df.filter(col("amount") > 100)
high_value_orders.show()
save_to_mysql(high_value_orders, "high_value_orders", jdbc_url, mysql_user, mysql_password)

updated_orders = orders_df.withColumn(
    "status_description",
    when(col("status") == "PAID",       "Completed")
    .when(col("status") == "CANCELLED", "Cancelled")
    .otherwise("Pending")
)
updated_orders.show()
save_to_mysql(updated_orders, "updated_orders", jdbc_url, mysql_user, mysql_password)

joined_df = users_df.join(orders_df, on="user_id", how="inner")
joined_df.show()
save_to_mysql(joined_df, "users_with_orders", jdbc_url, mysql_user, mysql_password)

orders_per_country = joined_df.groupBy("country") \
    .agg(count("order_id").alias("order_count"))
orders_per_country.show()
save_to_mysql(orders_per_country, "orders_per_country", jdbc_url, mysql_user, mysql_password)

spain_users     = users_df.filter(col("country") == "Spain")
spain_orders    = orders_df.join(spain_users, on="user_id", how="inner")
count_by_status = spain_orders.groupBy("status") \
    .agg(count("order_id").alias("order_count"))
count_by_status.show()
save_to_mysql(count_by_status, "spain_orders_by_status", jdbc_url, mysql_user, mysql_password)

spark.stop()
