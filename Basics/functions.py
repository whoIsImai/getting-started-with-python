# def hello_world() -> str:
#    return print("Hello World From Function!")

# hello_world()

# def add_numbers(num1: int, num2: int) -> int:
#     return print(num1 + num2)

# add_numbers(2,10)

# def User(**user) -> str:
#     return print(f"name: {user["name"]}, age: {user["age"]}, country: {user["country"]}")

# User(name="John Doe", age=30, country="USA")

add_numbers = lambda num1, num2: num1 + num2
print(add_numbers(5, 15))