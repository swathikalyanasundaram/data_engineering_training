# -*- coding: utf-8 -*-
"""pyspark_ex.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FGI5iBHDTIUoXhC0OPyNQgjy7kWggyBp
"""

! pip install pyspark

from pyspark.sql import SparkSession

spark= SparkSession.builder \
  .appName("FitnessTrackerAnalysis") \
  .getOrCreate()

#Sample Data
data = [
    (1, "2023-07-01", 12000, 500, 8.5, 90),
    (2, "2023-07-01", 8000, 350, 5.6, 60),
    (3, "2023-07-01", 15000, 600, 10.2, 120),
    (1, "2023-07-02", 11000, 480, 7.9, 85),
    (2, "2023-07-02", 9000, 400, 6.2, 70),
    (3, "2023-07-02", 13000, 520, 9.0, 100),
    (1, "2023-07-03", 10000, 450, 7.1, 80),
    (2, "2023-07-03", 7000, 320, 4.9, 55),
    (3, "2023-07-03", 16000, 620, 11.0, 130)
]

columns=["user_id","date","steps","calories","distance_km","active_minutes"]

df=spark.createDataFrame(data,columns)
df.show()

from pyspark.sql.functions import col,sum,avg,max
from pyspark.sql.window import Window

# 1. Total Steps Taken by Each User
total_steps_per_user= df.groupby("user_id").agg(sum("steps").alias("total_steps"))
total_steps_per_user.show()

# 2. Filter Days Where a User Burned More Than 500 Calories
days_over_500_calories = df.filter(col("calories") > 500)
days_over_500_calories.show()

# 3. Average Distance Traveled by Each User
average_distance_per_user = df.groupBy("user_id").agg(avg("distance_km").alias("average_distance"))
average_distance_per_user.show()

# 4. Day with Maximum Steps for Each User
max_steps_per_user = df.withColumn("max_steps",max("steps").over(Window.partitionBy("user_id"))) \
                       .filter(col("steps") == col("max_steps"))
max_steps_per_user.show()

# 5. Users Who Were Active for More Than 100 Minutes on Any Day
active_over_100_minutes = df.filter(col("active_minutes") > 100).select("user_id").distinct()
active_over_100_minutes.show()

# 6. Total Calories Burned per Day
total_calories_per_day = df.groupBy("date").agg(sum("calories").alias("total_calories"))
total_calories_per_day.show()

# 7. Average Steps per Day Across All Users
average_steps_per_day = df.groupBy("date").agg(avg("steps").alias("average_steps"))
average_steps_per_day.show()

# 8. Rank Users by Total Distance Traveled
total_distance_per_user = df.groupBy("user_id").agg(sum("distance_km").alias("total_distance"))
distance_ranking = total_distance_per_user.orderBy(col("total_distance").desc())
distance_ranking.show()

# 9. Most Active User by Total Active Minutes
most_active_user = df.groupBy("user_id").agg(sum("active_minutes").alias("total_active_minutes")) \
                    .orderBy(col("total_active_minutes").desc()).limit(1)
most_active_user.show()

# 10. Create New Column for Calories Burned per Kilometer
df_with_calories_per_km = df.withColumn("calories_per_km", col("calories") / col("distance_km"))
df_with_calories_per_km.show()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, max, countDistinct

# Initialize Spark session
spark = SparkSession.builder.appName("BookSalesAnalysis").getOrCreate()

# Sample Data
data = [
    (1, "The Catcher in the Rye", "J.D. Salinger", "Fiction", 15.99, 2, "2023-01-05"),
    (2, "To Kill a Mockingbird", "Harper Lee", "Fiction", 18.99, 1, "2023-01-10"),
    (3, "Becoming", "Michelle Obama", "Biography", 20.00, 3, "2023-02-12"),
    (4, "Sapiens", "Yuval Noah Harari", "Non-Fiction", 22.50, 1, "2023-02-15"),
    (5, "Educated", "Tara Westover", "Biography", 17.99, 2, "2023-03-10"),
    (6, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 10.99, 5, "2023-03-15"),
    (7, "Atomic Habits", "James Clear", "Self-Help", 16.99, 3, "2023-04-01"),
    (8, "Dune", "Frank Herbert", "Science Fiction", 25.99, 1, "2023-04-10"),
    (9, "1984", "George Orwell", "Fiction", 14.99, 2, "2023-04-12"),
    (10, "The Power of Habit", "Charles Duhigg", "Self-Help", 18.00, 1, "2023-05-01")
]

# Column names
columns = ["sale_id", "book_title", "author", "genre", "sale_price", "quantity", "date"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# 1. Total Sales Revenue per Genre
df = df.withColumn("total_sales", col("sale_price") * col("quantity"))
total_sales_per_genre = df.groupBy("genre").agg(sum("total_sales").alias("total_sales"))
total_sales_per_genre.show()

# 2. Filter Books Sold in the "Fiction" Genre
fiction_books = df.filter(col("genre") == "Fiction")
fiction_books.show()

# 3. Find the Book with the Highest Sale Price
highest_sale_price = df.orderBy(col("sale_price").desc()).limit(1)
highest_sale_price.show()

# 4. Calculate Total Quantity of Books Sold by Author
total_quantity_per_author = df.groupBy("author").agg(sum("quantity").alias("total_quantity"))
total_quantity_per_author.show()

# 5. Identify Sales Transactions Worth More Than $50
sales_over_50 = df.filter(col("total_sales") > 50)
sales_over_50.show()

# 6. Find the Average Sale Price per Genre
avg_sale_price_per_genre = df.groupBy("genre").agg(avg("sale_price").alias("average_sale_price"))
avg_sale_price_per_genre.show()

# 7. Count the Number of Unique Authors in the Dataset
unique_authors = df.select(countDistinct("author").alias("unique_authors"))
unique_authors.show()

# 8. Find the Top 3 Best-Selling Books by Quantity
top_3_books_by_quantity = df.groupBy("book_title").agg(sum("quantity").alias("total_quantity")).orderBy(col("total_quantity").desc()).limit(3)
top_3_books_by_quantity.show()

# 9. Calculate Total Sales for Each Month
from pyspark.sql.functions import month

df = df.withColumn("month", month(col("date")))
total_sales_per_month = df.groupBy("month").agg(sum("total_sales").alias("total_sales"))
total_sales_per_month.show()

# 10. Create a New Column for Total Sales Amount
df_with_total_sales = df.withColumn("total_sales", col("sale_price") * col("quantity"))
df_with_total_sales.show()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, max, countDistinct

# Initialize Spark session
spark = SparkSession.builder.appName("FoodDeliveryAnalysis").getOrCreate()

# Sample Data
data = [
    (1, 201, "McDonald's", "Burger", 2, 5.99, 30, "2023-06-15"),
    (2, 202, "Pizza Hut", "Pizza", 1, 12.99, 45, "2023-06-16"),
    (3, 203, "KFC", "Fried Chicken", 3, 8.99, 25, "2023-06-17"),
    (4, 201, "Subway", "Sandwich", 2, 6.50, 20, "2023-06-17"),
    (5, 204, "Domino's", "Pizza", 2, 11.99, 40, "2023-06-18"),
    (6, 205, "Starbucks", "Coffee", 1, 4.50, 15, "2023-06-18"),
    (7, 202, "KFC", "Fried Chicken", 1, 8.99, 25, "2023-06-19"),
    (8, 206, "McDonald's", "Fries", 3, 2.99, 15, "2023-06-19"),
    (9, 207, "Burger King", "Burger", 1, 6.99, 30, "2023-06-20"),
    (10, 203, "Starbucks", "Coffee", 2, 4.50, 20, "2023-06-20")
]

# Column names
columns = ["order_id", "customer_id", "restaurant_name", "food_item", "quantity", "price", "delivery_time_mins", "order_date"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# 1. Calculate Total Revenue per Restaurant
df = df.withColumn("total_revenue", col("price") * col("quantity"))
total_revenue_per_restaurant = df.groupBy("restaurant_name").agg(sum("total_revenue").alias("total_revenue"))
total_revenue_per_restaurant.show()

# 2. Find the Fastest Delivery
fastest_delivery = df.orderBy(col("delivery_time_mins")).limit(1)
fastest_delivery.show()

# 3. Calculate Average Delivery Time per Restaurant
avg_delivery_time_per_restaurant = df.groupBy("restaurant_name").agg(avg("delivery_time_mins").alias("average_delivery_time"))
avg_delivery_time_per_restaurant.show()

# 4. Filter Orders for a Specific Customer (e.g., customer_id = 201)
orders_for_customer_201 = df.filter(col("customer_id") == 201)
orders_for_customer_201.show()

# 5. Find Orders Where Total Amount Spent is Greater Than $20
orders_over_20 = df.filter((col("price") * col("quantity")) > 20)
orders_over_20.show()

# 6. Calculate the Total Quantity of Each Food Item Sold
total_quantity_per_food_item = df.groupBy("food_item").agg(sum("quantity").alias("total_quantity_sold"))
total_quantity_per_food_item.show()

# 7. Find the Top 3 Most Popular Restaurants by Number of Orders
top_3_restaurants_by_orders = df.groupBy("restaurant_name").count().orderBy(col("count").desc()).limit(3)
top_3_restaurants_by_orders.show()

# 8. Calculate Total Revenue per Day
total_revenue_per_day = df.groupBy("order_date").agg(sum("total_revenue").alias("total_revenue"))
total_revenue_per_day.show()

# 9. Find the Longest Delivery Time for Each Restaurant
longest_delivery_time_per_restaurant = df.groupBy("restaurant_name").agg(max("delivery_time_mins").alias("longest_delivery_time"))
longest_delivery_time_per_restaurant.show()

# 10. Create a New Column for Total Order Value
df_with_total_order_value = df.withColumn("total_order_value", col("price") * col("quantity"))
df_with_total_order_value.show()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, min , max

# Initialize Spark session
spark = SparkSession.builder.appName("WeatherDataAnalysis").getOrCreate()

# Sample Data
data = [
    ("2023-01-01", "New York", 5, 60, 20, "Cloudy"),
    ("2023-01-01", "Los Angeles", 15, 40, 10, "Sunny"),
    ("2023-01-01", "Chicago", -2, 75, 25, "Snow"),
    ("2023-01-02", "New York", 3, 65, 15, "Rain"),
    ("2023-01-02", "Los Angeles", 18, 35, 8, "Sunny"),
    ("2023-01-02", "Chicago", -5, 80, 30, "Snow"),
    ("2023-01-03", "New York", 6, 55, 22, "Sunny"),
    ("2023-01-03", "Los Angeles", 20, 38, 12, "Sunny"),
    ("2023-01-03", "Chicago", -1, 70, 18, "Cloudy")
]

# Column names
columns = ["date", "city", "temperature_c", "humidity", "wind_speed_kph", "condition"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# 1. Find the Average Temperature for Each City
avg_temp_per_city = df.groupBy("city").agg(avg("temperature_c").alias("average_temperature"))
avg_temp_per_city.show()

# 2. Filter Days with Temperature Below Freezing
below_freezing_days = df.filter(col("temperature_c") < 0)
below_freezing_days.show()

# 3. Find the City with the Highest Wind Speed on a Specific Day (e.g., 2023-01-02)
highest_wind_speed_20230102 = df.filter(col("date") == "2023-01-02").orderBy(col("wind_speed_kph").desc()).limit(1)
highest_wind_speed_20230102.show()

# 4. Calculate the Total Number of Days with Rainy Weather
rainy_days_count = df.filter(col("condition") == "Rain").count()
print(f"Total number of rainy days: {rainy_days_count}")

# 5. Calculate the Average Humidity for Each Weather Condition
avg_humidity_per_condition = df.groupBy("condition").agg(avg("humidity").alias("average_humidity"))
avg_humidity_per_condition.show()

# 6. Find the Hottest Day in Each City
hottest_day_per_city = df.groupBy("city").agg(max("temperature_c").alias("max_temperature"))
hottest_day_per_city.show()

# 7. Identify Cities That Experienced Snow
cities_with_snow = df.filter(col("condition") == "Snow").select("city").distinct()
cities_with_snow.show()

# 8. Calculate the Average Wind Speed for Days When the Condition was Sunny
avg_wind_speed_sunny_days = df.filter(col("condition") == "Sunny").agg(avg("wind_speed_kph").alias("average_wind_speed"))
avg_wind_speed_sunny_days.show()

# 9. Find the Coldest Day Across All Cities
coldest_day_across_cities = df.orderBy(col("temperature_c")).limit(1)
coldest_day_across_cities.show()

# 10. Create a New Column for Wind Chill
df_with_wind_chill = df.withColumn(
    "wind_chill",
    13.12 + (0.6215 * col("temperature_c")) - (11.37 * (col("wind_speed_kph") ** 0.16)) + (0.3965 * col("temperature_c") * (col("wind_speed_kph") ** 0.16))
)
df_with_wind_chill.show()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count

# Initialize Spark session
spark = SparkSession.builder.appName("AirlineFlightDataAnalysis").getOrCreate()

# Sample Data
data = [
    (1, "Delta", "DL123", "JFK", "LAX", "08:00", "11:00", 30, 3970, "2023-07-01"),
    (2, "United", "UA456", "SFO", "ORD", "09:30", "15:00", 45, 2960, "2023-07-01"),
    (3, "Southwest", "SW789", "DAL", "ATL", "06:00", "08:30", 0, 1150, "2023-07-01"),
    (4, "Delta", "DL124", "LAX", "JFK", "12:00", "20:00", 20, 3970, "2023-07-02"),
    (5, "American", "AA101", "MIA", "DEN", "07:00", "10:00", 15, 2770, "2023-07-02"),
    (6, "United", "UA457", "ORD", "SFO", "11:00", "14:30", 0, 2960, "2023-07-02"),
    (7, "JetBlue", "JB302", "BOS", "LAX", "06:30", "09:45", 10, 4180, "2023-07-03")
]

# Column names
columns = ["flight_id", "airline", "flight_number", "origin", "destination", "departure_time", "arrival_time", "delay_minutes", "distance_km", "date"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# 1. Find the Total Distance Traveled by Each Airline
total_distance_by_airline = df.groupBy("airline").agg(sum("distance_km").alias("total_distance"))
total_distance_by_airline.show()

# 2. Filter Flights with Delays Greater than 30 Minutes
delays_greater_than_30 = df.filter(col("delay_minutes") > 30)
delays_greater_than_30.show()

# 3. Find the Flight with the Longest Distance
longest_distance_flight = df.orderBy(col("distance_km").desc()).limit(1)
longest_distance_flight.show()

# 4. Calculate the Average Delay Time for Each Airline
avg_delay_by_airline = df.groupBy("airline").agg(avg("delay_minutes").alias("average_delay"))
avg_delay_by_airline.show()

# 5. Identify Flights That Were Not Delayed
flights_not_delayed = df.filter(col("delay_minutes") == 0)
flights_not_delayed.show()

# 6. Find the Top 3 Most Frequent Routes
top_3_frequent_routes = df.groupBy("origin", "destination").count().orderBy(col("count").desc()).limit(3)
top_3_frequent_routes.show()

# 7. Calculate the Total Number of Flights per Day
total_flights_per_day = df.groupBy("date").agg(count("flight_id").alias("total_flights"))
total_flights_per_day.show()

# 8. Find the Airline with the Most Flights
most_flights_by_airline = df.groupBy("airline").agg(count("flight_id").alias("total_flights")).orderBy(col("total_flights").desc()).limit(1)
most_flights_by_airline.show()

# 9. Calculate the Average Flight Distance per Day
avg_flight_distance_per_day = df.groupBy("date").agg(avg("distance_km").alias("average_distance"))
avg_flight_distance_per_day.show()

# 10. Create a New Column for On-Time Status
df_with_on_time_status = df.withColumn("on_time", col("delay_minutes") == 0)
df_with_on_time_status.show()