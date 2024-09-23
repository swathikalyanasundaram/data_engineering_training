# -*- coding: utf-8 -*-
"""start.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i4B7mWlY8BDFfJZH7PZqP8W_3pz7fRkm
"""

! pip install pyspark

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("Advanced DataFrame Operations - Different Dataset") \
    .getOrCreate()

# Create two sample DataFrames for Product Sales
data1 = [
    (1, 'Product A', 'Electronics', 1200, '2022-05-10'),
    (2, 'Product B', 'Clothing', 500, '2022-07-15'),
    (3, 'Product C', 'Electronics', 1800, '2021-11-05')
]

data2 = [
    (4, 'Product D', 'Furniture', 3000, '2022-03-25'),
    (5, 'Product E', 'Clothing', 800, '2022-09-12'),
    (6, 'Product F', 'Electronics', 1500, '2021-10-19')
]

# Define schema (columns)
columns = ['ProductID', 'ProductName', 'Category', 'Price', 'SaleDate']

# Create DataFrames
sales_df1 = spark.createDataFrame(data1, columns)
sales_df2 = spark.createDataFrame(data2, columns)

### Tasks:

#1. **Union of DataFrames (removing duplicates)**:
 #  Combine the two DataFrames (`sales_df1` and `sales_df2`) using `union` and remove any duplicate rows.
sales_df_union =sales_df1.union(sales_df2).distinct()
sales_df_union.show()


# 2. **Union of DataFrames (including duplicates)**:
  #  Combine both DataFrames using `unionAll` (replaced by `union`) and include duplicate rows.
sales_df_unionall=sales_df1.unionAll(sales_df2)
sales_df_unionall.show()


# 3. **Rank products by price within their category**:
  #  Use window functions to rank the products in each category by price in descending order.
window_func=Window.partitionBy("Category").orderBy(F.col("Price").desc())
sales_df_rank=sales_df_unionall.withColumn("Rank", F.rank().over(window_func))
sales_df_rank.show()


# 4. **Calculate cumulative price per category**:
  #  Use window functions to calculate the cumulative price of products within each category.
sales_df_rank.withColumn("cumulativePrice",F.sum("Price").over(window_func))
sales_df_rank

# 5. **Convert `SaleDate` from string to date type**:
  #  Convert the `SaleDate` column from string format to a PySpark date type.
sales_df_date=sales_df_rank.withColumn("SaleDate",F.to_date(F.col("SaleDate"),"yyyy-MM-dd"))
sales_df_date.show()

# 6. **Calculate the number of days since each sale**:
  #  Calculate the number of days since each product was sold using the current date.
sales_df_since=sales_df_date.withColumn("DaySinceSale",F.datediff(F.current_date(),F.col("SaleDate")))
sales_df_since.show()

# 7. **Add a column for the next sale deadline**:
  #  Add a new column `NextSaleDeadline`, which should be 30 days after the `SaleDate`.
sales_df_deadline=sales_df_since.withColumn("NextSaleDeadline",F.expr("date_add(SaleDate,30)"))
sales_df_deadline.show()

# 8. **Calculate total revenue and average price per category**:
  #  Find the total revenue (sum of prices) and the average price per category.
sales_tot=sales_df_deadline.groupBy("Category").agg(F.sum("Price").alias("TotalRevenue"),F.avg("Price").alias("AveragePrice"))
sales_tot.show()

# 9. **Convert all product names to lowercase**:
  #  Create a new column with all product names in lowercase.
sales_lower=sales_df_deadline.withColumn("ProductNameLower",F.lower(F.col("ProductName")))
sales_lower.show()