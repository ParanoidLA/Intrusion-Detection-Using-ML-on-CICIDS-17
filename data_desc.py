import pandas as pd
# Specify the path to your CSV file without double quotes
csv_file_path = r'E:\IDS\final\18lakh.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Display basic statistics for each column
print("Summary Statistics:")
print(df.describe())

# Display information about the DataFrame, including data types and non-null values
print("\nData Information:")
print(df.info())

# Display the column names
print("\nColumn Names:")
print(df.columns)
