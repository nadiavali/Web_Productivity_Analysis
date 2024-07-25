import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

from main import data_a, data_b


# Setting up a function is the best way to opzimize time and space
#  Plotting the distributions of a given dataset column for a specific group
def plot_distributions(column, group_name):
    # Calculate the theoretical distributions based on the data
    x_values = np.linspace(min(column), max(column), 100)
    distributions = {  # Create a dictionary with calculated theoretical distributions
        "Normal": stats.norm.pdf(x_values, *stats.norm.fit(column)),
        "Exponential": stats.expon.pdf(x_values, *stats.expon.fit(column)),
        "Uniform": stats.uniform.pdf(
            x_values, loc=min(column), scale=max(column) - min(column)
        ),
    }

    # Set up a plot with 1 row and 3 columns
    # We need 3 plots, no? yes
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Loop through each subplot and distribution # love the zip here(3 in 1)
    for ax, (distribution_name, distribution) in zip(axes, distributions.items()):

        ax.hist(
            column,
            bins=70,
            alpha=0.5,
            label=f"{column.name} of {group_name}",
            density=True,
        )
        ax.plot(x_values, distribution, label="Theoretical Distribution")
        ax.set_title(f"{distribution_name} Distribution")
        ax.set_xlabel(column.name)
        ax.set_ylabel("Density")
        ax.legend()
    # Get out of the loopppp!!!
    plt.show()


# Call the function, it will answer
plot_distributions(data_a["AOV"], "Group A")
plot_distributions(data_b["AOV"], "Group B")
plot_distributions(data_a["Total_Amount_Spent"], "Group A")
plot_distributions(data_b["Total_Amount_Spent"], "Group B")
