import pandas as pd

# Read the text file
dataframe = pd.read_csv("staff_diploma.txt", delimiter="\t") # Adjust the delimiter as needed

# Convert to CSV
dataframe.to_csv("staff_diploma.csv", index=False)