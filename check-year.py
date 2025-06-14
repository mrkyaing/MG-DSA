import pandas as pd

# Load the CSV file
file_path = "D:\\au_works\\Results.csv"  # Change this path if your file is elsewhere
df = pd.read_csv(file_path)

# Check if 'Original_WeekPattern' column contains the string "2026"
if 'Original_WeekPattern' in df.columns:
    contains_2026 = df['Original_WeekPattern'].astype(str).str.contains("2026")
    rows_with_2026 = df[contains_2026]
    print("Number of rows with '2026' in 'Original_WeekPattern':", len(rows_with_2026))
    print(rows_with_2026)
else:
    print("Column 'Original_WeekPattern' not found in the CSV file.")
