class ComputerA:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def display(self):
        print("Computer's name is: " + str(self.getName()) +
              " its price is %.2f" %self.getPrice())


isName = False

while(not isName):
    name = str(input("Input the computer's name: "))

    if 2 <= len(name) <= 10:
        isName = True
    else:
        print("The name is invalid!")

isPrice = False

while (not isPrice):
    price = float(input("Input the computer's price: "))

    if 999.99 >= price >= 99.9:
        isPrice = True
    else:
        print("The price is not valid")

comp = ComputerA(name, price)
comp.display()

# comp.setName("Dell")
# comp.setPrice(900.00)

# part 1.3
comp.name = "Dell"
comp.price = 200.30
comp.display()
