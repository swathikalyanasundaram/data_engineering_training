# Databricks notebook source
# MAGIC %md
# MAGIC 1. Create Delta Tables Using 3 Methods

# COMMAND ----------

dbutils.fs.cp("file:/Workspace/Shared/sales_dataa.csv","dbfs:/FileStore/sales_dataa.csv")

sales_df=spark.read.format("csv").option("header","true").load("/FileStore/sales_dataa.csv")
sales_df.show()


# COMMAND ----------

#DataFrame as a Delta Table
sales_df.write.format("delta").mode("overwrite").save("/delta/sales_dataa_delta")

# Load and verify the Delta table
sales_df = spark.read.format("delta").load("/delta/sales_dataa_delta")
sales_df.show()


# COMMAND ----------

#Load the customer_data.json file into a DataFrame.

dbutils.fs.cp("file:/Workspace/Shared/cust_data.json", "dbfs:/FileStore/cust_data.json")

# Load customer data from JSON
customer_df = spark.read.option("multiline", "true").json("/FileStore/cust_data.json")

# Display customer data
customer_df.show()


# COMMAND ----------

#Cust table as a delta table
# Write customer data as a Delta table
customer_df.write.format("delta").mode("overwrite").save("/delta/customer_data_delta")

customer_delta_df = spark.read.format("delta").load("/delta/customer_data_delta")
customer_delta_df.show()



# COMMAND ----------

# MAGIC %md
# MAGIC 2. Data Management

# COMMAND ----------

dbutils.fs.cp("file:/Workspace/Shared/new_sales_data.csv", "dbfs:/FileStore/new_sales_data.csv")
# Load new sales data into DataFrame
new_sales_df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/FileStore/new_sales_data.csv")
new_sales_df.show()


# COMMAND ----------

#Perform the MERGE INTO Operation
from delta.tables import DeltaTable

# Load the existing Delta table
delta_table = DeltaTable.forPath(spark, "/delta/sales_dataa_delta")

# Perform the MERGE INTO operation
delta_table.alias("sales") \
    .merge(
        new_sales_df.alias("new_sales"),
        "sales.OrderID = new_sales.OrderID"  # Merge condition based on OrderID
    ) \
    .whenMatchedUpdateAll() \
    .whenNotMatchedInsertAll() \
    .execute()
updated_sales_delta_df = spark.read.format("delta").load("/delta/sales_dataa_delta")
updated_sales_delta_df.show()


# COMMAND ----------

# MAGIC %md
# MAGIC 3. Optimize Delta Table

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE delta.`/delta/sales_dataa_delta` ZORDER BY (CustomerID)
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC 4. Advanced Features
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY delta.`/delta/sales_dataa_delta`
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM delta.`/delta/sales_dataa_delta` RETAIN 168 HOURS
# MAGIC
# MAGIC

# COMMAND ----------

spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "false")


# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM delta.`/delta/sales_dataa_delta` RETAIN 0 HOURS
# MAGIC

# COMMAND ----------

spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "true")


# COMMAND ----------

# MAGIC %md
# MAGIC 5. Hands-on Exercises

# COMMAND ----------

# Query a historical version of the Delta table
historical_sales_df = spark.read.format("delta").option("versionAsOf", 2).load("/delta/sales_dataa_delta")
historical_sales_df.show()


# COMMAND ----------

from delta.tables import DeltaTable

# Path to the existing Delta table
delta_table_path = "/delta/sales_dataa_delta"

# Load the existing Delta table
delta_table = DeltaTable.forPath(spark, delta_table_path)

# Load the new sales data into a DataFrame
new_sales_df = spark.read.format("csv").option("header", "true").load("/FileStore/new_sales_data.csv")

# Perform the MERGE operation
(delta_table.alias("sales")
    .merge(
        new_sales_df.alias("new_sales"),
        "sales.OrderID = new_sales.OrderID"
    )
    .whenMatchedUpdateAll()
    .whenNotMatchedInsertAll()
    .execute()
)




# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE delta.`/delta/sales_dataa_delta` ZORDER BY (CustomerID);
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "false")

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM delta.`/delta/sales_dataa_delta` RETAIN 0 HOURS;
