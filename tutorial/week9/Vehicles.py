class Vehicle:
    def __init__(self, colour, type):
        self.colour = colour
        self.type = type

    def __str__(self):
        return "Colour: " + self.colour + ", Type:"+ self.type

class Bus(Vehicle):
    def __init__(self, colour, speed, busType):
        super().__init__(colour, "Bus")
        self.speed = speed
        self.busType = busType

    def __str__(self):
        return super().__str__() + "Speed: " + str(self.speed) + "Bus type: " + self.busType

class Car(Vehicle):
    def __init__(self, colour, speed, carType):
        super().__init__(colour, "Car")
        self.speed = speed
        self.carType = carType

    def __str__(self):
        return super().__str__() + "Speed: " + str(self.speed) + "Car type: " + self.carType

class Truck(Vehicle):
    def __init__(self, colour, weightLimit, purpose):
        super().__init__(colour, "Truck")
        self.weightLimit = weightLimit
        self.purpose = purpose

    def __str__(self):
        return super().__str__() + "Weight Limit: " + str(self.weightLimit) + ", Purpose: " + self.purpose

class Mercedes_Benzes(Car):
    def __init__(self, colour, speed, carType):
        super().__init__(colour,speed, carType)
    
    def __str__(self):
        return super().__str__() + "Brand: Mercedes Benzes"

class Honda_Accord(Car):
    def __init__(self, colour, speed, carType):
        super().__init__(colour,speed, carType)
    def __str__(self):
        return super().__str__() + "Brand: Honda Accord"



truck1 = Truck("black", 300, "Heavy material")
mercBen = Mercedes_Benzes("white", 120, "SUV")
honAcc = Honda_Accord("red", 240, "sport car")

print(truck1)
print()
print(mercBen)
print()
print(honAcc)


