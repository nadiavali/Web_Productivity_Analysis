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


# Import the matplotlib.pyplot library as plt
import matplotlib.pyplot as plt

# Select a column to visualize
column = data_a['AOV']

# Create a single plot (1x1) of a specific size
fig, axes = plt.subplots(1, 1, figsize=(16, 5))

# Initialize the plot title
axes.set_title(f'{column.name} Distribution')

# Generate the histogram of a column, specifying number of bins
axes.hist(column, bins=100)

# Label the x-axis and y-axis
axes.set_xlabel(column.name)
axes.set_ylabel('Density')

# Render and display the plot
plt.show()



column = data_a['Total_Amount_Spent']
fig, axes = plt.subplots(1,1, figsize=(16,5))
axes.set_title(f'{column.name} :)')
axes.hist(column, bins=50)

axes.set_xlabel(column.name)
axes.set_ylabel('Density')
plt.show()