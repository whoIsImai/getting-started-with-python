import pandas as pd

data_set = {
    "cars" : ["Toyota","Camry", "Honda", "Civic"],
    "year" : [2020, 2021, 2022, 2023],
    "price" : [20000, 22000, 25000, 270]
}
df = pd.DataFrame(data_set)
series = pd.Series(data_set)

print("### series ###")
print(series)
print("### DataFrame ###")
print(df)