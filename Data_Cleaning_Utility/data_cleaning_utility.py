import pandas as pd
import numpy as np

print("=" * 60)
print("           DATA CLEANING UTILITY")
print("=" * 60)

# Create sample raw customer dataset
data = {
    "Customer Name": [
        "Ananya", "Rahul", "Priya", "Kiran", "Ananya",
        "Vikram", "Sneha", "Arjun", "Priya", "Meena"
    ],
    "Age": [
        23, 28, np.nan, 35, 23,
        "Thirty", 26, 31, np.nan, 29
    ],
    "City Name": [
        "Hyderabad", "Bangalore", "Hyderabad", "Chennai",
        "Hyderabad", "Pune", "Bangalore", "Chennai",
        "Hyderabad", "Pune"
    ],
    "Purchase Amount": [
        2500, 4200, 1800, np.nan, 2500,
        5600, 3200, 4100, 1800, np.nan
    ],
    "Purchase Date": [
        "2026-01-10", "2026-01-12", "2026-01-15",
        "2026-02-01", "2026-01-10", "2026-02-05",
        "2026-02-08", "2026-02-10", "2026-01-15",
        "invalid-date"
    ]
}

df = pd.DataFrame(data)

# Add duplicate intentionally
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

print("\n1. RAW DATA")
print(df)

print("\nOriginal Shape:", df.shape)

# Cleaning log
cleaning_log = []

# Standardize column names
old_columns = df.columns.tolist()

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

cleaning_log.append("Standardized all column names.")

# Fix data types
df["age"] = pd.to_numeric(df["age"], errors="coerce")
cleaning_log.append("Converted age column to numeric.")

df["purchase_amount"] = pd.to_numeric(
    df["purchase_amount"], errors="coerce"
)
cleaning_log.append("Converted purchase_amount column to numeric.")

# Parse dates
df["purchase_date"] = pd.to_datetime(
    df["purchase_date"], errors="coerce"
)
cleaning_log.append("Parsed purchase_date and handled invalid dates.")

# Missing values before cleaning
print("\n2. MISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

# Fill missing values
df["age"] = df["age"].fillna(df["age"].median())
df["purchase_amount"] = df["purchase_amount"].fillna(
    df["purchase_amount"].median()
)
df["purchase_date"] = df["purchase_date"].fillna(
    df["purchase_date"].mode()[0]
)

cleaning_log.append("Filled missing age values using median.")
cleaning_log.append("Filled missing purchase amounts using median.")
cleaning_log.append("Filled missing dates using mode.")

# Remove duplicates
duplicate_count = df.duplicated().sum()

print("\n3. DUPLICATES FOUND:", duplicate_count)

df = df.drop_duplicates()

cleaning_log.append(
    f"Removed {duplicate_count} duplicate row(s)."
)

# Final validation
print("\n4. MISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

print("\n5. DATA TYPES AFTER CLEANING")
print(df.dtypes)

print("\n6. CLEANED DATA")
print(df)

print("\nFinal Shape:", df.shape)

# Save cleaned dataset
df.to_csv("cleaned_customer_data.csv", index=False)

# Save cleaning log
with open("cleaning_log.txt", "w") as file:
    file.write("DATA CLEANING LOG\n")
    file.write("=" * 40 + "\n\n")

    for step in cleaning_log:
        file.write("- " + step + "\n")

print("\n7. GENERATED FILES")
print("cleaned_customer_data.csv")
print("cleaning_log.txt")

print("\n" + "=" * 60)
print("      DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 60)