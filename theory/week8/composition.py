class House:
    def __init__(self, noRooms):
        self.noRooms = noRooms
        self.rooms = []

        for x in range(0, noRooms):
            self.rooms.append(Room(0, ""))
    
    def displayRooms(self):
        # loop through the rooms list
        for n in self.rooms:
            print ("Room %i is %s " % (n.number, n.colour))

    def setRoom(self, n, number, colour):
        self.rooms[n].number = number
        self.rooms[n].colour = colour


class Room:
    def __init__(self, number, colour):
        self.number=number
        self.colour=colour

# myHouse has 3 rooms
myHouse = House(3)

# set the number and colour of each room
myHouse.setRoom(0,1,"Green")
myHouse.setRoom(1,2,"Yellow")
myHouse.setRoom(2,3,"Red")

myHouse.displayRooms()
