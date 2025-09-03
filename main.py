from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, avg, count, round

spark = (
    SparkSession.builder
    .appName("CSV Reader")
    .config("spark.driver.bindAddress", "127.0.0.1")  # explicitly bind to localhost
    .getOrCreate()
)

df = spark.read.csv("/Users/joao-henrique.ferreira/personal_repos/journal/sandbox_pyspark/train_and_test2.csv", header=True, inferSchema=True)



# Renomear coluna '2urvived' para 'Survived' para facilitar
df = df.withColumnRenamed("2urvived", "Survived")

# Criar coluna "age_group"
df = df.withColumn(
    "age_group",
    when(col("Age") >= 50, "Senior")
    .when(col("Age") >= 18, "Adult")
    .otherwise("Child")
)

# Filtrar passageiros com tarifa paga maior que zero
df_filtered = df.filter(col("Fare") > 0)

# Agregar: taxa de sobrevivência média e contagem por sexo e classe
df_agg = (
    df_filtered.groupBy("Sex", "Pclass", "age_group")
    .agg(
        round(avg("Survived"), 2).alias("avg_survival_rate"),
        count("*").alias("num_passengers"),
        round(avg("Fare"), 2).alias("avg_fare")
    )
)

# Ordenar por classe e taxa de sobrevivência
df_result = df_agg.orderBy(col("Pclass"), col("avg_survival_rate").desc())

# Mostrar resultado
df_result.show(truncate=False)