from abc import *
class Demo1(ABC):
    def m3(self):
       print("Implemented method")
   # @abstractmethod
   # def m1(self):
   #   pass
  
    

d = Demo1()
d.m3()