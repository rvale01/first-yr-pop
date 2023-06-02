class Dog:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def display(self):
        print("The name of the dog is: %s and the age is: %i" %
              (self.__name, self.__age))


def checkName():
    isName = False

    while(not isName):
        name = str(input("Input the name of the dog:"))
        if 2 <= len(name) <= 10:
            isName = True
            return name
        else:
            print("The name is too short or long")


def checkAge():
    isAge = False

    while(not isAge):
        age = int(input("Input the age of the dog"))
        if 20 >= age >= 0.1:
            isAge = True
            return age
        else:
            print("The age is out of range")


objList = []

for x in range(4):
    name = checkName()
    age = checkAge()
    dog = Dog(name, age)
    objList.append(dog)

for x in objList:
    x.display()
    
