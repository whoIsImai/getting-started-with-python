class Person():
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def Intro(self):
        return print(f"Hi, i'm {self.name} {self.age} old. I'm a {self.role}")