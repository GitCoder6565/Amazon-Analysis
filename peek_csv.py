import pandas as pd

try:
    df = pd.read_csv('Amazon.csv', nrows=5)
    print("Columns:", df.columns.tolist())
    print("\nFirst 5 rows:")
    print(df.head())
except Exception as e:
    print(f"Error reading CSV: {e}")
