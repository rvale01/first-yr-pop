class Animal:
  def __init__(self, name=None, age=None):
    self.__name = name
    self.__age = age
  
  def eat(self):
      print("eats food!")

  def __str__(self):
      return "Animal's name is: "+ self.__name+ "\nIts age is: "+str(self.__age)


class Cat(Animal): 
    def __init__(self, name, age, colour):
        super().__init__(name,age)
        self.__colour = colour

    def __str__(self):
        return super().__str__()+"\nIts colour is: "+self.__colour+self.__name
       # return "\nIts colour is: "+self.__colour


class PersianCat(Cat):
    def __init__(self, name, age, colour):
        super().__init__(name,age,colour)

    def __str__(self):
        return super().__str__()

c = PersianCat("Bela", 1.0, "White") 
print(c)
