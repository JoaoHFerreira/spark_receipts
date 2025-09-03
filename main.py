from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, avg, count, round

spark = (
    SparkSession.builder
    .appName("CSV Reader")
    .config("spark.driver.bindAddress", "127.0.0.1")  
    .getOrCreate()
)

df = spark.read.csv("/Users/joao-henrique.ferreira/personal_repos/journal/sandbox_pyspark/train_and_test2.csv", header=True, inferSchema=True)




df = df.withColumnRenamed("2urvived", "Survived")


df = df.withColumn(
    "age_group",
    when(col("Age") >= 50, "Senior")
    .when(col("Age") >= 18, "Adult")
    .otherwise("Child")
)


df_filtered = df.filter(col("Fare") > 0)


df_agg = (
    df_filtered.groupBy("Sex", "Pclass", "age_group")
    .agg(
        round(avg("Survived"), 2).alias("avg_survival_rate"),
        count("*").alias("num_passengers"),
        round(avg("Fare"), 2).alias("avg_fare")
    )
)


df_result = df_agg.orderBy(col("Pclass"), col("avg_survival_rate").desc())


df_result.show(truncate=False)