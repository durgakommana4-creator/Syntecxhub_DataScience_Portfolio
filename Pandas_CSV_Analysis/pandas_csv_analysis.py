import pandas as pd

print("=" * 60)
print("        PANDAS CSV READER & BASIC ANALYSIS")
print("=" * 60)

# ---------------------------------------------------------
# 1. Create sample CSV dataset
# ---------------------------------------------------------

data = {
    "Name": [
        "Ananya", "Rahul", "Priya", "Kiran", "Vikram",
        "Sneha", "Arjun", "Meena", "Ravi", "Divya"
    ],
    "Age": [23, 28, 25, 31, 29, 26, 24, 30, 27, 22],
    "City": [
        "Hyderabad", "Bangalore", "Hyderabad", "Chennai",
        "Pune", "Bangalore", "Chennai", "Hyderabad",
        "Pune", "Hyderabad"
    ],
    "Salary": [
        35000, 48000, 42000, 55000, 50000,
        45000, 38000, 52000, 46000, 34000
    ],
    "Experience": [1, 3, 2, 5, 4, 3, 1, 5, 3, 1]
}

sample_df = pd.DataFrame(data)

# Save sample CSV
sample_df.to_csv("employee_data.csv", index=False)

print("\nSample CSV created: employee_data.csv")

# ---------------------------------------------------------
# 2. Read CSV using Pandas
# ---------------------------------------------------------

df = pd.read_csv("employee_data.csv")

print("\n1. COMPLETE DATASET")
print(df)

# ---------------------------------------------------------
# 3. First five rows
# ---------------------------------------------------------

print("\n2. FIRST FIVE ROWS")
print(df.head())

# ---------------------------------------------------------
# 4. Last five rows
# ---------------------------------------------------------

print("\n3. LAST FIVE ROWS")
print(df.tail())

# ---------------------------------------------------------
# 5. Data types
# ---------------------------------------------------------

print("\n4. DATA TYPES")
print(df.dtypes)

# ---------------------------------------------------------
# 6. Dataset information
# ---------------------------------------------------------

print("\n5. DATASET INFORMATION")
print(df.info())

# ---------------------------------------------------------
# 7. Summary statistics
# ---------------------------------------------------------

print("\n6. SUMMARY STATISTICS")
print(df.describe())

# ---------------------------------------------------------
# 8. Mean, Median, Minimum and Maximum
# ---------------------------------------------------------

print("\n7. SALARY ANALYSIS")

print("Mean Salary:", df["Salary"].mean())
print("Median Salary:", df["Salary"].median())
print("Minimum Salary:", df["Salary"].min())
print("Maximum Salary:", df["Salary"].max())

# ---------------------------------------------------------
# 9. Column selection
# ---------------------------------------------------------

print("\n8. SELECTED COLUMNS")
print(df[["Name", "City", "Salary"]])

# ---------------------------------------------------------
# 10. Filtering
# ---------------------------------------------------------

high_salary = df[df["Salary"] > 45000]

print("\n9. EMPLOYEES WITH SALARY ABOVE 45000")
print(high_salary)

# ---------------------------------------------------------
# 11. Multiple condition filtering
# ---------------------------------------------------------

experienced_employees = df[
    (df["Experience"] >= 3) &
    (df["Salary"] >= 45000)
]

print("\n10. EXPERIENCED EMPLOYEES")
print(experienced_employees)

# ---------------------------------------------------------
# 12. City-wise analysis
# ---------------------------------------------------------

print("\n11. CITY-WISE EMPLOYEE COUNT")
print(df["City"].value_counts())

# ---------------------------------------------------------
# 13. Average salary by city
# ---------------------------------------------------------

print("\n12. AVERAGE SALARY BY CITY")
print(df.groupby("City")["Salary"].mean())

# ---------------------------------------------------------
# 14. Save filtered data
# ---------------------------------------------------------

high_salary.to_csv(
    "high_salary_employees.csv",
    index=False
)

print("\n13. FILTERED DATA SAVED")
print("high_salary_employees.csv")

print("\n" + "=" * 60)
print("       PANDAS ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)