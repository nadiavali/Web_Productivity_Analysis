# Import mathematical and statistical libraries
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

from main import data_a

# Column selection
column = data_a['AOV']  

# Calculate the theoretical distributions based on the data
x_values = np.linspace(min(column), max(column), 100)  # Create a range of values for the x-axis
#(it creates 100 points between the minimum and maximum values of the 'AOV' column from my dataset.)

distributions = {  # Create a dictionary with calculated theoretical distributions
    'Normal': stats.norm.pdf(x_values, *stats.norm.fit(column)), #pdf: probability density function (PDF)
    'Exponential': stats.expon.pdf(x_values, *stats.expon.fit(column)),
    'Uniform': stats.uniform.pdf(x_values, loc=min(column), scale=max(column)-min(column))
}

# Specify and extract distribution to use
distribution_name = 'Exponential'  
distribution = distributions[distribution_name] 

# Plotting
fig, axes = plt.subplots(1, 1, figsize=(16, 5))  # Create a single plot
# density=True normalizes the histogram so that the area under the histogram equals 1,
# allowing it to be compared directly with the probability density function (PDF).
axes.hist(column, bins=70, alpha=0.5, label=column.name, density=True)  # Histogram of the data, semi transparent thanks to alpha
axes.plot(x_values, distribution, label='Theoretical Distribution')  # Theoretical distribution line
axes.set_title(f'{distribution_name} Distribution')
axes.set_xlabel(column.name)
axes.set_ylabel('Density')
axes.legend()  # Display legend
plt.show()



