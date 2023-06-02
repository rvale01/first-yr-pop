
class Animal:
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age

    def getAge(self):
        print(self.name+"'s age : "+str(self.age))
    
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def meow(self):
        print(self.name + " ...is meowing!")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def fly(self):
        print(self.name + " ...is flying!")

c = Cat("Bob", 10)
c.meow()
c.getAge()

b = Bird("Tom", 4)
b.fly()
b.getAge()