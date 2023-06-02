# Full Name: Valentina Ronchi
# Date: 20/01/2021
# Student n.: 20035819
# Description: This program is a software system to keep track of stock items and prices
# of a car Parts and Accessories shop


class StockItem:
    __stockCategory = "Car accessories"

    # constructor for Stock Item
    def __init__(self, quantity=0, price=0.0, stockCode=None):
        self.__stockCode = stockCode
        self.__quantity = quantity
        self.__price = price
        self.__priceWithVAT = self.__price + self.getVAT()*self.__price

    # setters and getters
    def setStockCode(self, stockCode):
        self.__stockCode = stockCode

    def getStockCode(self):
        return self.__stockCode

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def getQuantity(self):
        return self.__quantity

    def setPriceWithoutVAT(self, price):
        self.__price = price
        self.setPriceWithVAT()

    def getPriceWithoutVAT(self):
        return self.__price

    def setPriceWithVAT(self):
        self.__priceWithVAT = self.__price + self.getVAT()*self.__price

    def getPriceWithVAT(self):
        return self.__priceWithVAT

    def getStockName(self):
        return "Unknown Stock Name"

    def getStockDescription(self):
        return "Unknown Stock Description"

    # method to increase the stock quantiy
    def increaseStock(self, value):
        if(value < 1):  # if the value given by the user is less than 1, it prints an error
            print("Error: the value given cannot be lower than 1")
        elif(self.__quantity > 100):  # if the quantity is more than 100, it prints an error
            print("Error: The quantity of the object is too high")
        else:  # if all the conditions are not met, the value of the user is added to the existing quantity
            self.__quantity += value

    # method to sell the quantity
    def sellStock(self, value):
        if (value < 1):  # if the value given by the user is less than 1, it prints an error
            print("Error: the value given cannot be lower than 1")
        # if the value given by the user is less or equal than the quantity available of the stock, it returns true
        elif(value <= self.__quantity):
            self.__quantity -= value
            return True
        else:  # otherwise it will return False
            return False

    # returns the VAT value
    def getVAT(self):
        return 17.5/100

    # this method is called when I print the object
    def __str__(self):
        return "Stock code: " + self.getStockCode() + "\nStock name: " + self.getStockName() \
            + "\nStock category: " + StockItem.__stockCategory\
            + "\nStock description: " + self.getStockDescription() \
            + "\nQuantity: " + str(self.getQuantity()) \
            + "\nPrice before VAT: " + "{:.2f}".format(self.getPriceWithoutVAT())\
            + "\nPrice after VAT: " + "{:.2f}".format(self.getPriceWithVAT())


class NavSys(StockItem):
    # constructor of the Navigation system
    def __init__(self, quantity=0, price=0.0, stockCode=None, navsysBrand=None):
        # here the constructor of the super class is called
        super().__init__(quantity, price, stockCode)
        self.__navsysBrand = navsysBrand

    #setters and getters
    def setNavsysBrand(self, navsysBrand):
        self.__navsysBrand = navsysBrand

    def getNavsysBrand(self):
        return self.__navsysBrand

    # overriding two methods of the super class
    def getStockName(self):
        return "Navigation system"

    def getStockDescription(self):
        return "GeoVision Sat Nav"

    # overriding the __str__ method
    def __str__(self):
        return super().__str__() + "\nBrand: " + self.getNavsysBrand()


class AlSys(StockItem):
    # constructor of the Alarm System
    def __init__(self, quantity=0, price=0.0, stockCode=None, numbBatteries=0):
        super().__init__(quantity, price, stockCode)
        self.__numbBatteries = numbBatteries

    #setters and getters
    def setNumbBatteries(self, numbBatteries):
        self.__numbBatteries = numbBatteries

    def getNumbBatteries(self):
        return self.__numbBatteries

    # overriding two methods of the super class
    def getStockName(self):
        return "Alarm system"

    def getStockDescription(self):
        return "Alarm system for cars"

    # overriding the __str__ method
    def __str__(self):
        return super().__str__()+"\nNumber of batteries: "+self.getNumbBatteries()


class VacClean(StockItem):
    # constructor of the Vacuum Cleaner
    def __init__(self, quantity=0, price=0.0, stockCode=None, wattage=None):
        super().__init__(quantity, price, stockCode)
        self.__wattage = wattage

    #setters and getters
    def setWattage(self, wattage):
        self.__wattage = wattage

    def getWattage(self):
        return self.__wattage

    # overriding two methods of the super class
    def getStockName(self):
        return "Car vacuum cleaner"

    def getStockDescription(self):
        return "Car vacuum cleaner with accessories"

    # overriding the __str__ method
    def __str__(self):
        return super().__str__()+"\nWattage: "+str(self.getWattage())


class SteerWheelCov(StockItem):
    # constructor of the Steering Wheel Cover
    def __init__(self, quantity=0, price=0.0, stockCode=None, colour=0):
        super().__init__(quantity, price, stockCode)
        self.__colour = colour

    #setters and getters
    def setColour(self, colour):
        self.__colour = colour

    def getColour(self):
        return self.__colour

    # overriding two methods of the super class
    def getStockName(self):
        return "Steering wheel cover "

    def getStockDescription(self):
        return "Steering wheel cover "

    # overriding the __str__ method
    def __str__(self):
        return super().__str__()+"\nColour: "+self.getColour()


# Step 1.2 of the coursework #Commented because it is not a compulsory step
# print("Add stock information:")
# code = str(input("Input stock code: "))
# price = float(input("Input price without VAT: "))
# quantity = int(input("Input unit number: "))

# print("\n")
# stock1 = StockItem(quantity, price, code)
# print(stock1)

# print("Increasing 4 units")
# stock1.increaseStock(4)
# print(stock1)

# print("Selling 2 units")
# result = stock1.sellStock(2)
# if(result):
#     print(stock1)
# else:
#     print("Unsuccessful, pleasy try with another value!")
# print("Setting price to 85")
# stock1.setPriceWithoutVAT(85)
# print("Increasing 0 unit")
# stock1.increaseStock(0)


# creating an object for each child class
# Navigation system
print("Creating a navigation system stock")
print("Add new information: ")
navCode = str(input(" - Input stock code: "))
navPrice = float(input(" - Input price without VAT: "))
navQuantity = int(input(" - Unit in stock: "))
navBrand = str(input(" - Input brand: "))
navSys1 = NavSys(navQuantity, navPrice, navCode, navBrand) # creating instance of the NavSys class (object)

print("Navigation system stock was created")
print("\n\n")

# Alarm System
print("Creating an alarm system stock")
print("Add new information: ")
alSysCode = str(input(" - Input stock code: "))
alSysPrice = float(input(" - Input price without VAT: "))
alSysQuantity = int(input(" - Unit in stock: "))
alSysBatteries = str(input(" - Input number of batteries: "))
alSyst1 = AlSys(alSysQuantity, alSysPrice,
                         alSysCode, alSysBatteries) # creating instance of the AlarmSystem class (object)

print("Alarm system stock was created")
print("\n\n")

# Vacuum cleaner
print("Creating a vacuum cleaner stock")
print("Add new information: ")
vacCleanCode = str(input(" - Input stock code: "))
vacCleanPrice = float(input(" - Input price without VAT: "))
vacCleanQuantity = int(input(" - Unit in stock: "))
vacCleanWattage = str(input(" - Input wattage: "))
vacClean1 = VacClean(
    vacCleanQuantity, vacCleanPrice, vacCleanCode, vacCleanWattage) # creating instance of the VacuumCleaner class (object)

print("Vacuum cleaner system stock was created")
print("\n\n")

# Steering wheel cover
print("Creating a steering wheel cover stock")
print("Add new information: ")
stWheelCoverCode = str(input(" - Input stock code: "))
stWheelCoverPrice = float(input(" - Input price without VAT: "))
stWheelCoverQuantity = int(input(" - Unit in stock: "))
stWheelCoverColour = str(input(" - Input colour: "))
stWheelCover1 = SteerWheelCov(
    stWheelCoverQuantity, stWheelCoverPrice, stWheelCoverCode, stWheelCoverColour)# creating instance of the SteeringWheelCover class (object)

print("Steering wheel cover stock was created")
print("\n\n")

# creating a tuple with all the objects
group = (navSys1, alSyst1, vacClean1, stWheelCover1)


print("Starting loop...")
loop = True
while(loop == True):
    # looping trough all the objects in the tuple
    for x in group:
        print("Class: " + type(x).__name__)
        print("--Printing item information:--")
        print(x)  # this will invoke the __str__ method
        print("\n\n")

        # prompt the user to input a value for the quantity to increase
        add = int(input("Increase quantity: "))
        x.increaseStock(add)  # pass the value to the method
        print("--Printing item information:--")
        print(x)  # this will invoke the __str__ method
        print("\n\n")

        # prompt the user to input a value for the quantity to sell
        sell = int(input("Sell quantity: "))
        x.sellStock(sell)  # pass the value to the method
        print("--Printing item information:--")
        print(x)  # this will invoke the __str__ method
        print("\n\n")

        price = float(input("Set price:"))  # prompt the user to input a value for the price
        x.setPriceWithoutVAT(price)  # pass the value to the method
        print("--Printing item information:--")
        print(x)  # this will invoke the __str__ method
        print("\n\n")

    # asking the user if they want to continue or not
    ans = str(input("Do you want to continue? y/n   "))
    if(ans == "n"):
        loop = False
