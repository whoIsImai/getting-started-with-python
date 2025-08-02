from person import Person

class student(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age, role)
    
class teacher(Person):
    def __init__(self, name, age, role):
        super().__init__(name,age,role)

student1 = student("Imai", 21, "Student").Intro()
teacher1 = teacher("Cos", 40,"Teacher").Intro()