import pandas as pd
import numpy as np

# Import dataset
df = pd.read_excel("Maths.csv", engine="openpyxl")

# Inspect dataset
print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nDataset information:")
df.info()

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

print("\nTotal missing values:")
print(df.isnull().sum().sum())

# Check duplicate records
print("\nNumber of duplicate records:")
print(df.duplicated().sum())

print("\nDuplicate records:")
print(df[df.duplicated(keep=False)])

# Remove duplicates
df = df.drop_duplicates()

# Remove extra spaces from text columns
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()

# Check data types again
print("\nData types after cleaning:")
print(df.dtypes)

# Check unique values
print("\nUnique values in categorical columns:")

for col in text_columns:
    print(col, ":", df[col].unique())

# Statistical summary
print("\nStatistical summary:")
print(df.describe())

# Final cleaning check
print("\nFinal dataset shape:")
print(df.shape)

print("\nFinal missing values:")
print(df.isnull().sum().sum())

print("\nFinal duplicate records:")
print(df.duplicated().sum())

# Save cleaned dataset
df.to_csv("cleaned_Maths.csv", index=False)

print("\nCleaned dataset saved successfully!")