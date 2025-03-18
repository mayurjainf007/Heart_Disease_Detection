from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier

# Initialize Spark Session
spark = SparkSession.builder.appName("HeartDiseaseProcessing").getOrCreate()

# Load Data
df = spark.read.csv("heart_disease_data.csv", header=True, inferSchema=True)

# Convert DataFrame to ML format
feature_columns = df.columns[:-1]  # Exclude target column
assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
df = assembler.transform(df).select("features", "target")

# Train Model
train, test = df.randomSplit([0.8, 0.2], seed=42)
rf = RandomForestClassifier(labelCol="target", featuresCol="features", numTrees=100)
model = rf.fit(train)

# Evaluate Model
predictions = model.transform(test)
predictions.select("target", "prediction").show(10)

# Save Model
model.save("spark_heart_disease_model")
