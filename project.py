import pandas as pd

# Set pandas options to display all columns
pd.set_option('display.max_columns', None)

# 1. Data Collection: Load energy data from a CSV file
energy_data = pd.read_csv('energy_data.csv')

# 2. Data Preprocessing: Handle missing values, parse date
# Convert reading_time to datetime format
energy_data['reading_time'] = pd.to_datetime(energy_data['reading_time'])

# Check for missing values and handle them (use direct assignment instead of inplace)
energy_data['energy_consumed'] = energy_data['energy_consumed'].fillna(energy_data['energy_consumed'].median())

# 3. Feature Engineering: Extract hour of the day and normalize energy readings
# Extract the hour from reading_time
energy_data['hour_of_day'] = energy_data['reading_time'].dt.hour

# Normalize energy_consumed (z-score normalization)
energy_data['normalized_energy'] = (energy_data['energy_consumed'] - energy_data['energy_consumed'].mean()) / energy_data['energy_consumed'].std()

# Display the processed data without truncation
print(energy_data[['user_id', 'device_id', 'reading_time', 'energy_consumed', 'hour_of_day', 'normalized_energy']])
