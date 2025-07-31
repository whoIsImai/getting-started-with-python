from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, year, color, make, model):
        super().__init__("Car", year, color)
        self.make = make
        self.model = model

    def move(self):
        return f"The {self.color} {self.make} {self.model} car from {self.year} is driving."
    
class Plane(Vehicle):
    def __init__(self, type, year, color):
        super().__init__(type, year, color)

    def move(self):
        return f"The {self.color} {self.type} from {self.year} is flying."
    
class Boat(Vehicle):
    def __init__(self, type, year, color):
        super().__init__(type, year, color)

    def move(self):
        return f"The {self.color} {self.type} from {self.year} is sailing."
    
car = Car(2020, "red", "Toyota", "Corolla")
plane = Plane("Boeing 747", 2015, "white")
boat = Boat("Yacht", 2018, "blue")