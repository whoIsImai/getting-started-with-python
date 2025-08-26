import pandas as pd

df = pd.read_csv("data.csv")

# new_df = df.dropna(inplace = True)

# print(new_df.to_string())

new_df = df.fillna(111, inplace = True)
