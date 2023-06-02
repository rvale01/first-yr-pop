class Kitten:
    breed = "Abyssinian"

    def __init__(self, value):
        self.age = value
    def set_age(self, value):
        self.age = value
    def display_age(self):
        print(self.age)

kitt = Kitten(3)
kitt2 = Kitten(4)

kitt.display_age() 
kitt2.display_age() 
kitt.display_age() 
kitt.set_age(5) 
kitt.display_age()
print(kitt.breed) 
print(kitt2.breed)
print(Kitten.breed)
# print(Kitten.age) it does not work
Kitten.breed = "American Bobtail"
print(Kitten.breed)
print(kitt.breed)
print(kitt2.breed)

kitt.breed = 'none'
print(kitt.breed)