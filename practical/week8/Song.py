class Song:
    def __init__(self, name, length):
        self.__name = name
        self.__length = length

    def getName(self):
        return self.__name

    def getLength(self):
        return self.__length

    def setName(self, name):
        self.__name = name

    def setLength(self, length):
        self.__length = length

    def display(self):
        print("Song's name is: " + str(self.getName()) +
              " its length is %.2f" % self.getLength())


def checkName():
    isName = False

    while(not isName):
        name = str(input("Input the name of the dog:"))
        if 2 <= len(name) <= 10:
            isName = True
            return name
        else:
            print("The name is too short or long")


def checkLength():
    isLength = False

    while(not isLength):
        length = int(input("Input the age of the dog"))
        if 100 >= length >= 0.1:
            isLength = True
            return length
        else:
            print("The age is out of range")


objList = []

for x in range(4):
    name = checkName()
    length = checkLength()
    song = Song(name, length)
    objList.append(song)

for x in objList:
    x.display()
    