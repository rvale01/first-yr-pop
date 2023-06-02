class Animal:
  def __init__(self, name=None, age=None):
    self.name = name
    self.age = age
  
  def eat(self):
      print("eats food!")

class Cat(Animal): 
    def __init__(self, name, age):
        super().__init__(name,age)

    def eat(self):
        print(self.name+" eats rat!")
        
    def meow(self):
      print(self.name+"...meowing!")

c = Cat("Bela", 1.0) 
c.meow()
c.eat()
