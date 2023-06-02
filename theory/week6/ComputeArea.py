# Compare with ComputeArea.c from week 2

PI = 3.14159

# Read radius as float
radius = float(input("input radius: \n"))

# If the radius is not a negative number
if(radius >= 0):
    area = PI*radius*radius
    print("The radius is %.2f", radius)
else:
    print("Radius cannot be negative")
