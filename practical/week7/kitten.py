# 1.1
# class Kitten:
#   pass

# kit = Kitten()
# kit2 = Kitten()
# print(kit)
# print(kit2)

# 1.2
# class Kitten:
#     def __init__(self):
#         self.age = 1

#     def displayAge(self):
#         print(self.age)

# kitt = Kitten()

# kitt.displayAge()

# 1.3
# class Kitten:
#     # def __init__(self):
#     #     self.age = 1

#     def displayAge(self):
#         print("Age unknown")

# kitt = Kitten()

# kitt.displayAge()

# 1.4, 1.5, 1.6, 1.7
# class Kitten:
#     def __init__(self, value):
#         self.age = value

#     def displayAge(self):
#         print(self.age)
    
#     def set_age(self, valu)

# kitt = Kitten(3)
# kitt2 = Kitten(5)

# kitt.displayAge()
# kitt2.displayAge()
# kitt.displayAge()


# 1.8
# you can't create an object without passing a paramether if the constructor requires a paramether.
# Because the constructor requires a paramether

# 1.9
class Kitten:
    def __init__(self, value = None):
        self.age = value

    def displayAge(self):
        print(self.age)
    
    def set_age(self, value):
        self.age = value

kitt = Kitten(3)
kitt2 = Kitten(4)
kitt3 = Kitten()
kitt.displayAge()
kitt2.displayAge()
kitt.displayAge()
kitt.set_age(5)
kitt.displayAge()
print(kitt)
print(kitt2)
kitt3.displayAge()
# 1.9 when using a constructor, you have to set a value when you create the object,
# with a method you can change/set the value at any point after the object is created