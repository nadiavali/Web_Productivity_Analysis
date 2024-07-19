from IPython.display import display
import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('CSV_data.csv')

display(data)


data_a = data[data['Group'] == 'A']
data_b = data[data['Group'] == 'B']

display(data_a.describe())
display(data_b.describe())

'''
This function provides insights into:
*Statistic	Description
count	The number of non-missing values
mean	The arithmetic mean (average)
std	How spreaded the data is
min	The minimum value
25%	The 25th percentile or the first quartile
50%	The 50th percentile or the median
75%	The 75th percentile or the third quartile
max	The maximum value

'''


