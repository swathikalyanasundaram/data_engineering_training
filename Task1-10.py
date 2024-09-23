#1: Creating DataFrame from Scratch
import pandas as pd

data = {
    "Product": ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone'],
    "Category": ['Electronics', 'Accessories', 'Electronics', 'Accessories', 'Electronics'],
    "Price": [80000, 1500, 20000, 3000, 40000],
    "Quantity": [10, 100, 50, 75, 30]
}

df = pd.DataFrame(data)
print(df)

# # 2: Basic DataFrame Operations
# # Display the first 3 rows
# print(df.head(3))

# # Display column names and index
# print(df.columns)
# print(df.index)

# # Display summary statistics
# print(df.describe())

# #3: Selecting Data
# # Select "Product" and "Price" columns
# selected_df = df[['Product', 'Price']]
# print(selected_df)

# # Select rows where "Category" is "Electronics"
# electronics_df = df[df['Category'] == 'Electronics']
# print(electronics_df)

# #4: Filtering Data
# # Filter products with price greater than 10,000
# filtered_df1 = df[df['Price'] > 10000]
# print(filtered_df1)

# # Filter products with "Accessories" category and quantity greater than 50
# filtered_df2 = df[(df['Category'] == 'Accessories') & (df['Quantity'] > 50)]
# print(filtered_df2)

# #5.Adding and Removing Columns
# # Add "Total Value" column
# df['Total Value'] = df['Price'] * df['Quantity']

# # Drop "Category" column
# df = df.drop(columns=['Category'])
# print(df)

# #6: Sorting Data
# # Sort by "Price" in descending order
# df_sorted_price = df.sort_values('Price', ascending=False)
# print(df_sorted_price)

# # Sort by "Quantity" in ascending order, then by "Price" in descending order
# df_sorted_multi = df.sort_values(['Quantity', 'Price'], ascending=[True, False])
# print(df_sorted_multi)

# # 7: Grouping Data
# #  Group the DataFrame by "Category" and calculate the total quantity for each category.
# df_grouped = df.groupby("Category")["Quantity"].sum()
# print(df_grouped)
# #  Group by "Category" and calculate the average price for each category.
# df_grouped = df.groupby("Category")["Quantity"].mean()
# print(df_grouped)

# #8: Handling Missing Data
# # Introduce missing values
# df.loc[1, 'Price'] = None
# df.loc[3, 'Price'] = None

# # Fill missing values with mean price
# df['Price'] = df['Price'].fillna(df['Price'].mean())

# Drop rows with "Quantity" less than 50
df = df[df['Quantity'] >= 50]
print(df)

# #9:Apply Custom Functions
# # Increase prices by 5%
# def increase_price(price):
#     return price * 1.05

# df['Price'] = df['Price'].apply(increase_price)

# # Create "Discounted Price" column
# df['Discounted Price'] = df['Price'] * 0.9
# print(df)

# #10:Merging DataFrames
# # Create another DataFrame
# supplier_df = pd.DataFrame({'Product': ['Laptop', 'Mouse', 'Monitor'], 'Supplier': ['Supplier A', 'Supplier B', 'Supplier C']})

# # Merge DataFrames
# merged_df = pd.merge(df, supplier_df, on='Product')
# print(merged_df)



