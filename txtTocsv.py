import pandas as pd

# Read the text file
dataframe = pd.read_csv("subjects.txt", delimiter="\t") # Adjust the delimiter as needed

# Convert to CSV
dataframe.to_csv("subjects.csv", index=False)