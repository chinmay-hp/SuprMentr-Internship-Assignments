# Dataset Detective

import pandas as pd

# Load Dataset

df = pd.read_csv("data.csv")

# Display Top Rows

print("----- Top 5 Rows of Dataset -----")
print(df.head())

# Find Highest Value Column

numeric_columns = df.select_dtypes(include=['number'])

if not numeric_columns.empty:
    highest_column = numeric_columns.max().idxmax()
    highest_value = numeric_columns.max().max()
    print("\n----- Highest Value Column -----")
    print(f"Column with highest value: {highest_column}")
    print(f"Highest value found: {highest_value}")
else:
    print("\nNo numeric columns found in the dataset.")

# Count Missing Values

print("\n----- Missing Values in Each Column -----")
print(df.isnull().sum())

# Basic Dataset Information

print("\n----- Dataset Information -----")
print(f"Number of Rows: {df.shape[0]}")
print(f"Number of Columns: {df.shape[1]}")

print("\n----- Column Names -----")
print(df.columns.tolist())

print("\n----- Summary Statistics -----")
print(df.describe())




# The 5 Insights from the Dataset are :-

# Insight 1:
# - The dataset contains multiple rows and columns, showing structured tabular data suitable for analysis.

# Insight 2:
# - The first few rows help in understanding the type and pattern of values present in the dataset.

# Insight 3:
# - The highest value column indicates which feature contains the largest numerical values in the dataset.

# Insight 4:
# - Missing values are present in some columns (if any), which means data cleaning may be required before further processing.

# Insight 5:
# - Summary statistics such as mean, minimum, maximum, and standard deviation help in understanding the data distribution.