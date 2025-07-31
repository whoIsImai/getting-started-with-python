class Vehicle:
    def __init__(self, type, year, color):
        self.type = type
        self.year = year
        self.color = color

    def move(self):
        return f"The {self.color} {self.type} from {self.year} is moving."
        