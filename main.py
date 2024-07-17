
from IPython.display import display
import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('Web_Data.csv')

display(data)


data_a = data[data['Group'] == 'A']
data_b = data[data['Group'] == 'B']

display(data_a.describe())
display(data_b.describe())

