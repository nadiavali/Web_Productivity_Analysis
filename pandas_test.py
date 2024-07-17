import pandas as pd

# Sample data
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 6, 7, 8, 9],
    'C': [10, 11, 12, 13, 14]
}

# Creating a DataFrame
df = pd.DataFrame(data)
print(df)
# Calculating the standard deviation for each column
std_devs = df.std()
print("Standard deviation for each column:")
print(std_devs)

# Calculating the standard deviation for a specific column
std_dev_A = df['A'].std()
print("\nStandard deviation for column A:")
print(std_dev_A)

# Calculating the standard deviation for each row
std_devs_rows = df.std(axis=1)
print("\nStandard deviation for each row:")
print(std_devs_rows)
