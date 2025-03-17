from pyspark.sql import SparkSession
from pyspark.sql.functions import *

'Configuración Spark'
spark = SparkSession.builder.getOrCreate()


countryDF= spark.read.option("header", "true").option("inferSchema", "true").csv("/opt/project/resources/Country.csv")
countryDF.printSchema()
countryDF.show(3)

indicatorDF= spark.read.option("header", "true").option("inferSchema", "true").csv("/opt/project/resources/HDI.csv")
indicatorDF.printSchema()
indicator2019DF = indicatorDF.select("HDI Rank", "Country", "2019").orderBy("HDI Rank")
indicator2019DF.show(3)

happinessDF= spark.read.option("header", "true").option("inferSchema", "true").csv("/opt/project/resources/happiness_2019.csv")
happinessDF.printSchema()
happinessDF.show(3)

terrorismDF= spark.read.option("header", "true").option("inferSchema", "true").csv("/opt/project/resources/terrorism.csv")
# terrorismDF.printSchema()
terrorismColumnsDF = terrorismDF.select("eventid", "iyear", "imonth", "iday", "extended", "country","country_txt", "region", "region_txt", "city","multiple","success","suicide","attacktype1", "attacktype1_txt", "targtype1","targtype1_txt")
# terrorismColumnsDF.show(3)

"""## Transformaciones

Countries with most cases of terrorism
"""

WorstCountryTerrorismDF = terrorismColumnsDF.groupBy("country_txt").agg(count("*").alias("totalEvents")).orderBy(col("totalEvents").desc())
WorstCountryTerrorismDF.show(5)

"""Safest countries (less cases of terrorism)"""

SafestCountryDF = terrorismColumnsDF.groupBy("country_txt").agg(count("*").alias("totalEvents")).orderBy(col("totalEvents"))
SafestCountryDF.show(10)

"""Terrorism per region"""

RegionTerrorismDF = terrorismColumnsDF.groupBy("region_txt").agg(count("*").alias("totalEvents")).orderBy(col("totalEvents").desc())
RegionTerrorismDF.show(truncate=False)

"""Terrorism in European countries"""

RegionTerrorismDF.filter((col("region_txt") == "Western Europe") | (col("region_txt") == "Eastern Europe")).show()

EuropeTerrorismDF = terrorismColumnsDF.filter((col("region_txt") == "Western Europe") | (col("region_txt") == "Eastern Europe")).groupBy("region_txt", "country_txt").agg(count("*").alias("totalEvents")).orderBy(col("totalEvents").desc())
EuropeTerrorismDF.show(10)

"""Yearly evolution of terrorism cases"""

yearEvolutionDF = terrorismColumnsDF.groupBy("iyear").agg(count("*").alias("totalEvents")).orderBy(col("iyear").desc())
yearEvolutionDF.show()

"""Year with most cases"""

yearEvolutionDF.orderBy(col("totalEvents").desc()).show(1)

"""For happiness index, correlation between GDP and any index is not directly linear (individually):"""

happinessDF.orderBy(col("GDP per capita").desc()).show(15)

happinessDF.filter(col("Healthy life expectancy") >= 1).orderBy(col("Healthy life expectancy").desc()).show(15)

"""Relation between happiness index and terrorism: there is not a clear correlation. Nevetheless, happier countries tend ot have less terrorism cases."""

happinessTerrorismDF = happinessDF.join(SafestCountryDF, col("Country or region") == col("country_txt"), "inner").orderBy(col("Overall rank").desc()).orderBy("Overall rank").select("Overall rank", "Country or region", "Score", "totalEvents")
happinessTerrorismDF.show(10)
happinessTerrorismDF.orderBy(col("totalEvents").desc()).show(10)
happinessTerrorismDF.orderBy(col("totalEvents").asc()).show(10)

"""Relation between corruption and terrorism: there is not a significant correlation"""

corruptionTerrorismDF = happinessDF.join(SafestCountryDF, col("Country or region") == col("country_txt"), "inner").select("Overall rank", "Country or region", "GDP per capita", "Perceptions of corruption", "totalEvents")
corruptionTerrorismDF.orderBy(col("Perceptions of corruption").asc()).show(10)
corruptionTerrorismDF.orderBy(col("Perceptions of corruption").desc()).show(10)

"""Is GDP per capita correlated with terrorism? Overall, countries with higher GDP per capita tend to have less terrorism cases (except some countries like USA)."""

GDPTerrorismDF = corruptionTerrorismDF.drop("Perceptions of corruption").orderBy(col("GDP per capita").desc())
GDPTerrorismDF.show(15)

"""However, if we look at the countries with the least cases, we see a mix of high income and low income countries. In low income countries, social unrest may focus more on basic survival and needs, while wealthier countries often experience more political or ideological violence due to stronger institutions and more divided politics.
"""

GDPTerrorismDF.orderBy("totalEvents").show(15)

"""Upper/lower middle income countries have the most cases of terrorism.They often face significant challenges such as political instability, economic inequality, and weak institutions."""

IncomeGroupTerrorDP = GDPTerrorismDF.join(countryDF, col("Country or region") == col("ShortName"), "inner").select("Overall rank", "Country or region", "GDP per capita", "totalEvents", "IncomeGroup")
IncomeGroupTerrorDP.orderBy(col("totalEvents").desc()).show(n=10, truncate=False)
IncomeGroupTerrorDP.orderBy(col("totalEvents")).show(n=10, truncate=False)

"""Correlation happiness, HDI and terrorism: Hapiness and HDI is highly related."""

joinedDF = happinessTerrorismDF.join(indicator2019DF, col("Country or region") == col("Country"), "inner").drop("Country").withColumnRenamed("Overall rank", "Happiness rank").withColumnRenamed("2019", "HDI_2019").orderBy("Happiness rank")
joinedDF.show(20)

joinedDF.orderBy(col("HDI Rank")).show(10)
joinedDF.orderBy(col("HDI Rank").desc()).show(10)

"""Stats: average Happiness score and HDI.
We establish a constant (threshold) for both indexes based on:
*   HDI = "The cutoff-points are HDI of less than 0.550 for low human development, 0.550–0.699 for medium human development, 0.700–0.799 for high human development and 0.800 or greater for very high human development."
*   Happiness =  score above 5 can be considered neutral or happy
"""

StatsDF = joinedDF.select(count("*").alias("count"),
                          lit(5).alias("Score_threshold"),
                          lit(0.550).alias("HDI_threshold"),
												 mean("Score").alias("Score_mean"),
                          mean("HDI_2019").alias("HDI_mean"))
StatsDF.show()

avgHappinessDF = joinedDF.withColumn("Happier than average", col("Score")>=5)
avgHappinessDF.orderBy(col("totalEvents").desc()).show(10)
avgHappinessDF.orderBy(col("totalEvents").asc()).show(10)

avgHDI = joinedDF.withColumn("More developed than average", col("HDI_2019") >= 0.55)
avgHDI.orderBy(col("totalEvents").desc()).show(10)
avgHDI.orderBy(col("totalEvents").asc()).show(10)