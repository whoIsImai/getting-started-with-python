import pandas as pd

df = pd.read_csv("data.csv")

# # new_df = df.dropna(inplace = True)

# # print(new_df.to_string())

# new_df = df.fillna({"Calories": 130}, inplace = True)

v = df["Calories"].mean()

df.fillna({"Calories": v}, inplace=True)
print(df)