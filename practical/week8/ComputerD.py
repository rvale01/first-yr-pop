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
              " its price is %.2f" % self.getPrice())


def checkName():
    isName = False
    while(not isName):
        name = str(input("Input the computer's name: "))
        if 2 <= len(name) <= 10:
            isName = True
            return name
        else:
            print("The name is invalid!")


def checkPrice():
    isPrice = False

    while (not isPrice):
        price = float(input("Input the computer's price: "))
        if 999.99 >= price >= 99.9:
            isPrice = True
            return price
        else:
            print("The price is not valid")


objectList = []

for x in range(5):
    name = checkName()
    price = checkPrice()
    obj = ComputerA(name,price)
    objectList.append(obj)

for x in objectList:
    x.display()
