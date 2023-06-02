class SeaAnimal:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(self.name+"...swimming!")

class LandAnimal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name+"...walking!")

class Amphibian(SeaAnimal, LandAnimal):
    def __init__(self, name, category):
        super().__init__(name)
        self.category = category

    def getCategory(self):
        print("Its category is: "+self.category)

penguin = Amphibian("Chinstrap", "Flightless bird")

penguin.walk()
penguin.swim()
penguin.getCategory()
