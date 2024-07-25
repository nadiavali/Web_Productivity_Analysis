from main import data_a, data_b

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

'''
Normalization
Before applying the IQR method, we need to ensure our data follows a normal distribution.
Although the IQR method can be applied to any distribution, normalizing the data first will yield more accurate results.
Since we know our target columns follow an exponential distribution, we can use the Box-Cox transformation
to convert the exponential distribution into a normal distribution.
'''
def detect_outliers(column):
    # Normalizing the data
    transformed_data, _ = stats.boxcox(column + 1)

    # Plotting the transformed data
    plt.figure(figsize=(10, 6))
    plt.hist(transformed_data, bins=30, alpha=0.7, color='blue')
    plt.title('Histogram of Transformed Data')
    plt.xlabel('Transformed values')
    plt.ylabel('Frequency')
    #plt.show()

    # calculate IQR
    Q1 = np.percentile(transformed_data, 25)
    Q3 = np.percentile(transformed_data, 75)
    IQR = Q3 - Q1

    # Calculate boundries baseed on IQR shouöd be 1.5 but that is too harsh in this case
    left_bound = Q1 - 1.5 * IQR
    right_bound = Q3 - 1.5 * IQR

    # Detect outliers
    outlier_indices = column.index[
        (transformed_data < left_bound) | (transformed_data > right_bound)
    ]

    return outlier_indices


# Extract outlier indices
data_a_spent_outliers = detect_outliers(data_a['Total_Amount_Spent'])
data_b_spent_outliers = detect_outliers(data_b['Total_Amount_Spent'])
data_a_aov_outliers = detect_outliers(data_a['AOV'])
data_b_aov_outliers = detect_outliers(data_b['AOV'])

# Print outlier quantity
print(f'Total_Amount_Spent, Group A: {data_a_spent_outliers.size}')
print(f'Total_Amount_Spent, Group B: {data_b_spent_outliers.size}')
print(f'AOV, Group A: {data_a_aov_outliers.size}')
print(f'AOV, Group B: {data_b_aov_outliers.size}')


total_data_points = data_a['AOV'].size
number_of_outliers = data_a_spent_outliers.size
percentage_of_outliers = (number_of_outliers / total_data_points) * 100

#print(f"Percentage of data removed as outliers: {percentage_of_outliers}%")


# Filter group A data
data_a_filtered = data_a.drop(data_a_spent_outliers)
data_a_filtered = data_a_filtered.drop(data_a_aov_outliers, errors='ignore')

# Filter group B data
data_b_filtered = data_b.drop(data_b_spent_outliers)
data_b_filtered = data_b_filtered.drop(data_b_aov_outliers, errors='ignore')

# Display filtered data
display(data_a_filtered)
display(data_b_filtered)
