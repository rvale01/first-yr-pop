class ComputerA:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def setName(self, name):
        self.__name = name

    def setPrice(self, price):
        self.__price = price

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

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

# part 1.4
# comp.__name = "Dell"
# comp.__price = 200.30

comp.setName("Dell")
comp.setPrice(900.00)
comp.display()
