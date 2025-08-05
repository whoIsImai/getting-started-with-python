from person import Person

class student(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age, role)
    
class teacher(Person):
    def __init__(self, name, age, role):
        super().__init__(name,age,role)

    def getCourse(self):
        course = input("Enter the course you're teachin: ")
        return print(f"{self.name} is teaching {course}")

student1 = student("Imai", 21, "Student")

teacher1 = teacher("Cos", 40,"Teacher")



try:
    student1.Intro()
    student1.getCourse()
    student1.subjects()
    print("#########################################################")

    teacher1.Intro()
    teacher1.getCourse()
    teacher1.subjects()
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors occurred.")
finally:
    print("Execution completed.")