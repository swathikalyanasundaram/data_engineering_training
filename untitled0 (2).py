# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i4B7mWlY8BDFfJZH7PZqP8W_3pz7fRkm
"""

! pip install pyspark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("Employee Data Analysis") \
    .getOrCreate()

# Sample employee data
data = [
    (1, 'Arjun', 'IT', 75000),
    (2, 'Vijay', 'Finance', 85000),
    (3, 'Shalini', 'IT', 90000),
    (4, 'Sneha', 'HR', 50000),
    (5, 'Rahul', 'Finance', 60000),
    (6, 'Amit', 'IT', 55000)
]

# Define schema (columns)
columns = ['EmployeeID', 'EmployeeName', 'Department', 'Salary']

# Create DataFrame
employee_df = spark.createDataFrame(data, columns)

# Task 1: Filter Employees by Salary
filtered_df = employee_df.filter(col('Salary') > 60000)
filtered_df.show()

# Task 2: Calculate the Average Salary by Department
average_salary_df = employee_df.groupBy('Department').agg(avg('Salary').alias('AverageSalary'))
average_salary_df.show()

# Task 3: Sort Employees by Salary
sorted_df = employee_df.orderBy(col('Salary').desc())
sorted_df.show()

# Task 4: Add a Bonus Column
employee_df_with_bonus = employee_df.withColumn('Bonus', col('Salary') * 0.10)
employee_df_with_bonus.show()