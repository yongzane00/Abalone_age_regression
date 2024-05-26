import pandas as pd

# Assuming 'abalone.data' is a CSV-like file without a header
column_names = ['sex', 'length(mm)', 'diameter(mm)', 'height(mm)', 'whole_weight(grams)', 'shucked_weight(grmas)', 'viscera_weight(grams)', 'shell_weight(grams)', 'number_of_rings']

df = pd.read_csv('abalone.data', header=None, names=column_names)

df.to_csv('abalone.csv', index=False)
