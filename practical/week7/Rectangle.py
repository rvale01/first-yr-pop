class Rectangle:
    width = 1.0
    height = 1.0

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def getArea(self):
        return self.width*self.height

    def getPerimeter(self):
        return (self.width+self.height)*2


rect1 = Rectangle(4, 40)
rect2 = Rectangle(3.5, 35.9)

# rectangle 1
print("Rectangle 1: ")
print("width: %i" % rect1.width)
print("height: %i" % rect1.height)
print("Area: ", rect1.getArea())
print("Perimeter: ", rect1.getPerimeter())

print()
print()

# rectangle 2
print("Rectangle 2: ")
print("width: %.2f" % rect2.width)
print("height: %.2f" % rect2.height)
print("Area: ", rect2.getArea())
print("Perimeter: ", rect2.getPerimeter())
