#11: Pivot Tables
import pandas as pd

# Create the DataFrame
data = {
    "Product": ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone'],
    "Category": ['Electronics', 'Accessories', 'Electronics', 'Accessories', 'Electronics'],
    "Quantity": [10, 100, 50, 75, 30]
}

df = pd.DataFrame(data)

# Create the pivot table
pivot_df = df.pivot_table(index=['Category', 'Product'], values='Quantity', aggfunc='sum')
print(pivot_df)

#12:Concatenating DataFrames
# Create two separate DataFrames
store1_df = pd.DataFrame({'Product': ['Laptop', 'Mouse', 'Monitor'], 'Price': [80000, 1500, 20000], 'Quantity': [10, 100, 50]})
store2_df = pd.DataFrame({'Product': ['Keyboard', 'Phone', 'Headphones'], 'Price': [3000, 40000, 500], 'Quantity': [75, 30, 20]})

# Concatenate the DataFrames
combined_df = pd.concat([store1_df, store2_df], ignore_index=True)
print(combined_df)

#13:Working with Dates
import pandas as pd
import numpy as np

# Create the DataFrame with dates
end_date = pd.to_datetime('today')
start_date = end_date - pd.to_timedelta('5 days')
date_range = pd.date_range(start=start_date, end=end_date)
df = pd.DataFrame({'Date': date_range})

# Add random sales data
df['Sales'] = np.random.randint(100, 1000, size=len(df))

# Calculate total sales
total_sales = df['Sales'].sum()
print(total_sales)

#14:Reshaping Data with Melt
# Create the DataFrame
data = {
    "Product": ['Laptop', 'Mouse', 'Monitor'],
    "Region": ['North', 'South', 'East'],
    "Q1_Sales": [1000, 500, 800],
    "Q2_Sales": [1200, 600, 900]
}

df = pd.DataFrame(data)

# Melt the DataFrame
melted_df = df.melt(id_vars=['Product', 'Region'], var_name='Quarter', value_name='Sales')
print(melted_df)

#15:Reading and Writing Data
# Read the data from CSV
df = pd.read_csv('products.csv')

# Perform operations (e.g., add a new column)
df['Total Value'] = df['Price'] * df['Quantity']

# Write the DataFrame to a new CSV
df.to_csv('updated_products.csv', index=False)



#16:Renaming Columns
# Create the DataFrame
data = {
    "Prod": ['Laptop', 'Mouse', 'Monitor'],
    "Cat": ['Electronics', 'Accessories', 'Electronics'],
    "Price": [80000, 1500, 20000],
    "Qty": [10, 100, 50]
}

df = pd.DataFrame(data)

# Rename the columns
df = df.rename(columns={'Prod': 'Product', 'Cat': 'Category', 'Qty': 'Quantity'})
print(df)

#17:Creating a MultiIndex DataFrame
# Create the MultiIndex DataFrame
index = pd.MultiIndex.from_product([['Store A', 'Store B'], ['Laptop', 'Mouse', 'Monitor']], names=['Store', 'Product'])
data = np.random.randint(100, 1000, (6, 2))
df = pd.DataFrame(data, index=index, columns=['Price', 'Quantity'])
print(df)

#18:Resample Time-Series Data
import pandas as pd
import numpy as np

# Create the DataFrame with dates
end_date = pd.to_datetime('today')
start_date = end_date - pd.to_timedelta('30 days')
date_range = pd.date_range(start=start_date, end=end_date)
df = pd.DataFrame({'Date': date_range})

# Add random sales data
df['Sales'] = np.random.randint(100, 1000, size=len(df))

# Resample the data by week
df.set_index('Date', inplace=True)
df_resampled = df.resample('W').sum()
print(df_resampled)

#19: Handling Duplicates
# Create the DataFrame with duplicates
data = {
    "Product": ['Laptop', 'Mouse', 'Monitor', 'Laptop'],
    "Price": [80000, 1500, 20000, 80000],
    "Quantity": [10, 100, 50, 10]
}

df = pd.DataFrame(data)

# Remove duplicates
df = df.drop_duplicates()
print(df)

#20:import pandas as pd
import numpy as np

# Create the DataFrame with numeric data
np.random.seed(42)
data = {
    "Height": np.random.randint(150, 190, 100),
    "Weight": np.random.randint(50, 100, 100),
    "Age": np.random.randint(20, 50, 100),
    "Income": np.random.randint(30000, 100000, 100)
}

df = pd.DataFrame(data)

# Compute the correlation matrix
correlation_matrix = df.corr()
print(correlation_matrix)

