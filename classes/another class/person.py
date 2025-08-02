class Person():
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def Intro(self):
        return print(f"Hi, i'm {self.name} {self.age} old. I'm a {self.role}")
    
    def getCourse(self):
        course = input("Enter your course: ")
        return print(f"{self.name} is doin {course}")
    
    def subjects(self):
        sub = []
        sub1 = input("Enter your first subject: ")
        sub.append(sub1)
        ans = input("Do you want to add another subject? (yes/no): ")
        while ans.lower() == 'yes':
                sub2 = input("Enter your next subject: ")
                sub.append(sub2)
                ans = input("Do you want to add another subject? (yes/no): ")
                if ans.lower() == 'no':
                  return print(f"{self.name} = {sub1} and {sub}")