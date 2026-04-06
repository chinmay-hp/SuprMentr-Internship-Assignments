# Data Doctor - Dataset Cleaning Program

import pandas as pd

# Load Dataset

df = pd.read_csv("data.csv")

print("----- Original Dataset -----")
print(df.head())

# 1. Handling Missing Values

# Fill numeric missing values with mean
for col in df.select_dtypes(include='number').columns:
    df[col].fillna(df[col].mean(), inplace=True)

# Fill text missing values with "Unknown"
for col in df.select_dtypes(include='object').columns:
    df[col].fillna("Unknown", inplace=True)

# 2. Removing Duplicates

df.drop_duplicates(inplace=True)

# 3. Standardizing Text

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip().str.title()

# Display Cleaned Dataset

print("\n----- Cleaned Dataset -----")
print(df.head())

# Save Cleaned Dataset

df.to_csv("cleaned_data.csv", index=False)

print("\n✅ Data cleaning completed successfully!")
print("Cleaned file saved as 'cleaned_data.csv'")