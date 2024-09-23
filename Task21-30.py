# 21: Cumulative Sum and Rolling Windows
import pandas as pd
import numpy as np

# Create the DataFrame with random sales data
index = pd.date_range(start='today', periods=30)
df = pd.DataFrame({'Sales': np.random.randint(100, 1000, size=30)}, index=index)

# Calculate cumulative sum
df['Cumulative Sales'] = df['Sales'].cumsum()

# Calculate rolling average over the past 7 days
df['Rolling Avg'] = df['Sales'].rolling(window=7).mean()
print(df)

# 22: String Operations
# Create the DataFrame with names
data = {'Names': ['John Doe', 'Jane Smith', 'Sam Brown']}
df = pd.DataFrame(data)

# Split the "Names" column
df[['First Name', 'Last Name']] = df['Names'].str.split(' ', expand=True)

# Convert "First Name" to uppercase
df['First Name'] = df['First Name'].str.upper()
print(df)

#23: Conditional Selections with np.where
import numpy as np

# Create the DataFrame
data = {'Employee': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 35, 45, 55], 'Department': ['Sales', 'HR', 'IT', 'Finance']}
df = pd.DataFrame(data)

# Create the "Status" column using np.where
df['Status'] = np.where(df['Age'] >= 40, 'Senior', 'Junior')
print(df)

#24:Slicing DataFrames
# Create the DataFrame
data = {'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone'], 'Category': ['Electronics', 'Accessories', 'Electronics', 'Accessories', 'Electronics'], 'Sales': [100000, 50000, 80000, 30000, 120000], 'Profit': [20000, 10000, 15000, 5000, 30000]}
df = pd.DataFrame(data)

# Slice the DataFrame
first_10_rows = df.head(10)
electronics_category = df[df['Category'] == 'Electronics']
high_sales_profit = df[(df['Sales'] > 50000) & (df['Profit'] > 5000)][['Sales', 'Profit']]
print(first_10_rows)
print(electronics_category)
print(high_sales_profit)

#25: Concatenating DataFrames Vertically and Horizontally
# Create the DataFrames
store_a_df = pd.DataFrame({'Employee': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 35, 45], 'Salary': [50000, 60000, 70000]})
store_b_df = pd.DataFrame({'Employee': ['David', 'Emily', 'Frank'], 'Age': [55, 30, 40], 'Salary': [80000, 55000, 65000]})

# Concatenate vertically
combined_df_vertical = pd.concat([store_a_df, store_b_df], ignore_index=True)

# Concatenate horizontally
combined_df_horizontal = pd.concat([store_a_df, store_b_df], axis=1)
print(combined_df_vertical)
print(combined_df_horizontal)

#26: Exploding Lists in DataFrame Columns
# Create the DataFrame
data = {'Product': ['Laptop', 'Mouse', 'Monitor'], 'Features': [['Feature1', 'Feature2'], ['Feature3', 'Feature4'], ['Feature5']]}
df = pd.DataFrame(data)

# Explode the "Features" column
exploded_df = df.explode('Features')
print(exploded_df)

# 27: Using .map() and .applymap()
import pandas as pd

df = pd.DataFrame({
    "Product": ["A", "B", "C"],
    "Price": [100, 200, 300],
    "Quantity": [10, 20, 30]  # Added a "Quantity" column for completeness
})

# Increase price by 10% using map
df["Price"] = df["Price"].map(lambda x: x * 1.1)

# Format numeric values to two decimal places using map
df = df.apply(lambda x: ["{:.2f}".format(i) if isinstance(i, float) else i for i in x])

print(df)

#28: Combining groupby() with apply()
import pandas as pd

# Create the DataFrame
data = {'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles'], 'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone'], 'Sales': [100000, 50000, 80000, 30000, 120000], 'Profit': [20000, 10000, 15000, 5000, 30000]}
df = pd.DataFrame(data)

# Group by "City" and calculate profit margin (avoiding deprecated apply)
def calculate_profit_margin(group):
    return group['Profit'].sum() / group['Sales'].sum()

# Use groupby with select columns and apply the function
grouped_df = df.groupby('City')[['Profit', 'Sales']].apply(calculate_profit_margin)
print(grouped_df)

# 29:Creating a DataFrame from Multiple Sources
df_csv = pd.read_csv("data1.csv")
df_json = pd.read_json("data2.json")
data3 = {
    "ID": [1, 2, 3],
    "Name": ["John", "Anna", "Peter"]
}
df_dict = pd.DataFrame(data3)
df_consolidated = pd.merge(df_csv, df_json, on="ID")
df_consolidated = pd.merge(df_consolidated, df_dict, on="ID")
print(df_consolidated)

### *Exercise 30: Dealing with Large Datasets*
# 1. Create a large DataFrame with 1 million rows, representing data on "Transaction ID", "Customer", "Product", "Amount", and "Date".
# 2. Split the DataFrame into smaller chunks (e.g., 100,000 rows each), perform a simple analysis on each chunk (e.g., total sales), and combine the results.

df = pd.DataFrame({
    "Amount": np.random.randint(1, 100, 1000000)
})
chunk_size = 100000
total_sales = sum(chunk["Amount"].sum() for chunk in [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)])
print("Total Sales:", total_sales)