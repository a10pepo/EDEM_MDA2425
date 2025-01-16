import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

object Example extends App {

  val spark = SparkSession.builder()
    .appName("Example")
    .config("spark.master", "local")
    .getOrCreate()

  val exampleDF = spark.read
    .option("inferSchema", "true")
    .csv("src/main/resources/dataset/example.csv")

  exampleDF.show()
}
