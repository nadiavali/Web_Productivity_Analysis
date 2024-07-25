import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

from actual_plot import data_a


column = data_a["Total_Amount_Spent"]
x_values = np.linspace(min(column), max(column), 100)

distributions = {
    "Normal": stats.norm.pdf(x_values, *stats.norm.fit(column)),
    "Exponential": stats.expon.pdf(x_values, *stats.expon.fit(column)),
    "Lognormal": stats.lognorm.pdf(x_values, *stats.lognorm.fit(column)),
}

distribution_name = "Lognormal"
distribution = distributions[distribution_name]


fig, axes = plt.subplots(1, 1, figsize=(16, 5))
axes.hist(column, bins=70, alpha=0.5, label=column.name, density=True)  # plo
axes.plot(x_values, distribution, label="Theoretical Distibution")
axes.set_xlabel(column.name)
axes.set_ylabel("Density")
axes.legend()
plt.show()
