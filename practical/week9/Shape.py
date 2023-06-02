class Shape:
    def __init__(self, colour = "Black"):
        self._colour = colour
        print("Shape constructor is called")
    
    def display(self): 
        print("Shape is displaying")

    def getColour(self):
        return self._colour

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        print("Rectangle constructor is called") 
    
    def display(self):
        print("Rectangle is displaying")

    def getRectangleCOlour(self):
        return self.getColour()

class Square(Shape):
    pass

rec = Rectangle() 
# rec.displayShape() 
# rec.displayRectangle()

print(rec.getRectangleCOlour())
rec.display()

sq = Square()
sq.display()
# sq.getRectangleCOlour()

# 1.7
# yes, the display in the rectangle si overriding the one inherited from the Shape class
# this happens if two methods have the same name and ask for the same paramethers
#1.9
# the square is not a subclass of the rectangle class, so it won't inherit the getrectangleColour method


