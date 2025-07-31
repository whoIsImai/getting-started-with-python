class person:
    def __init__(self, name: str, age:int):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Hi, i'm {self.name} and i am {self.age} old"
    
p1 = person("John", 30)
print(p1)
        