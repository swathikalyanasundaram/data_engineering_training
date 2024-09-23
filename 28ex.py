import pandas as pd

# Creating a new dataset
data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Rajesh", "Meena", "Suresh", "Anita", "Vijay", "Neeta"],
    "Department": ["HR", "IT", "Finance", "IT", "Finance", "HR"],
    "Age": [29, 35, 45, 32, 50, 28],
    "Salary": [70000, 85000, 95000, 64000, 120000, 72000],
    "City": ["Delhi", "Mumbai", "Bangalore", "Chennai", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
print(df)


# Exercise 1: Rename Columns
# Rename the "Salary" column to "Annual Salary" and "City" to "Location".
# Print the updated DataFrame.

df.rename(columns={"Salary":"Annual Salary","City":"Location"},inplace=True)
print(df)

# Exercise 2: Drop Columns
# Drop the "Location" column from the DataFrame.
# Print the DataFrame after dropping the column.
drop_column=df.drop(columns=["Location"])
print(drop_column)

# Exercise 3: Drop Rows
# Drop the row where "Name" is "Suresh".
# Print the updated DataFrame.
drop2=drop_column[drop_column["Name"]!="Suresh"]
print(drop2)

# Exercise 4: Handle Missing Data
# Assign None to the "Salary" of "Meena".
# Fill the missing "Salary" value with the mean salary of the existing employees.
# Print the cleaned DataFrame.
df.loc[df["Name"]=="Meena","Annual Salary"]=None
mean_salary=df["Annual Salary"].mean()
df["Annual Salary"]=df["Annual Salary"].fillna(mean_salary)
print(df)

#
# Exercise 5: Create Conditional Columns
# Create a new column "Seniority" that assigns "Senior" to employees aged 40 or above and "Junior" to employees younger than 40.
# Print the updated DataFrame.
df["Seniority"]=df["Age"].apply(lambda age:"Senior" if age >= 40 else "Junior")
print(df)

# Exercise 6: Grouping and Aggregation
# Group the DataFrame by "Department" and calculate the average salary in each department.
# Print the grouped DataFrame.

Avg_salary=df.groupby("Department")["Annual Salary"].mean().reset_index()
print(Avg_salary)