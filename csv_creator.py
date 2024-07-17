import pandas as pd

import pandas as pd

# Create the data as provided
data = {
    'Time_Spent_on_Site': [90.987906, 50.794390, 66.206264, 61.225810, 122.862188, 
                           110.375357, 172.102860, 134.548224, 68.672467, 160.964552],
    'Total_Amount_Spent': [496.88, 347.66, 161.50, 70.91, 1014.99, 
                           99.26, 52.29, 332.94, 233.74, 13.23],
    'Page_Views': [12.0, 14.0, 13.0, 8.0, 14.0, 
                   30.0, 40.0, 27.0, 24.0, 27.0],
    'AOV': [47.348084, 38.614252, 21.520578, 11.533441, 90.846582, 
            22.399053, 29.303279, 52.063372, 28.713010, None],
    'Group': ['A', 'A', 'A', 'A', 'A', 
              'B', 'B', 'B', 'B', None]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
file_path = '/Users/NadiaIT/Code/Data_Production/civ_data.csv'
df.to_csv(file_path, index=False)
