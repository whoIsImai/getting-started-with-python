my_list = ["apple", "banana", "cherry", "mango", "orange", "grape", "kiwi", "pear"]

#print(my_list[2:5]) # Output: ['cherry', 'mango', 'orange']

# last_index = len(my_list) -1

# print(my_list[last_index])

# my_list.append("peach")  # Adding a new fruit to the list
# print(my_list)

# my_list.insert(2, "blueberry")  # Inserting 'blueberry' at index 2
# print(my_list) 

# my_list.remove("cherry")  # Removing 'cherry' from the list
# print(my_list)

# for i in range(len(my_list)):
#     print(f"at index {i} = {my_list[i]}")  # Printing each fruit in the list

i = 0
while i < len(my_list):
    print(f"at index {i} = {my_list[i]}")
    i += 1 