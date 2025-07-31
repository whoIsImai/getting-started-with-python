# my_dic = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "Randburg",
# }
# name = my_dic["name"]
# print(f"Name: {name}")

# keys = my_dic.keys()
# values = my_dic.values()
# print(f"Keys: {keys}- Values: {values}")

# items = my_dic.items()
# print(f"{items}")

# my_dic["country"] = "South Africa"
# print(f"{my_dic}")

# for x in my_dic:
#     print(f"{x} : {my_dic[x]}")

# for x, y in my_dic.items():
#     print(f"{x} : {y}")

####### nested dictionary #######

john = {
    "name": "John Doe",
    "age": 30,
    "city": "Randburg",
}

jane = {
    "name": "Jane Doe",
    "age": 28,
    "city": "Sandton",
}

people = {
    "john": john,
    "jane": jane,
}

for key, value in people.items():
    print(f"{key}:")
    for key, value in value.items():
        print(f"{key}: {value}")
