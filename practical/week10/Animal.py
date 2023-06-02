from abc import *


class Animal(ABC):
    def __init__(self, numberOfLegs):
        self.__numberOfLegs = numberOfLegs

    def getNumberOfLegs(self):
        return self.__numberOfLegs

    def setNumberOfLegs(self, numberOfLegs):
        self.__numberOfLegs = numberOfLegs

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def walk(self):
        pass


class Pet(ABC):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    @abstractmethod
    def play(self):
        pass


class Cat(Pet, Animal):
    def __init__(self, numberOfLegs, name):
        Animal.__init__(self, numberOfLegs)
        Pet.__init__(self, name)

    def play(self):
        print(self.getName() + " plays with tail")

    def eat(self):
        print(self.getName() + " eats mice")

    def walk(self):
        print(self.getName() + " walks with " + str(self.getNumberOfLegs()) + "legs")

class Fish(Pet, Animal):
    def __init__(self, numberOfLegs, name):
        Animal.__init__(self, numberOfLegs)
        Pet.__init__(self, name)

    def play(self):
        print(self.getName() + " plays pokemon")

    def eat(self):
        print(self.getName() + " eats plants")

    def walk(self):
        print(self.getName() + " can't walk ")


class Spider(Animal):
    def __init__(self, numberOfLegs = 8):
        super().__init__(numberOfLegs)

    def eat(self):
        print("Spider eats fly")

    def walk(self):
        print("Spider walks with " + str(self.getNumberOfLegs()) + " legs")


s = Spider()
c = Cat(4, "Max")
f = Fish(0, "Nemo")
s.eat()
s.walk()
c.eat()

#Polymorphism
for x in (c,f):
    x.eat()
    x.walk()
    x.play()