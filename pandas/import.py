import pandas as pd

# data_set = {
#     "cars" : ["Toyota","Camry", "Honda", "Civic"],
#     "year" : [2020, 2021, 2022, 2023],
#     "price" : [20000, 22000, 25000, 270]
# }
# df = pd.DataFrame(data_set, index = ["1st", "2nd", "3rd", "4th"])
# # series = pd.Series(data_set)

# # print("### series ###")
# # print(series)
# print("### DataFrame ###")
# print(df)
# print("### DataFrame with index ###")
# print(df.loc["1st":"2nd", ["cars", "year"]])

data_set = pd.read_csv("data.csv")
#print(data_set)
pd.options.display.max_rows = 500
print(data_set.head(5))