#Base class
class Animal:
  #constructor
  def __init__(self, name=None):
    self.__name = name
    
  def getName(self):
      return self.__name

  def sound(self):
      print("Unknown sound")

#sub class 1
class Cat(Animal): 
    def __init__(self, name = None):
        super().__init__(name)

    def sound(self):
        print(self.getName()        +"...meowing!")
     
#sub class 2
class Bird(Animal): 
    def __init__(self, name = None):
        super().__init__(name)

    def sound(self):
         print(self.getName()+"...tweeting!")
     

c = Cat("Bela") 
c.sound()
print(isinstance(c, Cat))

b = Bird("Happy")
b.sound()
print(isinstance(b, Bird))
#print(isinstance(b, Cat))


a = Animal()
a.sound()
#print(isinstance(a, Animal))
#print(isinstance(b, Animal))
a = c
a.sound()
#print(isinstance(a, Bird))
#print(isinstance(a, Animal))
a = b
a.sound()

#for animal in (c,b):
 #   animal.sound()

#This is Python FLAW...Java does not support this. This should be a type mismatch
# print("Assigning c type to b type")
b = c
b.sound()
# b = a
# b.sound()
print(isinstance(b,Cat))

#creating another cat object
#print("Down casting")
#c1 = Cat()
#c1 = a
#c1.sound()
