import pandas as pd

df = pd.read_csv(r"C:\Users\Admin\Downloads\NetFlix.csv")

print("Total rows:", len(df))
print(df['type'].value_counts())
print(df['rating'].value_counts())