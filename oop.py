# class person:
#     def __init__(self, name: str, age:int):
#         self.name = name
#         self.age = age
#     # def __str__(self):
#     #     return f"Hi, i'm {self.name} and i am {self.age} old"
    
#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# p1 = person("John", 30)
# print(p1.greet())
        
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, i'm {self.name} and I am {self.age}."
    
class Student(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def greet(self):
        return f"Hello, I'm {self.name}, I am {self.age} years old and I am a {self.role}."

WhoIsImai = Student("Imai", 20, "Student").greet()
print(WhoIsImai)
        