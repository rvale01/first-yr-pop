class Car:
    doors = 0
    price = 0
    colour = ""
    brand = ""

    def __init__(self, doors, price, colour, brand):
        self.doors = doors
        self.price = price
        self.colour = colour
        self.brand = brand

    def startCar(self):
        print("Car has started")

    def stopCar(self):
        print("Car has stopped")

    def setDoors(self, doors):
        self.doors = doors

    def setPrice(self, price):
        self.price = price

    def setColour(self, colour):
        self.colour = colour

    def setBrand(self, brand):
        self.brand = brand

    def getDoors(self):
        return self.doors

    def getPrice(self):
        return self.price

    def getColour(self):
        return self.colour

    def getBrand(self):
        return self.brand


car1 = Car(5, 20000, "White", "ToyCar")

print(car1.startCar())

print("Doors", car1.getDoors())
print("Price", car1.getPrice())
print("Colour", car1.getColour())
print("Brand", car1.getBrand())

print(car1.stopCar())

car1.setPrice(10000)
print("new price", car1.getPrice())
car1.setColour("Red")
print("new colour", car1.getColour())
