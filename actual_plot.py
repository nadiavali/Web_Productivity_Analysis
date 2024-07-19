
# Import the matplotlib.pyplot library as plt
import matplotlib.pyplot as plt

from main import data_a
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


