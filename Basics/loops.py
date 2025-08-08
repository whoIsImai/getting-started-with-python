# i = 0
# while i < 10:
#     print(f"Value: {i}")
#     i+=1
#     if i == 5:
#         print(f"Breaking at {i}")
#         continue
# else:
#     print("Loop completed without break")

list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]

# for i in range(len(list_1)):
#     for j in range(len(list_2)):
#         print(f"Pair: {list_1[i]}, {list_2[j]}")

for x in list_1:
    for y in list_2:
        print(f"Pair: {x}, {y}")    